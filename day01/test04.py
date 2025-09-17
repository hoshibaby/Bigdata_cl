# 1. 구구단 출력 (2단 ~ 9단)
# 2단
# 2 * 1 = 2

for i in range (2, 10):
    print(i, '단')
    for j in range (1, 10):
        print(i, '*', j, '=', i*j )
    print()

# 2. mylist 에서 짝수만 출력

mylist = [3,5,4,9,2,8,2,1]

#1.
for i in mylist:
   if i % 2 == 0 :
     print(i, end= ' ')

#2.
lst=[]
for i in mylist:
   if i % 2 == 0 :
      lst.append(i) # 리스트에 저장을 했다가 맨 마지막에 한번만 출력

print('lst: ', lst)

#3. 2번을 간단하게 작성한 것(리스트 컴플리핸션)
lst3 = [i for i in mylist if i % 2 == 0 ] #for문을 돌려서 그때 해당되는 i값을 담겠다!!
print('\nlst3 : ', lst3)

# 19세 이상인 사람만 추출하여 리스트 adult 에 저장
# 위 3번 형식으로 구하기

people = [31, 53, 41, 19, 15, 18, 21, 13]

lst4=[]
for i in people:
   if i >= 19 :
      lst4.append(i)

print('adult: ', lst4)

adult = [i for i in people if i >= 19]
print('\nadult ', adult)


#5. 항목이 2인것만 추출하여, 리스트 newlist에 저장

mylist = [[1,2], [3,4,5], [6,7]]

newlist = [ i for i in mylist if len(i) ==2]
print('newlist: ', newlist)



