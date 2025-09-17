#함수 만들기
# 짝수인지 홀수 인지 확인하는 함수
def seperate():
  #a = input('수 입력')
  #입력된 값을 받아왔는데 문자로 인지하고 있어서 나머지를 구하는게 안돼. 정수로 감싸야해
  a = int(input('>>> 수 입력 : '))
  if a % 2 == 0:
    print('짝수')
  else : 
    print('홀수')

print("함수는 리턴이 있을수도 있고 없을 수도 있고")

# 두 개의 수를 더하는 덧셈 기능 : addReturn
def addReturn(a, b):
  return a + b

# seperate()

sum = addReturn(3, 5)
print("addReturn 결과 : ", sum)

print("addReturn(11,13) 결과 : " , addReturn(11,13))

# 1부터 num까지의 합을 계산하는 hap 함수 정의


def hap(num): # 함수 정의
  h = 0 #초기값
  for i in range(1, num+1):
    h += i
  return h

print(hap(10)) # 1부터 10까지의 합 출력
print(hap(100)) # 1부터 100까지의 합 출력

################################

nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]


def max_count(nums):
  counst_dic = {}
  # for 문은 num만큼 돌고 dic에 있습니까 확인, 있으면 값을 +1 증가시킴
  for i in nums:
    if i in counst_dic: #{ 1:5 , 2: 2, 3:4}
      counst_dic[i] += 1 # key 값에 따라 벨류의 값을 업데이트 해
    else:
      counst_dic[i] = 1 # {1 :1 상태임}

  return counst_dic

counts = max_count(nums) # 함수 호출
print(counts) #{1: 4, 2: 4, 3: 5} 키와 벨류로 된 딕셔너리를 만들고 싶어


# counst dict 에서 최대 max value 출력


print(max(counts.values()))

for k, v in counts.items():
  print(k, ":", v, '번')

# counst dict 에서 최대 value의 키 출력
for k, v in counts.items():
  if v == max(counts.values()):
    print(k)