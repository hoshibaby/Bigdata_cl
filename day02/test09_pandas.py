# year sales
# 2018 350
# 2019 400
# 2020 1050
# 2021 2000
# 2022 1000
# 2023 2500


import pandas as pd
# dic 형태(data_dic)로 표현하고 이를 DataFrame 형(df)으

data_dic = {
  'year': [2018, 2019, 2020, 2021, 2022, 2023],
  'sales' : [350, 400, 1050, 2000, 1000, 2500]}

print(data_dic)
print(type(data_dic))

df = pd.DataFrame(data_dic)
print(df)
print(type(df))

print('*'*20)

##################################

#           1반    2반     3반
#중간고사   89.2   92.5    90.8
#기말고사   92.8   89.9    95.2

df2 = pd.DataFrame([[89.2, 92.5, 90.8],[92.8, 89.9, 95.2]],
                  index=['중간고사', '기말고사'],
                  columns = ['1반' , '2반' , '3반']
                  )
print(df2)

df3 = pd.DataFrame([[20251101, 'kim', 90, 80], [20251102, 'Lee', 85, 80],
                   [20251103,'park', 50, 50], [20251104,'Han', 78, 75]],
                   columns=['학번', '이름', '중간고사', '기말고사'])
print(df3)


# df3의 중간고사 합계 / df3의 기말고사 합계

print(df3.중간고사.sum())
print(df3['기말고사'].sum())


# 총점 컬럼을 생성 ==> 중간고사 + 기말고사
df3['총점'] = df3.중간고사 + df3['기말고사']


# 총점의 출력
print(df3['총점'])

# 총점의 평균 출력
print('총점 평균 : ', df3['총점'].mean())

# df3을 파일로 내보내기==> df3_pandas.csv

df3.to_csv('df3_pandas.csv', index=False)

print('*'*20)



df4 = pd.DataFrame([[20251101, 'kim', 90, 80], [20251102, 'Lee', 85, 80],
                   [20251103,'park', 50, 50], [20251104,'Han', 78, 75]],
                  )
print(df4)
df4.columns = ['학번', '이름', '시험1', '시험2']
print(df4)
print(df4.tail(2))

# df3_pandas.csv 을 읽어서 df33에 담에서 출력

df33 = pd.read_csv('df3_pandas.csv')
print(df33)

print('*'*20)

# 총점이 160이 넘는 것만 출력

#df3.df['총점'] >160

print(df3[df3['총점'] >160])

print(df33[df33['총점'] >160])