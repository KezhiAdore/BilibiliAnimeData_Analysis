import pandas as pd

# 文字数据转化为数字


def trans(string):
    if string[-1] == '万':
        return int(float(string[0:-1])*1e4)
    elif string[-1] == '亿':
        return int(float(string[0:-1])*1e8)
    else:
        return int(string)


filepath = 'data.csv'
df = pd.read_csv(filepath)

for i in ['barrage', 'follow', 'play']:
    for j, string in enumerate(df[i]):
        df[i][j] = trans(string)

df.to_csv('data_processed.csv', index=False)
