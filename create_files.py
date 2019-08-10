"""
Create issue files from csv
"""
import pandas as pd

t = """\
{title}

{line1}

{line2}
"""
df = pd.read_csv('issues.csv')
for i, row in df.iterrows():
    dd = row.to_dict()
    s = t.format(**dd)
    fn = "%s.txt" % dd['num']
    with open(fn, 'w') as f:
        f.write(s)