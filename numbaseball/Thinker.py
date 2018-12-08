# Thinker.py
import random as rnd
import NctrFuncs as nctr

class Thinker:
    def __init__(self):
        # 숫자 풀 : 경우의 수를 추려나가는 데 사용
        self.num_pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 숫자 집합(상대방의 경우의 수)
        self.poss_nums = []

        res_set = set()

        for i in self.num_pool:
            for j in self.num_pool:
                if j!=i:
                    for k in self.num_pool:
                        if k!=i and k!=j:
                            result = '%d%d%d' % (i, j, k)
                            res_set.add(result)
        self.history=[]
        self.update_nums(res_set)
        self.number = nctr.pick(self.poss_nums)

    # poss_nums 업데이트용
    def update_nums(self, new):
        res = new - set(self.history)
        self.poss_nums = list(res) 

    # poss_nums 추려나가기
    def infer(self, num, res):
        # 결과
        result = [0, 0, 0]
        res_set = set()
        
        # 아웃
        if res[2] == 1:
            for i in num:
                try:
                    self.num_pool.remove(i)
                except ValueError:
                    continue

            for i in self.num_pool:
                for j in self.num_pool:
                    if j != i:
                        for k in self.num_pool:
                            if k != i and k != j:
                                result = '%d%d%d' % (i, j, k)
                                res_set.add(result)
        else:
            # 0스트리아크
            if res[0] == 0:
                # 1볼
                if res[1] == 1:
                    # 1 -> 2
                    result[1] = str(num[0])
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j != i and j not in num:
                                    result[0] = str(i)
                                    result[2] = str(j)
                                    res_set.add(result[0] + result[1] + result[2])
                    # 1 -> 3
                    result[2] = str(num[0])
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j != i and j not in num:
                                    result[0] = str(i)
                                    result[1] = str(j)
                                    res_set.add(result[0] + result[1] + result[2])
                    # 2 -> 1
                    result[0] = str(num[1])
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j != i and j not in num:
                                    result[1] = str(i)
                                    result[2] = str(j)
                                    res_set.add(result[0] + result[1] + result[2])
                    # 2 -> 3
                    result[2] = str(num[1])
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j != i and j not in num:
                                    result[0] = str(i)
                                    result[1] = str(j)
                                    res_set.add(result[0] + result[1] + result[2])
                    # 3 -> 1
                    result[0] = str(num[2])
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j != i and j not in num:
                                    result[1] = str(i)
                                    result[2] = str(j)
                                    res_set.add(result[0] + result[1] + result[2])
                    # 3 -> 2
                    result[1] = str(num[2])
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j != i and j not in num:
                                    result[0] = str(i)
                                    result[2] = str(j)
                                    res_set.add(result[0] + result[1] + result[2])
                # 2볼
                elif res[1] == 2:

                    # 1번째 숫자가 아닐 경우
                    result[1] = str(num[2]); result[2] = str(num[1])
                    for i in self.num_pool:
                        if i not in num:
                            result[0] = str(i)
                            res_set.add(result[0] + result[1] + result[2])

                    # 2번째 숫자가 아닐 경우
                    result[0] = str(num[2]); result[2] = str(num[0])
                    for i in self.num_pool:
                        if i not in num:
                            result[1] = str(i)
                            res_set.add(result[0] + result[1] + result[2])

                    # 3번째 숫자가 아닐 경우
                    result[1] = str(num[0]); result[0] = str(num[1])
                    for i in self.num_pool:
                        if i not in num:
                            result[2] = str(i)
                            res_set.add(result[0] + result[1] + result[2])

                # 3볼
                elif res[1] == 3:
                    for i in num:
                        for j in num:
                            if j != i:
                                for k in num:
                                    if k != i and k != j:
                                        result = [i, j, k]
                                        if  result[0]!=num[0] and result[1]!=num[1] and result[2]!=num[2]:
                                            res_set.add(str(result[0])+str(result[1])+str(result[2]))

            # 1스트라이크
            elif res[0] == 1:
                # 0볼
                if res[1] == 0:
                    # 1번
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j!=i and j not in num:
                                    result = '%d%d%d' % (num[0], i, j)
                                    res_set.add(result)
                    # 2번
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j!=i and j not in num:
                                    result = '%d%d%d' % (i, num[1], j)
                                    res_set.add(result)
                    # 3번
                    for i in self.num_pool:
                        if i not in num:
                            for j in self.num_pool:
                                if j!=i and j not in num:
                                    result = '%d%d%d' % (i, j, num[2])
                                    res_set.add(result)
                # 1볼
                elif res[1] == 1:
                    # 1, 2
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (num[0], i, num[1])
                            res_set.add(result)
                    # 1, 3
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (num[0], num[2], i)
                            res_set.add(result)
                    # 2, 1
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (i, num[1], num[0])
                            res_set.add(result)
                    # 2, 3
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (num[2], num[1], i)
                            res_set.add(result)
                    # 3, 1
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (i, num[0], num[2])
                            res_set.add(result)
                    # 3, 2
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (num[1], i, num[2])
                            res_set.add(result)
                # 2볼
                elif res[1] == 2:
                    # 1
                    result = '%d%d%d' % (num[0], num[2], num[1])
                    res_set.add(result)
                    # 2
                    result = '%d%d%d' % (num[2], num[1], num[0])
                    res_set.add(result)
                    # 3
                    result = '%d%d%d' % (num[1], num[0], num[2])
                    res_set.add(result)
            # 2스트라이크
            elif res[0] == 2:
                if res[1] == 0:
                    # 1
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (num[0], num[1], i)
                            res_set.add(result)
                    # 2
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (i, num[1], num[2])
                            res_set.add(result)
                    # 3
                    for i in self.num_pool:
                        if i not in num:
                            result = '%d%d%d' % (num[0], i, num[2])
                            res_set.add(result)

            # 3스트라이크
            elif res[0] == 3:
                res_set.add('%d%d%d' % (num[0], num[1], num[2]))

        self.update_nums(res_set)

    # 숫자 제시
    def suggest(self):
        s = nctr.pick(self.poss_nums)
        self.history.append('%d%d%d' % (s[0], s[1], s[2]))
        return s

    