import csv

# 첫번째 행에 컴퓨터, 노트북, 태블릿 ==> ['컴퓨터', '노트북' , '태블릿'] <ㅡ 하나 하나로 보고 
# 두번째 행에 100, 80, 60 ==> [100, 80, 60]
# 리스트 형태로 표현 ==> test_list <- 담아라

test_list = [['컴퓨터', '노트북', '태블릿'], [100, 80, 60]]

# 각각 2개의 리스트를 가진 리스트를 만들었어.

# csv 를 이용해 파일(test.csv)로 출력

#with 쓰면 close 안해도 된데
# 
with open('test.csv', 'w', newline='', encoding = 'utf-8') as f:
  #쓰는 객체는 f야 구분자는 ,di.
  a = csv.writer(f, delimiter=',') #구분자는 , 임
  a.writerow(test_list) # 인코딩이 안맞아서 깨지는거 위에 utf-8로 잡았음