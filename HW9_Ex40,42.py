import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

df[
    (df['population'] > 0) &
    (df['population'] < 500)
].median_house_value.mean()


min_population = df.population.min()
df[
    df['population'] == min_population
].households.max()