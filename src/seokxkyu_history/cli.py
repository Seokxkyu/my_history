import pandas as pd
import sys
import argparse

def argp():
    parser = argparse.ArgumentParser(description='history searching program')
    group = parser.add_mutually_exclusive_group()
    
    group.add_argument('-c', '--count', type=str, help='mh -c <cmd>')
    group.add_argument('-t', '--top', type=str, help='mh -t <YYYY-MM-DD>')

    args = parser.parse_args()

    if args.count:
        count(args.count)
    elif args.top:
        top_dates(args.top)
    else:
        print('error')

def count(cmd):
    count = cnt(cmd)
    print(f'{cmd} 사용 횟수는 {count}회 입니다.')


def top_dates(date):
    df = read_parquet()
    fdf = df[df['dt'] == date].sort_values(by='cnt', ascending=False).head(10)
    fdf = fdf.drop(columns=['dt'])
    print(fdf.to_string(index=False))
    

def cnt(q):
    df = read_parquet()
    df = read_parquet('~/tmp/history.parquet')
    fdf = df[df['cmd'] == q]
    # fdf = df[df['cmd'].str.contains(q)]
    cnt = fdf['cnt'].sum()
    # print(int(cnt))
    return cnt

def read_parquet(path='~/tmp/history.parquet'):
    df = pd.read_parquet(path)
    return df


def query():
    q = sys.argv[1]
    i = cnt(q)
    print(f'질의:{q}에 대한 결과는 {i}입니다')
    # print("질의:%s에 대한 결과는 %d입니다" %(q,i))
