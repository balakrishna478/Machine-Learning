
import pandas as pd
# read the CSV file
try:
    df = pd.read_csv('cars.csv')
    df = pd.DataFrame(df)
# Computing conditional probabilities
    for i in range(len(df['make'].unique())):
        for j in range(len(df['aspiration'].unique())):
            x1 = df['make'].unique()[i]
            y1 = df['aspiration'].unique()[j]
            df1 = df[df['make'].str.contains(x1) & df['aspiration'].str.contains(y1)]
            l = len(df1)
            n = df.make.value_counts()[df['make'].unique()[i]]
# Display conditional probabilities
            print("Prob(aspiration={}/make={}) =".format(y1,x1),"{:.2f}".format(((l / n) * 100)), "%")
    print('\n')
# Computing unconditional probabilities
    for k in df['make'].unique():
        p = df.make.value_counts()[k]
        q = len(df['make'])
# Display unconditional probabilities
        print("Prob(make={}) =".format(k), ("{:.2f}".format(((p / q) * 100))), "%")
except FileNotFoundError:
    print("\n File Not Found")