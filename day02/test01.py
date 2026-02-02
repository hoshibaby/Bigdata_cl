import csv # csv파일을 편하게 보기 위해서 import 함.
import re

f = open('day02\\popSeoul.csv','r')

reader = csv.reader(f)
# 읽어들인걸 리더에 담았어.
# print(reader) 리더 오브젝 객체가 보임

# 천단위 , 로 끊어서 문자로 인지 하고 있음
# 숫자, (천단위) 제거하기
# 문자를 숫자(float)로 변환하기
# 담기 위해서는 리스트가 필요해

output = [] # 리스트 만들었어
for i in reader:
  #print(i) # 하나의 리스트에 담겨서 출력됨 가로나열
  tmp = [] # 하나하나를 전체 리스트에 추가?
  for j in i : 
   #print(j) # 한줄에 한 항목으로 나와 세로 나열, 쉼표를 지워보자
    if re.search(r'\d',j): #숫자라면 제거해라. , r 쓴 이유는 문자라는 것
      tmp.append(float(re.sub(',', '', j))) #(쉼표를, 공백처리해줘 , j에서), float을 싸서 숫자로 해줘 뒤에 .0 됨
    else : 
      tmp.append(j)
  #print(tmp)
  output.append(tmp)
print(output) # tmp 는 각각 한줄 , output에 담아서 한줄로? 출력물을 보려고 print 한거임


# '구', '한국인', '외국인', '외국인의 비율(%)'



result = ['구', '한국인', '외국인', '외국인비율(%)'] #여러 리스트를 하나의 리스트로 묶어
for i in output:
    #예외처리
  try:
    foreign = round(i[2]/(i[1] + i[2])*100,1)
    #print(foreign) #문자 형에 안맞다고 오류가 남, 맨 첫줄은 타이틀이라서 문자라서 오류가 남 예외처리 필요
    if foreign > 5 :

      result.append([i[0], i[1], i[2], foreign]) # 4개를 하나로 보겠다
  except:
    pass # 오류나면 패스하라고 강제 세팅
print(result)

# '외국인 비율(%) 이 5%로 넘는 것만 리스트에 담아 출력


# result를 파일 (foreign.csv)

#csv 라이브러리로 다운받기
# w는 쓰기모드, 읽기모드 아님
#with open('foreign.csv', 'w', newline='', encoding = 'utf-8') as f:
  #쓰는 객체는 f야 구분자는 ,di.
#  a = csv.writer(f) #구분자는 , 임
 # a.writerow(result)

#outfile 리스트를 문자열로 바꿔서 csv로 되야해, 반복문을 돌려서 문자를 바꿔야하는데 map()은 첫번째 행위를 반복적으로 수행
#row_str = ','.join(map(str,result)) #map(funtion, 바꿀 객체)
#with open('foreign1.csv', 'w', encoding='utf-8') as outFile:
  #outFile.write(result) #에러남, 리스트를 문자열로 변환해야지 에러가 풀려, 리스트를 문자로 바꿔야지 csv로 저장
 # outFile.write(row_str)





