from builtins import print

import pandas as pd

# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2021-06-07', 3.14, 'ABC', 100, True]

sr = pd.Series(list_data)

print(sr)

# index 배열은 변수 idx에 저장, value 배열은 변수 val에 저장
idx = sr.index
val = sr.values

print("idx >> ", idx)
print("val >> ", val)

# tuple을 Series로 변환
tup_data = ('영인', '2021-06-07', '여', True)
tup_to_sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])

print(tup_to_sr)

print(tup_to_sr[0]) #영인
print(tup_to_sr['이름']) #영인

print(tup_to_sr[[1, 2]], tup_to_sr[['생년월일', '성별']], sep="\n")
