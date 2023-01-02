
import pandas as pd
import numpy as np
try:
# Printing  Table 1
    df=pd.read_csv('ss13hil.csv')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)
    df1=pd.DataFrame(df)
    df2=df1.rename(columns = {'HHT':'HHT-Hosehold/family type'})
    d={1: 'Married couple household', 2: 'Other family household:Male householder, no wife present', 3: 'Other family household:Female householder, no husband present', 4: 'Nonfamily household:Male householder:Living alone', 5: 'Nonfamily household:Male householder:Not living alone', 6: 'Nonfamily household:Female householder:Living alone', 7: 'Nonfamily household:Female householder:Not living alone'}
    df2['HHT-Hosehold/family type'] = df2['HHT-Hosehold/family type'].replace(d)
    df3=df2['HINCP'].groupby(df2['HHT-Hosehold/family type'])
    k=df3.describe()[['mean','std','count','min','max']]
    k=k.sort_values('mean', ascending=False)
    k = k.astype({"count":"int","min":"int","max":"int"})
    print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***")
    print(k)
    print("\n")
# Printing   Table 2
    df_table2=df1.loc[:,['HHL','ACCESS','WGTP']]
    df_table2=df_table2.dropna()
    df_table2.columns = df_table2.columns.str.replace('HHL', 'HHL-Household Language')
    labels=["English only","Spanish","Other Indo-European languages","Asian and Pacific Island languages","Other language","All"]
    p={1.0:'Yes w/ Subsrc.', 2.0:'Yes wo/ Subsrc.',3.0:'No'}
    df_table2['ACCESS'] = df_table2['ACCESS'].replace(p)
    i=[i for i in range(1,6)]
    s=dict(zip(i,labels))
    df_table2['HHL-Household Language'] = df_table2['HHL-Household Language'].replace(s)
    HHL=df_table2['WGTP'].groupby(df_table2['HHL-Household Language']).sum()
    HHL=df_table2.groupby(['HHL-Household Language','ACCESS'],as_index='labels', sort=False,group_keys=True).agg({'WGTP':'sum'})
    HHL = HHL.groupby(level=0,group_keys=False).apply(lambda x:100 * x / df_table2['WGTP'].sum()).unstack('ACCESS')
    HHL=pd.DataFrame(HHL)
    HHL=HHL[[('WGTP','Yes w/ Subsrc.'),('WGTP','Yes wo/ Subsrc.'),('WGTP','No')]]
    HHL = HHL.sort_values(('WGTP','Yes w/ Subsrc.'), ascending=False)
    HHL['WGTP','  All']= HHL.sum(numeric_only=True, axis=1)
    HHL.loc['All']= HHL.sum(numeric_only=True, axis=0)
    for x in HHL.iloc[:]:
        format = lambda x: "{:0.02%}".format(x/100)
    HHL=HHL.applymap(format)
    print("*** Table 2 - HHL vs. ACCESS - Frequency Table ***")
    print(HHL)
    print("\n")
# Printing   Table 3
    grouping=pd.qcut(df1["HINCP"], q=3, labels=['low', 'medium', 'high'])
    grouped = df1["HINCP"].groupby(grouping)
    k=grouped.describe()[["min","max","mean"]]
    k=pd.DataFrame(k)
    df2=pd.qcut(df1["WGTP"], q=3, labels=['low', 'medium', 'high'])
    df3=df1["WGTP"].groupby(grouping)
    df3=pd.DataFrame(df3)
    df3=np.array(df3)
    hhc=[]
    for i in range(0,3):
        hhc.append(df3[i][1].sum())
    k["household_count"]=hhc
    k = k.astype({"min":"int","max":"int"})
    print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***")
    print(k)
except FileNotFoundError:
    print("\n File Not Found")