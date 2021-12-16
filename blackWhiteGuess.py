import random
def RPS():
    hand = int(random.randint(1,3))
    return(hand)
def subtract(x1, x2):
    return x1 - x2
def position():
    direction = ("上","下",'左','右')
    head = str(random.choice(direction))
    return(head)

def blackWhiteGuess(Bet):
    while True:
        print("=====歡迎來到你猜我猜黑白猜=====")
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
        Input=input("請輸入『數字』決定您的猜拳選擇：")
        if Input.isdecimal(): 
            numbers = int(Input)
            hand = RPS()
            direction = ("上","下",'左','右')
            if numbers == 1 :
                result1 = subtract(numbers,hand)
                result2 = abs(result1)
                if result2 == 1 :
                    print("電腦出石頭！")
                    print("輸了，請準備『防守』！四選一(上、下、左、右)")
                    IInput=input("請輸入『方位』決定您的閃躲選擇：")
                    pick = ["上","下","左","右"]
                    head = position()
                    if IInput in pick:
                            if IInput == head :
                                print("電腦手指%s！" %(head))
                                print("你輸了QQ！")
                                Bet = Bet - roundBet
                                print('你現在總賭金有',Bet,'元，再接再厲!!')#失敗扣賭金
                            else:
                                print("電腦手指%s！" %(head))
                                print("好險，躲過一劫！")
                    else:
                        print('您輸入的資料格式有誤!')
                elif result2 == 2 :
                    print("電腦出布！")
                    print("贏了，請準備『攻擊』！四選一(上、下、左、右)")
                    IInput=input("請輸入『方位』決定您的攻擊選擇：")
                    pick = ["上","下","左","右"]
                    head = position()
                    if IInput in pick:
                            if IInput == head :                            
                                print("電腦頭轉%s！" %(head))
                                print("恭喜你！你贏了！！")
                                Bet = Bet + roundBet
                                print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金                                
                            else:
                                print("電腦頭轉%s！" %(head))
                                print("唉，差一點！")
                    else:
                        print('您輸入的資料格式有誤!')
                else :
                    print("電腦出剪刀！")
                    print("可惜平手了，再來！")
                    continue
            elif numbers == 3 :
                result1 = subtract(numbers,hand)
                result2 = abs(result1)
                if result2 == 1 :
                    print("電腦出石頭！")
                    print("贏了，請準備『攻擊』！四選一(上、下、左、右)")
                    IInput=input("請輸入『方位』決定您的攻擊選擇：")
                    pick = ["上","下","左","右"]
                    head = position()
                    if IInput in pick:
                            if IInput == head :                           
                                print("電腦頭轉%s！" %(head))
                                print("恭喜你！你贏了！！")
                                Bet = Bet + roundBet
                                print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金   
                            else:
                                print("電腦頭轉%s！" %(head))
                                print("唉，差一點！")
                    else:
                        print('您輸入的資料格式有誤!')
                elif result2 == 2 :
                    print("電腦出剪刀！")
                    print("輸了，請準備『防守』！四選一(上、下、左、右)")
                    IInput=input("請輸入『方位』決定您的閃躲選擇：")
                    pick = ["上","下","左","右"]
                    head = position()
                    if IInput in pick:
                            if IInput == head :                            
                                print("電腦手指%s！" %(head))
                                print("你輸了QQ！")
                            else:
                                print("電腦手指%s！" %(head))
                                print("好險，躲過一劫！")
                    else:
                        print('您輸入的資料格式有誤!')
                else :
                    print("電腦出布！")
                    print("可惜平手了，再來！")
                    continue
            elif numbers == 2 :
                result1 = subtract(numbers,hand)
                result2 = int(result1)
                if result2 == 1 :
                    print("電腦出剪刀！")
                    print("贏了，請準備『攻擊』！四選一(上、下、左、右)")
                    IInput=input("請輸入『方位』決定您的攻擊選擇：")
                    pick = ["上","下","左","右"]
                    head = position()
                    if IInput in pick:
                            if IInput == head :                      
                                print("電腦頭轉%s！" %(head))
                                print("恭喜你！你贏了！！")
                                Bet = Bet + roundBet
                                print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金   
                            else:
                                print("電腦頭轉%s！" %(head))
                                print("唉，差一點！")
                    else:
                        print('您輸入的資料格式有誤!')
                elif result2 == -1 :
                    print("電腦出布！")
                    print("輸了，請準備『防守』！四選一(上、下、左、右)")
                    IInput=input("請輸入『方位』決定您的閃躲選擇：")
                    pick = ["上","下","左","右"]
                    head = position()
                    if IInput in pick:
                            if IInput == head :                     
                                print("電腦手指%s！" %(head))
                                print("你輸了QQ！")
                                Bet = Bet - roundBet
                                print('你現在總賭金有',Bet,'元，再接再厲!!')#失敗扣賭金
                            else:
                                print("電腦手指%s！" %(head))
                                print("好險，躲過一劫！")
                    else:
                        print('您輸入的資料格式有誤!')
                else :
                    print("電腦出石頭！")
                    print("可惜平手了，再來！")
                    continue
            else :
                print('您輸入的資料格式有誤!')
                continue

        elif Input == "Q" or Input == "q":
            print("歡迎您下次再度光臨！")
            break  
        else :
            print('您輸入的資料格式有誤!')
            continue
    return Bet
# blackWhiteGuess()