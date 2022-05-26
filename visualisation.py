import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date


fig = plt.figure(figsize=(30, 30))
fig.suptitle('Crypto Coin Price Over Time')

dfs = list()
for i, file in enumerate(os.listdir('archive')):
    df = pd.read_csv(f'archive/{file}')
    if 'Close' in df.columns:
        dfs.append([df, file.replace(".csv", "")])

rows_columns = int(np.ceil(np.sqrt(len(dfs))))

i = 1
for df, coin in dfs:
    df.index = pd.to_datetime(df['Date'])
    df.drop('Date', axis=1, inplace=True)
    df.dropna(axis=0, inplace=True)
    df['Previous Close'] = df.shift()['Close']
    df['Close Percentage Change'] = (df['Close'] - df['Previous Close']) / df['Previous Close']
    mean = np.mean(df.sort_values(by='Date', ascending=False)['Close Percentage Change'].head(2))

    if mean > 0.25:
        color = 'green'
    elif mean < -0.25:
        color = 'red'
    else:
        color = 'orange'

    fig.add_subplot(rows_columns, rows_columns, i)
    i += 1
    sns.lineplot(x='Date', y='Close', data=df, color=color)
    plt.xticks(rotation=15, fontsize=4)
    plt.title(coin)

fig.show()
fig.savefig(f'images/{date.today()}.jpg')
