# dungeons-and-dragons-and-probabilities
Probability calculations for different DnD things

`fenthras_vs_sky_sentinel` &mdash; data analysis of two longbows from Critical Role, following [a discussion](https://www.reddit.com/r/criticalrole/comments/59fans/spoilers_e72_what_is_the_difference_in_damage/) on Reddit. I generate different conditions and compare average damages dealt by each of the bows.

`dndrv.py` &mdash; I define a class for a discrete random variable, that allows addition, subtraction, and multiplication with other discrete random variables. Uses NumPy, SciPy, matplotlib.

`CR_E66_House_edge.ipynb` &mdash; determining the best strategy and house edge (expected winnings) for Avandra's Favor, a dice game from [episode 66](https://youtu.be/jgmBV5NA2A8) of Critical Role.

`CR_E71_Gate_scroll_roll.ipynb` &mdash; is d20 with advantage + d12 Inspiration + 8 a risky roll against DC 19? This is a pivotal moment in [episode 71](https://youtu.be/-I_tnzBKSWk) of Critical Role
