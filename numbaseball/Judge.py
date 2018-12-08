# Judge.py

class Judge:

   # 숫자 비교, 판정
    def judge(self, number, exp): # 주의 : obj는 Thinker 클래스의 객체이다.
        # 기록용 리스트 -  [스트라이크, 볼, 아웃]
        result = [0, 0, 0]

        for i in range(3):

            # 스트라이크 판정
            if number[i] == exp[i]:
                result[0] += 1

            # 볼 판정
            for j in range(3):
                if number[i] == exp[j]:
                    result[1] += 1

        # 아웃 판정
        if result[0] + result[1] == 0:
            result[2] = 1
        
        # 중복 제거
        result[1] -= result[0]

        return result