import csv
import re
# 파일을 읽어 리스트 반환
def opencsv(filename):
  output = []
  f = open(filename,'r')
  reader = csv.reader(f)
  for i in reader:
    output.append(i)
  # print(output)
  return output


result  = opencsv('day02\\popSeoul2.csv')

# 5개만 출력
for i in result[:5]:
  print(i)

# 5개만 천단위 , 제거 후  float으로 변환하여 출력

for i in result[:5]:
  for j in i:
    # print(i[i.index(j)])  i.index(j)==>위치값
    try:
      i[i.index(j)]= float(re.sub(',','',j))
    except:
        pass  

print(result[:5])