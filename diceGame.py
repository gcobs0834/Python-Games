#骰子賭博遊戲

import random

def diceGame(Bet):
    totalMoney = Bet
    print("本金為:" + str(totalMoney))
    while totalMoney > 0:
        print("=====遊戲開始=====")
        yourMoney = input("請輸入賭金（若要跳出請按Q）：")
        if yourMoney == "Q" or yourMoney == "q":
            print("你現在的本金為：" + str(totalMoney))
            break
        elif yourMoney.isdecimal():
            if int(yourMoney) > totalMoney:
                print("心太大囉！請重新輸入")
                print("你現在的本金為：" + str(totalMoney))
            else:
                dice = rollDice()
                sumDice = sum(dice)
                myPick = input("請問要猜大還是猜小（輸入”大“或“小”）：")
                pick = ["大", "小"]
                if myPick in pick:
                    if myPick == result(sumDice):
                        totalMoney += int(yourMoney)
                        print("你猜對囉！ 骰子點數為：" + str(dice) + " 骰子總和為：" + str(sumDice))
                        print("剩下本金為：" + str(totalMoney))
                    else:
                        totalMoney -= int(yourMoney)
                        print("你猜錯囉！ 骰子點數為：" + str(dice) + " 骰子總和為：" + str(sumDice))
                        print("剩下本金為：" + str(totalMoney))
                else:
                    print("格式錯誤，請重新輸入") 
                    print("你現在的本金為：" + str(totalMoney))
                
        else:
            print("格式錯誤，請重新輸入") 
            print("你現在的本金為：" + str(totalMoney))
        return totalMoney
#丟三顆骰子    
def rollDice():
    dice = []
    for i in range(3):
        point = random.randint(1,6)
        dice.append(point)
    return(dice)

#比大小
def result(sumPoint):
    if 3 <= sumPoint <= 10:
        return("小")
    elif 11<= sumPoint <=18:
        return("大")
    
# diceGame()