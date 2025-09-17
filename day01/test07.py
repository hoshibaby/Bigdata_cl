import codecs
import re

f = codecs.open('day01\\friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
#BIGDATA 폴더가 루트파일임
print(script101[:100])

print('=============================')

#Monica 출력하기

monica = re.findall(r'Monica:.+', script101 ) #.은 \n은 제외한 문자
print(monica[:3]) # 대사 3개
print('type monica :' , type(monica)) #list형태

print('=============================')

#All: 대사 출력
all = re.findall(r'All:.+', script101)
print(all)

print('=============================')

# All의 마지막 대사
print(all[-1])
print(len(all))
print('=============================')

#출연진 만 출력
# actor = refindall(r=[A-Z][a-z]+:', script101)
#print(actor)

patten = re.compile(r'[A-Z][a-z]+:')
actor = re.findall(patten, script101)
print(actor)

print('=============================')
actor_set = set(actor)
print(actor_set) #중복없이 출연진만 출력

# : 빼고 출연진만 출력

print('=============================')
actor_set = set(actor)
print(actor_set) #중복없이 출연진만 출력

# : 빼기

#character = []
#for i in actor_set:
#  ch = i.remove(":") #빼기 remove는 리스트가 아니라서 문자열이라서 못 쓴데
 # character.append(ch)

#print('출연진 : ', character )

print('=============================')

character = []
for i in actor_set: #i 는 문자열
  ch = re.sub(":", '', i)
  character.append(ch)
character.sort() #sort는 정렬
print('출연진 : ', character)

print('=============================')

character2 = []
for i in actor_set: #i 는 문자열
    character2 += [i[:-1]] # 끝에 맨 마지막을 빼자 -> 근데 단어단어로 나와, 리스트로 싸줘야해
character2.sort() #sort는 정렬
print('출연진2 : ', character2)