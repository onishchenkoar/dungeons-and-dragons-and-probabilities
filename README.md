# dungeons-and-dragons-and-probabilities
Probability calculations for different DnD things


## General DnD mechanics

[Two_ways_to_calculate_critical_hit_damage.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/Two_ways_to_calculate_critical_hit_damage.ipynb) &mdash; a quick comparison of Player's Handbook vs. Critical Role way of calculating critical damage.

[Vanishing_advantage.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/Vanishing_advantage.ipynb) &mdash; when player's advantage on an attack depends on target's saving throws.

[dndrv.py](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/dndrv.py) &mdash; I define a class for a discrete random variable that allows addition, subtraction, and multiplication with other discrete random variables. Uses NumPy, SciPy, matplotlib.

[Animate_Objects_and_War_Caster_vs_Resilient.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/Animate_Objects_and_War_Caster_vs_Resilient.ipynb) &mdash; to be finished. An unformatted notebook in which I have researched two problems:
1. What is an average damage of 10 tiny animated objects (as in [Animate Objects](https://roll20.net/compendium/dnd5e/Animate%20Objects#content) spell) against different levels of Armor Class (*considers the probability to hit and the probability of critical damage*).
2. When is Resilient feat better for concentration than War Caster feat?


## CritRoleStats - All Rolls Tal'Dorei table
[Cleanup_All_Rolls_TalDorei.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/Cleanup_All_Rolls_TalDorei.ipynb) &mdash; cleanup of [All Rolls Tal'Dorei table](https://docs.google.com/spreadsheets/d/1OEg29XbL_YpO0m5JrLQpOPYTnxVsIg8iP67EYUrtRJg/edit?usp=sharing).

[All_Rolls_TalDorei_EDA.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/All_Rolls_TalDorei_EDA.ipynb) &mdash; exploratary data analysis of the first campaign of Critical Role.

[All_Rolls_TalDorei_d20_rolls.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/All_Rolls_TalDorei_d20_rolls.ipynb) &mdash; analysis of distributions of d20 rolls in the first campaign of Critical Role.


## Critical Role
[fenthras_vs_lss.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/fenthras_vs_sky_sentinel/fenthras_vs_lss.ipynb) &mdash; numerical analysis of two longbows from Critical Role, following [a discussion](https://www.reddit.com/r/criticalrole/comments/59fans/spoilers_e72_what_is_the_difference_in_damage/) on Reddit. I generate different conditions and compare average damages dealt by each of the bows.

[CR_E66_House_edge.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/CR_E66_House_edge.ipynb) &mdash; determining the best strategy and house edge (expected winnings) for Avandra's Favor, a dice game from [episode 66](https://youtu.be/jgmBV5NA2A8) of Critical Role.

[CR_E71_Gate_scroll_roll.ipynb](https://github.com/onishchenkoar/dungeons-and-dragons-and-probabilities/blob/main/CR_E71_Gate_scroll_roll.ipynb) &mdash; is d20 with advantage + d12 Inspiration + 8 a risky roll against DC 19? This is a pivotal moment in [episode 71](https://youtu.be/-I_tnzBKSWk) of Critical Role.
