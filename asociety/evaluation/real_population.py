import pandas as pd

df = pd.read_csv('data/cross_section/age.csv')
def extract_mean(x):
    if not isinstance(x, str):
        return x
    s = x.split('(')
    if len(s) == 2:
        return s[0]
    return x
def extract_variation(x):
    if not isinstance(x, str):
        return x
    s = x.split('(')
    if len(s) == 2:
        return s[1].split(')')[0]
    return x
mdf = df.applymap(extract_mean)
vdf = df.applymap(extract_variation)
cdf = df.copy()

print(mdf)
print(vdf)