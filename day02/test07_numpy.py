# numpy - 수치데이터를 다루기 위한 라이브러리
# - 선형대수계산 등의 행렬연산에 사용(조금 쉽게)
# = 다차원배열 자료구조인 ndarry 지원


# pandas - 데이터분석에서 자주 사용, 테이블 형태를 다루는 라이브러리
# - 1차원 자료구조 : Series
# - 2차원 자료구조 : DataFrame -> 가장 많이 써
# - 3차원 자료구조 : Pane1 

# 단축 as 
import numpy as np  # pip install numpy 를 치면 numpy 설치됨
a = np.array([[2,3,4], [5,2,1]]) # 행렬을 만들어줘
print(a)

d = np.array([2,3,4,5,6,7]) # 1차원, 1차원이니까 
print(d)
print(d.shape) # 6개의 수를 가진 (6,) 구조로 출력
print('d.shape : ', d.shape)
print('d.dtype : ', d.dtype)
print(a.shape) # 3에 2행 (2,3)

e= np. array(([[1,2,3,4]],[[3,4,5,6]]))
# 2행 4열


print('e.shape : ', e.shape)
print('e.dtype : ', e.dtype)

print(np.zeros((2,10)))
# 0으로 만들어진 2행 10열자리 행렬
print(np.ones((2,10)))
print(np.arange(2,10)) # 2이상 10미만의 원소로 이루어진 1차원 배열

print(np.zeros((2,2,5)))

# 1로 이루어진 2행 3열의a 배열 생성

a= np.ones((2,3))
print(a)

b = np.transpose(a) # 3행 2열로 바뀜 / 행과 열이 바뀜
print(b)

arr1 = np.array([[2,3,4], [6,7,8]])
arr2 = np.array([[12,13,14], [26,27,28]])

#배열 덧셈 ==> 같은 자리의 원소끼리 덧셈
print(arr1+arr2) 
print(arr1-arr2) 
print(arr1*arr2) 
print(arr1/arr2) 


#######

# 5, 6, 6 개로 이뤄진 리스트
d_list = [[1,2,3,4,5],[2,3,4,5,6,7],[5,6,7,8,9,9]]
#d = np.array([[1,2,3,4,5],[2,3,4,5,6,7],[5,6,7,8,9,9]])
# 원소의 갯수가 서로 달라서 어레이(행렬)로 만들수 없어!!!!!!!!!!!!!!!!!!
print(d_list)
print(type(d_list))

print(d_list[:2])
#d_list[:2] = 0 ==> KeyError 어디서 어디까지는 안되고 자리 정확히 지정
d_list[2] = 0
print(d_list[:2])
print("==============")

#위에는 어디서 어디까지 한꺼번에 수정이 안됐는데 여기서는 가능
d_array = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,6,7,8,9]])
d_array[:2] = 0
print(d_array)
print(np.arange(10)) # 0 ~ 9 면 
arr4 = np.arange(10)+1 # 각각 원소에 +1  1 ~ 10되는 거
print(arr4)

print(arr4[:5])
print(arr4[-3:])

