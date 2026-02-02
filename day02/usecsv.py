import csv
import re

#test06 파일에 import 시킨거야

#함수는 여러번 사용하기 위해서 만드는거야. 어떤 파일이든 읽어오면 되게
def opencsv(filename):
  f = open(filename, 'r')
  reader = csv.reader(f)
  output = []
  for i in reader:
    output.append(i)
  return output


#천단위 제거
def deletecoma(output):
  for i in output:
    for j in i:
      try:
        i[i.index(j)] = float(re.sub(',','',j))
      except:
        pass
  return output
