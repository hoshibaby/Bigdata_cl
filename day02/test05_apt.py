import csv
import re

# apt_201910.csv 파일을 읽어, 천단위 제거한 후(가격 제거) float 형으로 반환하여 3개만 출력

f = open('day02\\apt_201910.csv', 'r')
reader = csv.reader(f)

output = []
for i in reader:
  output.append(i)

#천단위 제거
for i in output:
  for j in i:
    try:
      i[i.index(j)] = float(re.sub(',','',j))
    except:
      pass

print(output[:3])
print('길이 : ', len(output))

# 강원도에 120m2 이상 3억 이하 검색하기 시군구 단지명 가격 출력

new_list = [['시군구', '단지명', '가격']]
for i in output:

  try:
    if i[5] >= 120 and i[-4] <= 30000 and re.match('강원', i[0]):
      print([i[0], i[4], i[-4]])
      new_list.append([i[0], i[4], i[-4]])

  except:
    pass
print(new_list[:4])


#csv 이용해서 파일로 내어보내기 => apt.csv

with open('apt.csv', 'w', newline='', encoding = 'utf-8') as f:
  a = csv.writer(f)
  a.writerow(new_list)




