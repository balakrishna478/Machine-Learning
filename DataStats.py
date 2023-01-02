
import pandas as pd
try:
    df = pd.read_csv('cps.csv')
    df = pd.DataFrame(df)
    df1 = df.loc[:,['School_ID', 'Short_Name', 'Is_High_School', 'Zip', 'Student_Count_Total', 'College_Enrollment_Rate_School']]
    A = df['Grades_Offered_All']
    b = []
    LG = []
    HG = []
    for i in A:
        j = i.split(',')
        b.append(j)
    for i in b:
        if i[-1] == 'PK' or i[-1] == 'K':
            HG.append(i[-1])
        elif i[-1].isdigit():
            HG.append(i[-1])
        for j in i:
            if j == 'PK' or j == 'K' or j.isdigit():
                LG.append(j)
                break
    for i in range(len(LG)):
        df1.loc[i, ['Lowest_grade']] = LG[i]
        df1.loc[i, ['Highest_Grade']] = HG[i]
    a = df['School_Hours'].fillna('NM')
    k = []
    count7 = 0
    count8 = 0
    count9 = 0
    for i in a:
        for n in str(i):
            if n.isdigit() and int(n) > 0:
                k.append(n)
                break
            elif str(n) == 'N':
                k.append('NaN')
    for i in k:
        if i == '7':
            count7 += 1
        elif i == '8':
            count8 += 1
        elif i=='9':
            count9 += 1
    for i in range(len(k)):
        df1.loc[i, ['School_Start_Hour']] =k[i]
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.max_rows', 1000)
    df1["College_Enrollment_Rate_School"] = df1["College_Enrollment_Rate_School"].fillna(df1["College_Enrollment_Rate_School"].mean(),inplace=False)
    df1['Is_High_School'] = df1['Is_High_School'].replace({True: 'yes', False: 'no'})
    A = df1[df1['Is_High_School'] == 'no']
    B = round(A['Student_Count_Total'].mean(), 2)
    C = round(A['Student_Count_Total'].std(), 2)
    A1 = df1[df1['Is_High_School']=='yes']
    B1 = round(A1["College_Enrollment_Rate_School"].mean(),2)
    C1 = round(A1["College_Enrollment_Rate_School"].std(),2)
    df1['Is_High_School'] = df1['Is_High_School'].replace({'yes': True, 'no': False})
    print()
    print(df1.head(10))
    print()
    print(f'College Enrollment Rate for High Schools = {B1} (sd={C1})')
    print()
    print(f"Total Student Count for non High-schools = {B} (sd={C})")
    print()
    print('Distribution of Starting Hours:')
    print(f"8am:  {count8}")
    print(f"7am:  {count7}")
    print(f"9am:  {count9}")
    D = list(df['Zip'])
    count = 0
    for i in D:
        if str(i).isdigit() and i == 60601 or i == 60602 or i == 60603 or i == 60604 or i == 60605 or i == 60606 or i == 60607 or i == 60616 or str(
                i) == 'nan':
            count += 1
    E = len(D) - count
    print()
    print(f'Number of schools outside Loop: {E}')
except FileNotFoundError:
    print("\n File Not Found")