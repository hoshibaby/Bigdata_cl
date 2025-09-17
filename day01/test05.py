def multi(v1, v2):
  result1 = v1 + v2
  result2 = v1 - v2
  return result1, result2


hap, sub = multi(100, 200)
# %d 숫자 " "" 안에는 변수를 못 넣으니까"
print("multi()에서 리턴된 값 ==> %d , %d" %(hap, sub))

