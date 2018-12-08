# NctrFuncs.py
import random as rnd

# 리스트에서 랜덤으로 숫자 추출
def pick(pool, leng=3): # 주의 : pool은 str 형의 숫자를 가지고 있으므로 이를 list형으로 변환해야함.
    result=[0 for _ in range(leng)]
    k=rnd.randrange(0, len(pool))
    for i in range(leng):
        result[i] = int(pool[k][i])
    return result
            