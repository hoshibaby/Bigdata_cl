import pandas as pd

df = pd.read_csv('day02\\apt_201910.csv', encoding='cp949', thousands=',') # 인코딩이 utf-8 dkslfktj cp949
print(len(df))

print(df.shape) # (42758, 12) 하나는 12개의 
print(df.head(10)) # 위에서 10번까지, head()안쓰면 보통 5개 데이터 형식을 미리 점검할 수 있어
print(df.tail())

print('==================================')

#면적만 출력

print(type(df))
#면적만 출력
print(df['면적']) # <- 면적인 것은 다나와 ㄱ

print(df.면적) # 컬럼명을 적어준거야!!

# 면적이 200보다 큰 거 출력

print(df[df.면적>200].head())

print('==================================')

#단지명, 가격만 출력 => 필요한 열만 보고 싶어! 필요한 행만 보고 싶어!


print(df.loc[:,['단지명','가격'] ]) # 처음부터 끝까지

# 단지명, 가격만 10개 출력

print(df.loc[:,['단지명','가격']].head(10))

print(df.loc[:10,['단지명','가격']])

print(df.loc[:10,('단지명','가격')]) # 튜플도 잘나와


# 가격을 위에서 5개 출력

print(df.loc[:,['가격']].head())

print(df.가격.head())
print(df['가격'].head())


# 면적이 130 넘는 아파트의 가격만 출력
print(df.가격[df.면적>130])

# 면적이 130 넘는 아파트의 가격만 위에서 5개 출력
print(df.가격[df.면적>130].head())
 


print('==================================')
# 면적이 130 넘고 가격이 2억 미만인 아파트의 가격 출력

print(df.가격[(df.가격<20000) & (df.면적>130)])


# 면적이 130 넘거나 가격이 2억 미만인 아파트의 가격 출력

print(df.가격[(df.가격<20000) | (df.면적>130)].head())

# 가격 내림차순으로 출력

df_desc = df.sort_values(by='가격', ascending=False) # 어센딩 펄스 하면 내림차순
print(df_desc.가격)

# 9억원 초과하는 가격으로 거래된 단지명(아파트), 가격 출력

# df.loc는 [원하는 행 조건, 원하는 열의 조건]
print(df.loc[df.가격 > 90000 , ['단지명' , '가격']])
print('*'*20)
print(df.loc[:,['단지명', '가격']][df.가격>90000])



# print(df.단지명 [df.가격>90000])

# print(df.loc[['단지명','가격']]) 

# 단가 컬럼 생성 => 가격/면적

# df.단가 는 df['단가'] 와 같지만 없는 컬럼을 생성할 때는 df['단가'] 사용
# df.단가 = df.가격 / df.면적
# print(df.단가)

df['단가'] = df.가격 / df.면적
print(df.단가)

print(df.loc[:10, ('시군구', '면적', '단가')]) # 10개 뽑아서
df1 = df.loc[:10, ('시군구', '면적', '단가')]
df1.to_csv('apt_df.csv', index = False) #index true 주면 인덱스 번호 달려 

# csv를 이용해서 데이타 내보내고
# 판다스에서는 df = pd.read_csv



print('==================================')

data_dic = {
  'name' : ['aaa', 'bbb', 'ccc', 'ddd'],
  'age' : [22, 33, 44, 55],
  'score' : [97.2, 55.6, 33.5, 22.9]
}

# dic ==> dataframe으로 

#각각 컬럼에 맞게 합계를 구해
df2 = pd.DataFrame(data_dic)
print(df2)
print(type(df2))
print(df2.sum())
#print(df2.mean()) #이름에 평균이 없어서 오류남
#나이의 평균
print(df2['age'].mean())
print(df2.age.mean())

