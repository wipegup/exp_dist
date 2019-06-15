import pandas as pd
import numpy as np
split_dist = pd.read_csv('split_dist.csv', index_col= 0)
samples_to_take = 13209

def take_sample(samples = samples_to_take, dist = split_dist):
    sample = list(np.random.choice(dist.splits, size = samples, p = dist.prob))

    sample = [ s if s != 100 else round(np.random.uniform(50, 115)) for s in sample]

    return sample


def taxa_count(levels, distribution):
    if levels == 1:
        return np.random.choice(distribution)
    else:
        return sum([taxa_count(levels -1, distribution) for i in range(np.random.choice(distribution))])

to_sim = pd.read_csv('to_sim.csv', index_col= 0)
# to_sim = to_sim.head()

num_sims = 1000
simulations = []

for s in to_sim.index:
    info = to_sim.loc[s, :].to_dict()
    leaves = info['leaves']
    levels = info ['levels']
    for i in range(num_sims):
        sample = take_sample()
        to_add = info.copy()
        accounted_for = 0
        splits = 0
        while accounted_for < leaves:

            splits += 1
            accounted_for += taxa_counts(levels, sample)
        to_add['sim_split'] = splits
        simulations.append(to_add)

pd.DataFrame(simulations).to_csv('test.csv')
