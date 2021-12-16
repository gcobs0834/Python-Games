#划酒拳

import random

def yourselection():
    selection=(0,5,10)
    ten=int(random.choice(selection))
    return(ten)
def pss():
    hand= int(random.randint(1,3))
    return(hand)
def computerselection():
    ssum=(0,5,10,15,20)
    ssumm=int(random.choice(ssum))
    return(ssumm)


def drinkingGame(Bet):
    pick = [0,5,10]
    pick2 = [0,5,10,15,20]
    
    while True:
        print("=====歡迎來到划酒拳=====")
        prompt = input('要離開請按Q').upper()
        if prompt == 'Q': break
        #賭金系統
        while True:
            roundBet = int(input('請選擇這次的賭注:'))
            if (roundBet <= Bet):
                if(roundBet == Bet):print('豪氣萬千梭哈啦!!!')
                break
            print('你沒有這麼多賭金!!!!')
        
        print("規則說明：猜拳決定攻守，1:剪刀、2:石頭、3:布（若要跳出請按Q）")
        player = input("請輸入『數字』決定您的猜拳選擇：")
        hand = pss()

        if player == "Q" or player== "q":
            print("歡迎您下次再度光臨！")
            break 
        
        try:
            player = int(player) 
        except ValueError:
            print('您輸入的資料格式有誤!')
            continue
              
        if player == 1 and hand == 3 :
            print("你出剪刀！")
            print("電腦出布！")
            print("贏了，請準備『攻擊』！三選一(0、5、10)")
            IInput = int(input("請輸入您的出選擇："))
            ohh = int(input("請輸入你要喊的總和(0,5,10,15,20):"))
            pick = [0,5,10]
            ten= yourselection()
            if IInput in pick and ohh in pick2:
                if IInput+ten == ohh:
                    ans = IInput+ten
                    print("總和是%s" %(ans))
                    print("贏了！")
                    Bet = Bet + roundBet
                    print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金 

                else:
                    ans = IInput+ten
                    print("總和是%s！" %(ans))
                    print("電腦躲過一劫！")

            else:
                print('您輸入的資料格式有誤!') 


        elif player== 2 and hand== 1 :
            print("你出石頭！")
            print("電腦出剪刀！")
            print("贏了，請準備『攻擊』！三選一(0、5、10)")
            IInput = int(input("請輸入您的出選擇："))
            ohh = int(input("請輸入你要喊的總和(0,5,10,15,20):"))
            pick = [0,5,10]
            ten= yourselection()
            if IInput in pick and ohh in pick2:
                if IInput+ten == ohh:
                    ans = IInput+ten
                    print("總和是%s" %(ans))
                    print("贏了！")
                    Bet = Bet + roundBet
                    print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金 
                else:
                    ans = IInput+ten
                    print("總和是%s！" %(ans))
                    print("電腦躲過一劫！")

            else:
                 print('您輸入的資料格式有誤!') 

        elif player== 3 and hand== 2 :
            print("你出布！")
            print("電腦出石頭！")
            print("贏了，請準備『攻擊』！三選一(0、5、10)")
            IInput = int(input("請輸入您的出選擇："))
            ohh = int(input("請輸入你要喊的總和(0,5,10,15,20):"))
            pick = [0,5,10]
            ten= yourselection()
            if IInput in pick and ohh in pick2:
                if IInput + ten == ohh:
                    ans = IInput+ten
                    print("總和是%s" %(ans))
                    print("贏了！")
                    Bet = Bet + roundBet
                    print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金 
                else:
                    ans = IInput+ten
                    print("總和是%s！" %(ans))
                    print("電腦躲過一劫！")
            else:
                 print('您輸入的資料格式有誤!') 
                    
        elif player== 3 and hand== 1:
            print("你出布！")
            print("電腦出剪刀！")
            print("輸了，請準備『防守』！三選一(0、5、10)")
            IInput = int(input("請輸入您的出選擇："))
            pick = [0,5,10]
            ssumm = computerselection()
            ten = yourselection()
            if IInput in pick:
                if IInput + ten == ssumm:
                    print("總和是％s" %(IInput+ten))
                    print("哇你輸了！")
                    Bet = Bet - roundBet
                    print('你現在總賭金有',Bet,'元，再接再厲!!')#失敗扣賭金
                else:
                    print("總和是%s！" %(IInput+ten))
                    print("你躲過一劫了！")
            else:
                 print('您輸入的資料格式有誤!') 

        elif player== 2 and hand== 3:
            print("你出石頭！")
            print("電腦出布！")
            print("輸了，請準備『防守』！三選一(0、5、10)")
            IInput = int(input("請輸入您的出選擇："))
            pick = [0,5,10]
            ssumm=computerselection()
            ten= yourselection()
            if IInput in pick:
                if IInput+ ten == ssumm:
                    ans = IInput+ten
                    print("總和是％s" %(ans))
                    print("哇你輸了！")
                    Bet = Bet - roundBet
                    print('你現在總賭金有',Bet,'元，再接再厲!!')#失敗扣賭金
                else:
                    ans = IInput+ten
                    print("總和是%s！" %(ans))
                    print("你躲過一劫了！")
            else:
                 print('您輸入的資料格式有誤!') 
        elif player == 1 and hand == 2:
            print("你出剪刀！")
            print("電腦出石頭！")
            print("輸了，請準備『防守』！三選一(0、5、10)")
            IInput = int(input("請輸入您的出選擇："))
            pick = [0,5,10]
            ssumm=computerselection()
            ten= yourselection()
            if IInput in pick:
                if IInput+ten == ssumm:
                    ans = IInput+ten
                    print("總和是％s" %(ans))
                    print("哇你輸了！")
                    Bet = Bet - roundBet
                    print('你現在總賭金有',Bet,'元，再接再厲!!')#失敗扣賭金
                else:
                    ans = IInput+ten
                    print("總和是%s！" %(ans))
                    print("你躲過一劫了！")   


            else:
                print('您輸入的資料格式有誤!') 
        elif player == hand:
            print("平手再來一次~~")
            continue
        else:
            print('您輸入的資料有誤!請重新輸入')
    return Bet
# drinkingGame()