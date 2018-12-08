# GameMain.py
import Thinker
import Judge

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
        

def main():
    tk1, tk2 = Thinker.Thinker(), Thinker.Thinker()
    jud = Judge.Judge()
    com_v_com(tk1, tk2, jud)

main()
