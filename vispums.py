
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
try:
    df=pd.read_csv('ss13hil.csv')
    df1=pd.DataFrame(df)
    h=list(df1["HHL"])
    #Pie chart
    labels=["English only","Spanish","Other Indo-European languages","Asian and Pacific Island languages","Other"]
    Languages_count=[h.count(1),h.count(2),h.count(3),h.count(4),h.count(5)]
    plt.figure('pums')
    plt.subplot(2, 2, 1)
    patches, texts = plt.pie(Languages_count, startangle=242.5)
    plt.legend(patches, labels, loc="upper left",fontsize=7)
    plt.axis('equal')
    plt.title("Household Languages")
    plt.ylabel("HHL")
    # bar chart
    k=df1.loc[:,['VEH','WGTP']]
    m=[i for i in range(0,7)]
    j=[k[k['VEH']==0],k[k['VEH']==1],k[k['VEH']==2],k[k['VEH']==3],k[k['VEH']==4],k[k['VEH']==5],k[k['VEH']==6]]
    n=[]
    for i in j:
        o=i.WGTP.sum()
        n.append(o)
    p=[i/1000 for i in n]
    plt.subplot(2, 2, 3)
    plt.bar(m, p,color='red')
    plt.yticks(np.arange(0, 2000, 250))
    plt.xlabel("# of vehicles")
    plt.ylabel("Thousands of Households")
    plt.title("Vehicles Available in Households")
    # Histogram
    df3 = df1['HINCP']
    plt.subplot(2, 2, 2)
    plt.hist(df3,color='forestgreen', bins=np.logspace(np.log10(10),np.log10(10**7),100),density=True)
    plt.gca().set_xscale("log")
    df3.plot.kde(linestyle='dashed',color='black')
    plt.xscale('log')
    plt.xlim(5,2*10**7)
    plt.ticklabel_format(style='plain',axis='y')
    plt.title("Distribution of Household Income")
    plt.xlabel("Household Income($)-Log Scaled")
    plt.ylabel("Density")
    plt.grid(linestyle='dotted')
    #Scatter plot
    df1 = df["TAXP"].fillna(0)
    df2 = df["VALP"].fillna(0)
    df3= df["WGTP"]
    df4 = df["MRGP"]
    for i in range(len(df1)):
        if df1.iloc[i]==1:
            df1.iloc[i]=0
        elif df1.iloc[i]==2:
            df1.iloc[i]=1
        elif df1.iloc[i]>2 and df1.iloc[i]<=22:
            df1.iloc[i]=df1.iloc[i]*50-100
        elif df1.iloc[i]>22 and df1.iloc[i]<=62:
            df1.iloc[i]=(df1.iloc[i]-12)*100
        elif df1.iloc[i] == 63:
            df1.iloc[i] = 5500
        elif df1.iloc[i]>63:
            df1.iloc[i] = 6000+(df1.iloc[i]-64)*1000
    df1=list(df1)
    df2=list(df2)
    df3=list(df3)
    df3=np.array(df3)
    df4=list(df4)
    df4=np.array(df4)
    plt.subplot(2, 2, 4)
    plt.scatter(df2, df1, s=df3*0.15,c=df4,marker='o',cmap='seismic',alpha=0.2)
    plt.xlim(0,1200000)
    plt.ticklabel_format(style='plain',axis='x')
    plt.ylim(0,11000)
    plt.title("Property Taxes vs Property Values")
    plt.xlabel("Property Value($)")
    plt.ylabel("Taxes($)")
    cmap = plt.get_cmap('jet', 50)
    cbar = plt.colorbar()
    cbar.set_label("First Mortgage payment(Monthly $)",size=6.5)
    plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
    plt.show()
except FileNotFoundError:
    print("File Not Found")


