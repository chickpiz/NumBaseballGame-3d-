# GameMain.py
import Thinker
import Judge
import time

#TODO : 평균적으로 몇 턴만에 이기는지 확률 계산
def com_v_com(p1, p2, j):
    # 턴 진행 횟수
    tn_cnt = 0
    while True:
        tn_cnt += 1
        # p1 턴
        p1_s = p1.suggest()
        p1_r = j.judge(p2, p1_s)
        # p2 턴
        p2_s = p2.suggest()
        p2_r = j.judge(p1, p2_s)
        if p1_r == [3,0,0] or p2_r == [3,0,0]:
            p1.infer(p1_s, p1_r)
            p2.infer(p2_s, p2_r)
            print(str(tn_cnt)+': 1 - '+str(p1_s)+str(p1_r)+', 2 - '+str(p2_s)+str(p2_r))
            break
        else:
            p1.infer(p1_s, p1_r)
            p2.infer(p2_s, p2_r)
            print(str(tn_cnt)+': 1 - '+str(p1_s)+str(p1_r)+', 2 - '+str(p2_s)+str(p2_r))
    if p1_r == [3,0,0] and p2_r != [3,0,0]:
        print('1 won in : '+str(tn_cnt))
    elif p2_r == [3,0,0] and p1_r != [3,0,0]:
        print('2 won in : '+str(tn_cnt))
    else:
        print('draw in : '+str(tn_cnt))

def com_v_com_loop(p1, p2, j, numb):
    # 결과 기록
    p1_w, p2_w = 0, 0
    recorddate = time.strftime('%x', time.localtime(time.time()))
    recordtime = time.strftime('%X', time.localtime(time.time()))
    f = open('result_cvc_' + recorddate.replace('/', '-') + '_' + recordtime.replace(':', '-') +'.txt', 'a')
    for i in range(numb):
        print('<'+str(i+1)+'>')
        f.write('<'+str(i+1)+'>')
        f.write('\n')
        p1.__init__()
        p2.__init__()
        # 턴 진행 횟수
        tn_cnt = 0
        i = True
        while i == True:
            tn_cnt += 1
            # p1 턴
            p1_s = p1.suggest()
            p1_r = j.judge(p2, p1_s)
            # p2 턴
            p2_s = p2.suggest()
            p2_r = j.judge(p1, p2_s)
            if p1_r == [3,0,0] or p2_r == [3,0,0]:
                p1.infer(p1_s, p1_r)
                p2.infer(p2_s, p2_r)
                r1 = str(tn_cnt)+': 1 - '+str(p1_s)+str(p1_r)+', 2 - '+str(p2_s)+str(p2_r)
                print(r1)
                f.write(r1)
                f.write('\n')
                i = False
            else:
                p1.infer(p1_s, p1_r)
                p2.infer(p2_s, p2_r)
                r2 = str(tn_cnt)+': 1 - '+str(p1_s)+str(p1_r)+', 2 - '+str(p2_s)+str(p2_r)
                print(r2)
                f.write(r2)
                f.write('\n')
        if p1_r == [3,0,0] and p2_r != [3,0,0]:
            print('1 won in : '+str(tn_cnt))
            p1_w += 1
            f.write('1 won in : '+str(tn_cnt))
            f.write('\n')
        elif p2_r == [3,0,0] and p1_r != [3,0,0]:
            print('2 won in : '+str(tn_cnt))
            p2_w += 1
            f.write('2 won in : '+str(tn_cnt))
            f.write('\n')
        else:
            print('draw in : '+str(tn_cnt))
            f.write('draw in : '+str(tn_cnt))
            f.write('\n')
    f.write('com1 : '+str(p1_w)+', com2: '+str(p2_w))
    f.close()

def hum_v_com(com):
    pass
        
def main():
    while True:
        print('1. 컴퓨터 vs 컴퓨터 시뮬레이션 (1회)')
        print('2. 컴퓨터 vs 컴퓨터 시뮬레이션 (반복)')
        print('3. 컴퓨터와 대결하기')
        mode = input()
        if mode == '1':
            tk1, tk2 = Thinker.Thinker(), Thinker.Thinker()
            jud = Judge.Judge()
            com_v_com(tk1, tk2, jud)
        elif mode == '2':
            n = int(input('반복 횟수 : '))
            tk1, tk2 = Thinker.Thinker(), Thinker.Thinker()
            jud = Judge.Judge()
            com_v_com_loop(tk1, tk2, jud, n)
        elif mode == '3':
            com = Thinker.Thinker()
            hum_v_com(com)
        con = input('처음으로 돌아가시겠습니까? [예/아니오] : ')
        if con == '예' or con == 'ㅇ' or con == 'ㅇㅇ' or con == 'd':
            pass
        if con == '아니오' or con == '아니요' or con == '아뇨' or con == 'ㄴ' or con == 'ㄴㄴ' or con == 's':
            quit()

main()
