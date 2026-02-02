import csv, re
import usecsv

#usecsv라는 함수를 만들어서 소환 시킨거야

# 강원도에 120m2 이상 3억 이하 검색하기 시군구 단지명 가격 출력

output_result = usecsv.opencsv('day02\\apt_201910.csv')
output = usecsv.deletecoma(output_result)

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