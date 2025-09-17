#조건문

a = 2

if (a==1):
  print(1)
else : 
  print('1 아님')

if (a == 1):
  print(1)
elif a==2 :
  print(2)
else : 
  print(3)

#반복문
for i in [1,2,3]:
  print(i)
  #in은 저장소의 일종, 리스트가 들어간거임

for i in (4, 5, 6): # 튜플이 들어가도 상관없어!
  print(i)

for i in 'Hello' :
  print(i)
  #하나하나가 리턴이 됨

#시작점의 증감을 뺸다?

print('=' * 20)
num = 5
while num > 0 :
  print(num)
  num -=1

print("--while--")

# num이 6이면 end를 출력하고 종료 (while문 사용)

num = 10 # 10 9 8 7 end

#2차
while num > 0: 
  if num == 6:
    print('== end ==') # 6일때 end 출력한다.
    break
  print(num, end = ' ') # num 울 출력하되 옆에 공백을 넣는다.
  num -= 1 # 10으로 부터 하나씩 감소시킨다.

# 1차
#while num >6 :
#  print(num, end=' ')
#  num -=1 # 1감소 시킴
#print('--end--')

print('=' * 20)

# num 큰 수에서 test 값이 있는지 비교 조회
nums = [1,2,3,4,5]
test = (3, 6, 7)
for i in nums: # 맨처음 i는 1 
  if i in test: # 3,6,7에 i가 있는지 확인 
    print(i) # 있는 값은 3이라서 3만 찍힘

# 10의 범위 안에 숫자 출력하기
for i in range(10):
  print(i, end=' ')
print()

# 100까지의 수 중 7의 배수와 합계 출력
sum = 0
for i in range(101): # 101까지 돌릴게, range는 마지막 것을 포함하지 않아
  if i % 7 == 0: # 7로 나눈 것
   sum += i   
   print(i, end= ' ')
print('\nsum: ' , sum)

d1 = {
  'a' : 1,
  'b' : 2,
  'c' : 3  
}

# d1의 value의 최대값 출력
print(max(d1)) 

#1차
max = max(d1.values())
print('max : ', max) # 밸류값을 구했어

#2차
# d1의 value의 최대값을 가진 키를 출력
print(d1.items()) #items는 키 벨류 묶음으로 나와
# 최대값 3의 key값 구하기

# item은 2자리니까 kv 두개 와도 됨
for k, v in d1.items(): 
  print('key : ', k , 'value : ', v)
  if v == max : 
    print('max key : ' , k)


# * * *
# * * *
# * * *

#점찍기

for i in range(3): #줄
  for j in range(3): #별 갯수
    print(' * ', end='')
  print('')


