import pandas as pd
import sys


def cnt():
    df = pd.read_parquet("~/tmp/history.parquet")
    wrd = sys.argv[1]
    fdf = df[df['cmd'].str.contains(wrd)]
    cnt = fdf['cnt'].sum()
    print(cnt)
