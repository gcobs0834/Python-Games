#21點
import random 
def blackJack(Bet):
    while True:
        c=input('要玩遊戲請按P，退出請按Q:').upper()
        if c=='P':
            #print(歡迎進入21點遊戲，規則...)
            print('歡迎進入21點遊戲，遊戲規則如下:\n如果拿到的牌是2~10，拿到的點數等於牌面數字\n如果拿到的牌等於J,Q,K，拿到的點數等於10點\n如果拿到的牌等於A，拿到的點數等於1點\n每個玩家拿到的牌最多只能有五張，最後累加點數越接近21點的就是贏家。\n'+'-'*60)
            #用while迴圈隨機發牌牌給玩家(按hit)跟莊家(點數小於21)
            l=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
            #紀錄玩家的累積點數
            points=0
            #紀錄莊家累積點數
            bpoints=0
            #記錄發牌次數
            n=0

            #
            #下賭注
            while True:
                roundBet = int(input('請選擇這次的賭注:'))
                if (roundBet <= Bet):
                    if(roundBet == Bet):print('豪氣萬千梭哈啦!!!')
                    break
                print('你沒有這麼多賭金!!!!')
            #
            #


            while True:
                if points<=21:
                    a=input('輸入hit發牌，輸入stop停止發牌: ').lower()
                    if a=='hit' and n<5:
                        card=random.choice(l)
                        n+=1
                        if card=='A':
                            points+=1
                        elif card=='2':
                            points+=2
                        elif card=='3':
                            points+=3
                        elif card=='4':
                            points+=4
                        elif card=='5':
                            points+=5
                        elif card=='6':
                            points+=6
                        elif card=='7':
                            points+=7
                        elif card=='8':
                            points+=8
                        elif card=='9':
                            points+=9
                        elif card=='10':
                            points+=10
                        elif card=='J':
                            points+=10
                        elif card=='Q':
                            points+=10
                        elif card=='K':
                            points+=10
                        else:
                            card+=0
                        print('你拿到的牌是:',card,'目前的累積點數為:',points,'，一共有',n,'張牌')
                        
                    elif a=='stop':
                        print('你目前的累積點數為:',points,'，一共有',n,'張牌')
                        break
                    elif a=='hit' and n>=5:
                        print('你已經拿到五張牌了，不能再發了')
                        break
                    else:
                        print('輸入錯誤，請再輸入一次')
                else :
                    print('已經超過21點嘍!')
                    break 
            k=0   
            for j in range(random.randint(1,6)):
                if bpoints<21:
                    bcard=random.choice(l)
                    k+=1
                    if bcard=='A':
                        bpoints+=1
                    elif bcard=='2':
                        bpoints+=2
                    elif bcard=='3':
                        bpoints+=3
                    elif bcard=='4':
                        bpoints+=4
                    elif bcard=='5':
                        bpoints+=5
                    elif bcard=='6':
                        bpoints+=6
                    elif bcard=='7':
                        bpoints+=7
                    elif bcard=='8':
                        bpoints+=8
                    elif bcard=='9':
                        bpoints+=9
                    elif bcard=='10':
                        bpoints+=10
                    elif bcard=='J':
                        bpoints+=10
                    elif bcard=='Q':
                        bpoints+=10
                    elif bcard=='K':
                        bpoints+=10
                    else:
                        bpoints+=0
                else:
                    break
            print('莊家有',bpoints,'點','，一共有',k,'張牌')
            if points>bpoints and points<=21 and bpoints<21:
                print('你贏了!!!')
                Bet = Bet + roundBet
                print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金           
            elif points<bpoints and bpoints<=21 and points<21:
                print('莊家贏了，你輸了:(')
                Bet = Bet - roundBet
                print('你現在總賭金有',Bet,'元，再接再厲!!')#失敗扣賭金
            elif points>21 and bpoints<=21:
                print('你爆掉了，莊家贏了!')
                Bet = Bet - roundBet
                print('你現在總賭金有',Bet,'元，再接再厲!!')#失敗扣賭金
            elif bpoints>21 and points<=21:
                print('莊家爆掉了，你贏了!')
                Bet = Bet + roundBet
                print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金
            elif bpoints>21 and points>21:
                print('你們都爆掉了，本回合平手，再玩一次吧!')
            elif bpoints==points:
                print('點數相同，本回合平手，再玩一次吧!')
        elif c=='Q':
            print('結束遊戲!')
            break
        else:
            print('輸入不正確，請再輸入一次!')
    return(Bet)
# blackJack()