#Day1
import pandas as pd
#Part1
df=pd.read_csv('day1.txt', delimiter='   ', header=None)
print(df)
sorted_df=pd.DataFrame({col:sorted(df[col]) for col in df.columns})
all_sum=0
for i in range(len(df)):
    print(sorted_df.iloc[i][0]-sorted_df.iloc[i][1])
    all_sum+=abs(sorted_df.iloc[i][0] -sorted_df.iloc[i][1])
print(all_sum)

#Part2

from collections import Counter
second_column=df[1]
counter=Counter(second_column)
all_sum_new=0
for i in range (len(sorted_df)):
                all_sum_new+=sorted_df.iloc[i][0]*counter[sorted_df.iloc[i][0]]
print(all_sum_new)
