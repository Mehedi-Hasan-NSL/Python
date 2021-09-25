# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os

root_dir = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(root_dir + '/breast-cancer-wisconsin.csv')
df.head(6).T

df.describe().T
#print(df.dtypes)
df.info()
plt.figure(figsize=(21,21))
plt.title("Pearson Correlation Heatmap")
corr = df.corr(method='pearson')
mask = np.tril(df.corr())
sns.heatmap(corr,
           xticklabels=corr.columns.values,
           yticklabels=corr.columns.values,
           annot = True, # to show the correlation degree on cell
           vmin=-1,
           vmax=1,
           center= 0,
           fmt='0.2g', #
           cmap= 'coolwarm',
           linewidths=3, # cells partioning line width
           linecolor='white', # for spacing line color between cells
           square=False,#to make cells square
           cbar_kws= {'orientation': 'vertical'}
           )

b, t = plt.ylim()
b += 0.5
t -= 0.5
plt.ylim(b,t)
plt.show()
################################################################################
plt.figure(figsize=(21,21))
plt.title("Spearman Correlation Heatmap")
corr = df.corr(method='spearman')
mask = np.tril(df.corr())
sns.heatmap(corr,
           xticklabels=corr.columns.values,
           yticklabels=corr.columns.values,
           annot = True, # to show the correlation degree on cell
           vmin=-1,
           vmax=1,
           center= 0,
           fmt='0.2g', #
           cmap= 'coolwarm',
           linewidths=3, # cells partioning line width
           linecolor='white', # for spacing line color between cells
           square=False,#to make cells square
           cbar_kws= {'orientation': 'vertical'}
           )

b, t = plt.ylim()
b += 0.5
t -= 0.5
plt.ylim(b,t)
plt.show()

###############################

df_mean = df[df.columns[:11]]
df_se = df.drop(df.columns[1:11], axis=1)
df_se = df_se.drop(df_se.columns[11:], axis=1)
df_worst = df.drop(df.columns[1:21], axis=1)

# #df_worst.head()
# #df.diagnosis.value_counts() \
#     .plot(kind="bar", width=0.1, color=["lightgreen", "cornflowerblue"], legend=1, figsize=(8, 5))
# plt.xlabel("(0 = Benign) (1 = Malignant)", fontsize=12)
# plt.ylabel("Count", fontsize=12)
# plt.xticks(fontsize=12);
# plt.yticks(fontsize=12)
# plt.legend(["Benign"], fontsize=12)
# plt.show()