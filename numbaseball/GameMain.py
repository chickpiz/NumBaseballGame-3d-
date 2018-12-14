# GameMain.py
import Thinker
import Judge
import NctrFuncs as nctr
import time

def com_v_com(p1, p2, j):
    # 턴 진행 횟수
    tn_cnt = 0
    while True:
        tn_cnt += 1
        # p1 턴
        p1_s = p1.suggest()
        p1_r = j.judge(p2.number, p1_s)
        # p2 턴
        p2_s = p2.suggest()
        p2_r = j.judge(p1.number, p2_s)
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
    avr_cnt = 0
    contents = ''
    recorddate = time.strftime('%x', time.localtime(time.time()))
    recordtime = time.strftime('%X', time.localtime(time.time()))
    f = open('result_cvc_' + recorddate.replace('/', '-') + '_' + recordtime.replace(':', '-') +'.txt', 'a')
    for i in range(numb):
        contents += '<'+str(i+1)+'>\n'
        p1.__init__()
        p2.__init__()
        # 턴 진행 횟수
        tn_cnt = 0
        i = True
        while i == True:
            tn_cnt += 1
            # p1 턴
            p1_s = p1.suggest()
            p1_r = j.judge(p2.number, p1_s)
            # p2 턴
            p2_s = p2.suggest()
            p2_r = j.judge(p1.number, p2_s)
            if p1_r == [3,0,0] or p2_r == [3,0,0]:
                p1.infer(p1_s, p1_r)
                p2.infer(p2_s, p2_r)
                contents += str(tn_cnt)+': 1 - '+str(p1_s)+str(p1_r)+', 2 - '+str(p2_s)+str(p2_r)+'\n'
                i = False
            else:
                p1.infer(p1_s, p1_r)
                p2.infer(p2_s, p2_r)
                contents += str(tn_cnt)+': 1 - '+str(p1_s)+str(p1_r)+', 2 - '+str(p2_s)+str(p2_r)+'\n'
        if p1_r == [3,0,0] and p2_r != [3,0,0]:
            contents += '1 won in : '+str(tn_cnt)+'\n'
            p1_w += 1
            avr_cnt += tn_cnt
        elif p2_r == [3,0,0] and p1_r != [3,0,0]:
            contents += '2 won in : '+str(tn_cnt)+'\n'
            p2_w += 1
            avr_cnt += tn_cnt
        else:
            contents += 'draw in : '+str(tn_cnt)+'\n'
            avr_cnt += tn_cnt
    avr_cnt /= numb
    contents += 'com1 : '+str(p1_w)+', com2 : '+str(p2_w)+', draw : '+str(numb - p1_w - p2_w)+'\naverage : '+str(avr_cnt)
    f.write(contents)
    f.close()

def hum_v_com(com, jud):
    # 숫자 입력받기
    while True:
        pnum_ = input('숫자를 입력하세요. :')
        if len(pnum_) != 3 or type(pnum_) is not str:
            print('세 자리 숫자만 입력해주세요.')
            continue
        break
    pnum = nctr.toList(pnum_)
    input('당신의 숫자는 '+str(pnum[0])+str(pnum[1])+str(pnum[2])+' 입니다. 엔터를 누르면 게임이 시작됩니다.')
    # 시작
    tn_cnt = 0
    while True:
        tn_cnt += 1
        print('[Round '+str(tn_cnt)+']')
        while True:
            p_s_ = input('숫자 제시 : ')
            if len(p_s_) != 3 or type(p_s_) is not str:
                print('세 자리 숫자만 입력해주세요.')
                continue
            p_s = nctr.toList(p_s_)
            break
        p_r = jud.judge(com.number, p_s)
        print('결과 : '+str(p_r[0])+' s, '+str(p_r[1])+' b, '+str(p_r[2])+' out')
        input('엔터를 눌러 계속 진행...')
        print('<컴퓨터의 차례>')
        c_s = com.suggest()
        c_r = jud.judge(pnum, c_s)
        com.infer(c_s, c_r)
        time.sleep(1)
        print('컴퓨터가 제시한 숫자 : '+str(c_s[0])+str(c_s[1])+str(c_s[2]))
        time.sleep(1.1)
        print('결과 : '+str(c_r[0])+' s, '+str(c_r[1])+' b, '+str(c_r[2])+' out')
        input('엔터를 눌러 계속 진행...')
        if p_r == [3,0,0] or c_r == [3,0,0]:
            break
    if p_r == [3,0,0] and c_r != [3,0,0]:
        print('승리하셨습니다! 라운드 진행 횟수 : '+str(tn_cnt))
    elif p_r != [3,0,0] and c_r == [3,0,0]:
        print('패배하셨습니다. 라운드 진행 횟수 : '+str(tn_cnt))
    else:
        print('비기셨습니다.')
        
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
            jud = Judge.Judge()
            hum_v_com(com, jud)
        con = input('처음으로 돌아가시겠습니까? [예/아니오] : ')
        if con == '예' or con == 'ㅇ' or con == 'ㅇㅇ' or con == 'd':
            pass
        elif con == '아니오' or con == '아니요' or con == '아뇨' or con == 'ㄴ' or con == 'ㄴㄴ' or con == 's':
            quit()

main()
