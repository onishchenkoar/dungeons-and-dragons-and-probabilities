from matplotlib import pyplot as plt
import numpy as np
from scipy.stats._distn_infrastructure import rv_sample


class My_rv(rv_sample):
  """Scipy's rv_discrete that can do addition and multiplication of RVs."""

  def __new__(cls, values=None):
    return super(rv_sample, cls).__new__(cls)

  def __add__(self, other):
    if isinstance(other, int):
      return My_rv(values=(self.xk + other, self.pk))
    elif isinstance(other, My_rv):
      # Shift distributions to the right in case they have negative values.
      shift = abs(min(self.xk.min(), other.xk.min()))
      dist1 = np.zeros(self.xk.max() + shift + 1)
      dist1[self.xk + shift] = self.pk
      dist2 = np.zeros(max(other.xk) + shift + 1)
      dist2[other.xk + shift] = other.pk
      dist = np.convolve(dist1, dist2)
      idx = np.where(dist > 0)[0]
      pk = dist[idx]
      # Shift the resulting distribution back to the left.
      xk = idx - 2*shift
      return My_rv(values=(xk, pk))

  def __radd__(self, other):
    return self.__add__(other)

  def __iadd__(self, other):
    return self.__add__(other)

  def __neg__(self):
    return My_rv(values=(-self.xk, self.pk))

  def __sub__(self, other):
    return self + (-other)

  def __mul__(self, other):
    if isinstance(other, int):
      return My_rv(values=(self.xk * other, self.pk))
    elif isinstance(other, float):
      return My_rv(values=(np.floor(self.xk * other), self.pk))
    elif isinstance(other, My_rv):
      # Build "tables" of values and probabilities using outer products 
      xk_table = self.xk.reshape(-1, 1) @ other.xk.reshape(1, -1)
      pk_table = self.pk.reshape(-1, 1) @ other.pk.reshape(1, -1)
      xk = np.unique(xk_table)
      pk = np.array([sum(pk_table[xk_table == x]) for x in xk])
      return My_rv(values=(xk, pk))

  def __rmul__(self, other):
    return self.__mul__(other)

  def __floordiv__(self, other):
    return My_rv(values=(self.xk // other, self.pk))

  def plot(self, *args, **kwargs):
    plt.bar(self.xk, self.pk, snap=False, *args, **kwargs)


def d20_outcome(d20, threshold, modifier=0, bonus_dice=[],
                crit_fail_values=[], crit_success_values=[]):
  """
  Returns a binary (0 and 1) or a ternary (0, 1, and 2) random value. 1 means 
  the roll is successful; 0 means the roll has failed. 2 is returned on critical
  success; it is meant specifically for doubling *damage* on a critical hit, if 
  this is how you do your criticals.

  d20 -- a random value for a d20 roll. Can be straight, with advantage,
         with disadvantage.

  threshold -- Armor Class or Difficulty Class to beat.

  modifier -- all non-random integer bonuses.

  bonus_dice -- a list of random variables added to the d20 roll. E.g. Inspiration die
                and Guidance (1d4).

  crit_fail_values -- a list of integers on which failure is guaranteed. Typically,
                      it is 1, but attacks with some weapons can fail on other values.

  crit_success_values -- a list of integers on which success is guaranteed. Typically,
                         it is 20, but some subclasses make critical attacks on
                         19 and 18.
  """
  
  crit_success_mask = np.isin(d20.xk, crit_success_values)
  crit_fail_mask = np.isin(d20.xk, crit_fail_values)
  noncritical_mask = ~(crit_success_mask | crit_fail_mask)

  x_noncritical = d20.xk[noncritical_mask]
  p_noncritical = d20.pk[noncritical_mask]
  # Scaling probabilities so that their total is 1. These are conditional 
  # probabilities of each value, given it is non-critical.
  sum_noncritical = p_noncritical.sum()
  given_noncritical_rv = My_rv(values=(x_noncritical,
                                       p_noncritical / sum_noncritical))
  if bonus_dice:
    given_noncritical_rv += sum(bonus_dice)

  given_noncritical_rv += modifier
  success = given_noncritical_rv.xk >= threshold
  fail = given_noncritical_rv.xk < threshold

  # Scaling probabilities back to non-conditionals with sum_noncritical.
  p_crit_success = d20.pk[crit_success_mask].sum()
  p_success = given_noncritical_rv.pk[success].sum() * sum_noncritical
  p_fail = d20.pk[crit_fail_mask].sum()\
           + given_noncritical_rv.pk[fail].sum() * sum_noncritical
  return My_rv(values=([0, 1], [p_fail, p_success + p_crit_success]))



D4 = My_rv(values=(np.arange(1, 5), [1/4]*4))
D6 = My_rv(values=(np.arange(1, 7), [1/6]*6))
D8 = My_rv(values=(np.arange(1, 9), [1/8]*8))
D10 = My_rv(values=(np.arange(1, 11), [1/10]*10))
D12 = My_rv(values=(np.arange(1, 13), [1/12]*12))
D20 = My_rv(values=(np.arange(1, 21), [1/20]*20))
D20_ADV = My_rv(values=(np.arange(1, 21),
                [(2*i - 1) / 400 for i in range(1, 21)]))
D20_DISADV = My_rv(values=(np.arange(1, 21),
                   [(2*i - 1) / 400 for i in range(20, 0, -1)]))
