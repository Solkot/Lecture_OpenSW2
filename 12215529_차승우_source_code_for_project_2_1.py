import pandas as pd
from pandas import DataFrame, Series

csv_file_path = '/content/drive/MyDrive/2019_kbo_for_kaggle_v2.csv' #주소의 경우 변경이 필요합니다.

df = pd.read_csv(csv_file_path)

df_copy = df.copy()
df_copy_2015 = df_copy.loc[(df_copy['year'] == 2015), :]
df_copy_2016 = df_copy.loc[(df_copy['year'] == 2016), :]
df_copy_2017 = df_copy.loc[(df_copy['year'] == 2017), :]
df_copy_2018 = df_copy.loc[(df_copy['year'] == 2018), :]

#문제 2.1 - 1
#2015
top_10_H_2015 = df_copy_2015.sort_values(by='H', ascending=False).head(10)['batter_name'].tolist()
top_10_avg_2015 = df_copy_2015.sort_values(by='avg', ascending=False).head(10)['batter_name'].tolist()
top_10_HR_2015 = df_copy_2015.sort_values(by='HR', ascending=False).head(10)['batter_name'].tolist()
top_10_OBP_2015 = df_copy_2015.sort_values(by='OBP', ascending=False).head(10)['batter_name'].tolist()

result1_2015 = pd.DataFrame({'H' : top_10_H_2015,
                       'avg' : top_10_avg_2015,
                       'HR' : top_10_HR_2015,
                       'OBP' : top_10_OBP_2015}, index = range(1, 11))
#2016
top_10_H_2016 = df_copy_2016.sort_values(by='H', ascending=False).head(10)['batter_name'].tolist()
top_10_avg_2016 = df_copy_2016.sort_values(by='avg', ascending=False).head(10)['batter_name'].tolist()
top_10_HR_2016 = df_copy_2016.sort_values(by='HR', ascending=False).head(10)['batter_name'].tolist()
top_10_OBP_2016 = df_copy_2016.sort_values(by='OBP', ascending=False).head(10)['batter_name'].tolist()

result1_2016 = pd.DataFrame({'H' : top_10_H_2016,
                       'avg' : top_10_avg_2016,
                       'HR' : top_10_HR_2016,
                       'OBP' : top_10_OBP_2016}, index = range(1, 11))
#2017
top_10_H_2017 = df_copy_2017.sort_values(by='H', ascending=False).head(10)['batter_name'].tolist()
top_10_avg_2017 = df_copy_2017.sort_values(by='avg', ascending=False).head(10)['batter_name'].tolist()
top_10_HR_2017 = df_copy_2017.sort_values(by='HR', ascending=False).head(10)['batter_name'].tolist()
top_10_OBP_2017 = df_copy_2017.sort_values(by='OBP', ascending=False).head(10)['batter_name'].tolist()

result1_2017 = pd.DataFrame({'H' : top_10_H_2017,
                       'avg' : top_10_avg_2017,
                       'HR' : top_10_HR_2017,
                       'OBP' : top_10_OBP_2017}, index = range(1, 11))

#2018
top_10_H_2018 = df_copy_2018.sort_values(by='H', ascending=False).head(10)['batter_name'].tolist()
top_10_avg_2018 = df_copy_2018.sort_values(by='avg', ascending=False).head(10)['batter_name'].tolist()
top_10_HR_2018 = df_copy_2018.sort_values(by='HR', ascending=False).head(10)['batter_name'].tolist()
top_10_OBP_2018 = df_copy_2018.sort_values(by='OBP', ascending=False).head(10)['batter_name'].tolist()

result1_2018 = pd.DataFrame({'H' : top_10_H_2018,
                       'avg' : top_10_avg_2018,
                       'HR' : top_10_HR_2018,
                       'OBP' : top_10_OBP_2018}, index = range(1, 11))
print('2015 year')
print(result1_2015)
print('\n')
print('2016 year')
print(result1_2016)
print('\n')
print('2017 year')
print(result1_2017)
print('\n')
print('2018 year')
print(result1_2018)
print('\n')

#문제 2.1 - 2
df_copy2 = df_copy.copy()
df_copy2 = df_copy = df_copy.loc[(df_copy['year'] == 2018), :]
position = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
name = []
for i in position:
  name.append(*((df_copy.loc[(df_copy['cp'] == i), :]).sort_values(by='war', ascending=False).head(1)['batter_name'].tolist()))

result2 = pd.DataFrame({position[0] : [name[0]],
                        position[1] : [name[1]],
                        position[2] : [name[2]],
                        position[3] : [name[3]],
                        position[4] : [name[4]],
                        position[5] : [name[5]],
                        position[6] : [name[6]],
                        position[7] : [name[7]]}, index = ['Name'])

print(result2)
print('\n')

#문제 2.1 - 3
df_copy3 = df.copy()
df_copy3 = df_copy3[['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG', 'salary']]

correlation_matrix = df_copy3.corr()

# 'salary'와의 상관계수를 확인하고 가장 높은 변수 선택
highest_correlation_var = correlation_matrix['salary'].sort_values(ascending=False).index[1]

for column in df_copy3.columns:
    if column != 'salary':
        correlation = correlation_matrix['salary'][column]
#       print(f"상관계수 (salary vs. {column}): {correlation}")

print(f"The Highest correlations with salary : {highest_correlation_var}, {correlation_matrix['salary'][highest_correlation_var]}")
