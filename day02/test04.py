#파일 열기
with open('day02\\singer1.csv', 'r') as inFp:
#파일로 내보내기
  with open('day02\\singer1_out.csv', 'w', encoding = 'utf-8') as outFp:

    header = inFp.readline() # 한줄 읽어오는 리드라인 헤더에 담아 title에 공백 제거
    #print(header)
    header = header.strip() # 공백제거
    header_list = header.split(',')
    height_idx = header_list.index('평균 키')
    name_idx = header_list.index('이름')

  # print(header_list) # 리스트에 담겨서 출력

    

    for data in header_list:
      print(data, end='\t') # 탭만큼 띄운다.

  # 키가 165 이상인 사람 이름 출력 -> 파일로 내보내기 => singer1_out.csv


    output = []
    for data in inFp: #타이틀를 이미 readline 했으므로 내용 출력   
      #print(data) # 내용 출력
        dataStr = data.strip() # 공백제거
        row_list = data.split(',')
        if int(row_list[height_idx]) >= 165:
          # print(row_list[name_idx], row_list[height_idx])
          output.append([row_list[name_idx], row_list[height_idx]])

    print(output)

#리스트를 문자열로 변환
    row_str = ','.join(map(str,output))
    outFp.write(row_str)




