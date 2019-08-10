"""
Create issue files from csv
"""
import pandas as pd

f = open('make_issues.bat', 'w')
cmd = "hub issue create -a cwebber314 -l example_label -F {num}.txt"
df = pd.read_csv('issues.csv')
for i, row in df.iterrows():
    dd = row.to_dict()
    s = cmd.format(**dd)
    print(s)
    f.write(s)
    f.write("\n")
f.close()