print('Hello')

a=0
print(a)
print(type(a))

b = 'Hello world'
print(b)
print(type(b))

c="'안녕하세요'" # '안녕'을 표현하고 싶어서 ""로 쌌어!
print(c)

d="\'안녕하세요!!!\'"
print(d)

print(b+c)
print(2*3)
print('2'*3)
print(c*3)

print("="*10)

print(b)

print(b[-0])

print(b[-1])

# 추출하는 것, 커서 앞에 시작하는 위치값이 0 -> 
e = '안녕하세요'

print(e[0:2])
print(e[1:3])
print(e[0:5:2]) # 0-4까지 2칸씩 건너오며, 0, 2, 4 위치 값 2는 스텝

#처음부터 끝까지
print(e[:])

#====================list ======================== []
#객체 만들기

l = list() # 객체 만들어진 것
print(l, type(1))

lst = [1, 2, 3] #리스트는 대괄호로 만들어서 리스트를 만들었어!!
print(lst, type(lst))
l = [ 1,2,3,4,5,6,7,8,9,10,55]
print(l, type(l))

# l의 첫번째 값만 출력
print(l[0])
# l의 길이 출력 ==> len 함수 사용
print('길이 : ', len(l))
# l의 마지막 값 출력
print(l[-1])
print('마지막을 len 이용 : ', l[len(l)-1] )

#l리스트의 첫번째 값을 99로 수정
l[0] = 99
print(l)

#l의 첫번째 값에 리스트 [1,2,3] 수정
l[1] = [1,2,3]
print(l)

# l의 두번째 자리
l[2] = '문자'
print(l)

# 맨 마지막의 자리에 문자 넣기 
l.append(999)
print(l)

# 숫자 5 지우기
l.remove(5)
print(l)

# ========================tuple========================()
t = tuple() # 객체 
print(t, type(t))
t1 = (1,2,3)
print(t1, type(t1))

# 0번째 자리
print(t1[0])


print(t1[0], t1[0:2]) #값이 2개라서 튜플로 나와

print(t1+t1)

# t1의 첫번재를 5로 수정
#t1[0] = 5
#print(t1) # 튜플은 수정이 안되서 오류발생!!!!!!!

# ========================dictionary======================== {}
#dict 키와 벨류로 구성됨 { } 사용
d1 = dict()
print(d1, type(d1))

d = {
  'a' : 1,
  'b' : 2,
  'c' : 3,
  'd' : 4

}

print(d, type(d))

#자바의 맵과 같아 키를 부르면 값이 나와
print(d['a'])

#맵이나 딕셔너리나 키값은 중복을 허용하지 않아. 33으로 출력
d['d'] = 33
print(d)

#'d'만 출력
print(d['d'])

#key값만 가지고 오는 함수
d1 = d.keys()
print("keys() : ", d1)
# 대괄호로 리스트로 반환됨.

print("keys() type : " , type(d1))
# 로 리턴됨. keys() type :  <class 'dict_keys'> 
 

dd1 = d.keys
print("keys : ", dd1)
# 딕셔너리 오브젝 객체라는 것만 알려주고 값은 함수로 구해야해. 함수는 d.keys()

d2 = d.values()
print("values() : ", d2)
print("values() type : " , type(d2))
# 로 리턴됨. values() type :  <class 'dict_values'>

dd2 = d.values
print("values : ", dd2)

d3 = d.items()
print("items() : ", d3)

dd3 = d.items
print("items : ", dd3)

################ 리스트로 유형을 바꿔야한다면

print(d.keys())
# 이걸 리스트 형태로 변환하고 싶어!!!!
print(list(d.keys()))

#리스트로 바뀐거 확인
print("type list : ", type(list(d.keys())))

# 벨류를 리스트로 바꿔보자! -> 리스트로 감싸
print(d.values())
print(list(d.values()))
print(type(list(d.values())))

# d dict의 c키값을 2로 수정
# 키가 중복이 안되는 거지 값은 들어가져

d['c'] = 2 # 3이던 2자리에 2넣자
print(d)
print(d.values()) # 1,2,2,33

# set은 중복을 허용하지 않아서 2가 없어짐
print(set(d.values())) #{1,2,33}
print(type(set(d.values()))) # type은 집합 자료형 set이라는 형태 중복불가, 순서 없음 for문 돌면 가능, 수정가능




