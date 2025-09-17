# 표현식 연습


# 문자열이 갖는 find 함수
text = "<title>지금은 문자열 연습입니다.</title>"
print(text[0:7]) # 문자열 0에서 7까지 뽑아줘!
print(text.find('문')) # 인덱스 위치값을 알려줘 -> 반환은 int로 나오니까 위치값
print(text.find('파')) #없으면 -1을 리턴함. 제안사항이 없습니다!

# index 함수, 반환형은 int

print(text.index('문')) #있다면 위치값 리턴
#print(text.index('파'))  #없다면 오류발생

text1 = "    <title>지금은 문자열 연습입니다.</title>     "

# 공백제거

print(text1)
print(len(text1)) #38
#자바에서는 trim이 공백제거
print(text1.strip()) # 양족 공백제거 
print(len(text1)) # 38 공백 제거를 했지만 원본이 바뀌는건 아니야. 그냥 다른 변수값을 가진거고 원본은 변경사항이 없어.
print(len(text1.strip())) # 29 공백제거한 길이
print(len(text1.lstrip())) # 34 왼쪽 공백 날림

text2 = ";" # 문자열 끼리 합쳐줘
print(text1+text2)

print(text.replace('<title>', '<div>'))
print(text.replace('<title>', '')) #공백으로 리플레이스

#대문자

up = text.upper()
print(up) #타이틀이 대문자로 바뀜
print(up.lower()) #소문자로 바뀜

import re
# 라이브러리! 정규표헌식?

text3 = "<head>안녕하세요</head>"
 
body = re.search('<head.*/head>', text3) #' '에 패턴을 써주면 됨 .은 문자. # *는 0번 이상.
print('re.search : ', body)

#문자만 뽑아

body = body.group()
print('re.serach : ', body)

# [0-9], [a-z]
# ab*c : -> abc, abbc, abbbc, ac
# *(0번 이상) (없을 수도 있다는 말), +(1번 이상) ?(0이상1이하)

print('-----------------------------------------')

# re를 쓰면 문자열 자체가 바뀐다.
text4 = ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')
body = re.search('<title.*/title>', text4)
print(body)

print('-----------------------------------------')
body = body.group()
print(body)


print('연습1-----------------------------------------')
#<> 여는 것 닫는 것 사이에 있는
body1 = re.search('<.+?>', body) # . 문자열,  + 한번이상, ? 0번 이상 1번 한번이상 -> 가장 근접한 간결히 표현된거 title 만들어가
print('body1 : ', body1.group())

print('연습2-----------------------------------------')

body2 = re.search('<.+>', body) # > 닫히는 괄호가 여는 타이틀 닫는 타이틀 다 있어서 전체가 다 나와
print('body2 : ', body2.group())
# search는 문자열을 반환하는게 아니라 객체를 반환하는 거라tj group 필요

print('연습3-----------------------------------------')

body3 = re.sub('<.+?>','' , body) #sub는 3개가 들어가야해, title이 다 사라짐 여는거에서 닫는거 태그를 '' 공백으로 바꿔줘. # ? 있으니까 여는 타이틀 닫는 타이틀 각각 적용 ? 현재 태그만 하고 싶으면 <.+?>
# 만약 한글만 있는 자료를 쓰고 싶으면 이 함수로 정제작업을 함
print('body3 : ', body3)


print('-----------------------------------------')



######################################

a = [ 1, 2, 3, 4, 5, 2, 2]
print(a) # a직혀
  
#중복을 제거하고 싶어 = set

print(set(a)) #중복되는 것을 다 지워
print(type(set(a))) # 타입은 set

a = '제 이메일 주소는 ororong1@naver.com'
a += '오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr라는 메일을 사용합니다.'
print(a)
#메일 주소만 출력
mailText = re.findall(r'[a-z]+@[a-z.]+', a) #re가 가진 findall 사용. (패턴을 찾겠다) 
# r은 문자로 쳐 => [a-z에이에서 소문자 지까지] + 반복해서 와야하고, @반드시 와야하고, / a-z까지 반복와야하고 반드시 .와야하고
print('메일주소 출력 mailText: ', mailText)

mailText = re.findall(r'[a-z]+@[a-z]+', a)
#. 점 지우면 점 뒤에 것들이 날아가
print('메일주소 출력 mailText: ', mailText)

mailText = re.findall(r'[a-z]+@[a-z]', a)
#. 점 지우면 점 뒤에 것들이 날아가 +까지 지우면 반복이 안됨? 근데 뭘 반복한다는거지?
print('메일주소 출력 mailText: ', mailText)

print('-----------------------------------------')

words = ['apple', 'cat', 'barve', 'drama', 'asise', 'blow', 'coat', 'above']
# a로 시작하는 단어 출력

print('-findall----------------------------------------')
wordList = []
for i in words:
    wordList += re.findall(r'a[a-z]+', i) #a는 반드시 있고, [] 는 선택사항, a-z까지 영문자이고 +1번이상 반복적
print('~~~ a로 시작하는 단어: ', wordList)
# a로 머리가 된 것들은 다 나와 ['apple', 'at', 'arve', 'ama', 'asise', 'at', 'above']

print('-search----------------------------------------')

for i in words:
    wordList2 = re.search(r'a[a-z]+', i) #search는 객체임
    if wordList2:
      print(wordList2.group())
# 온전히 a로만 시작하는 단어를 가지고 오진 못해 리스트 아닌 단어로 쫙 나열, for 안에 들어가 있어서 +를 뺀거래

print('-match----------------------------------------')

for i in words:
 # wordList3 = re.match(r'a[a-z]+', i) # pattern 을 문자열의 첫부분과 비교, 단어가 출력이 된다.
  wordList3 =re.match(r'a\D+',i )
  if wordList3:
     print(wordList3.group())

