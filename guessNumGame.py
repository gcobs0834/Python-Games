#猜數字遊戲

import random

#選四位數字 數字不可重複
def pickNum():
    digit = ('0123456789')
    ans = "".join(random.sample(digit, 4))
    return ans

#計數器
def timer(times):
    times += 1
    return times

#比對數字
def comparison(guess, ans):
    a, b = 0, 0
    for i in range(4):
        if guess[i] == ans[i]:
            a += 1
        elif guess[i] in ans:
            b += 1
    return (a,b)
    
#猜數字遊戲
def guessNumGame(Bet):
    ans = pickNum()
    times = 0
    print("=====歡迎來到猜數字遊戲=====")
    print('在這裡，下了賭注後在20次內猜對即可獲得獎金!')
    while True:
        roundBet = int(input('請選擇這次的賭注:'))
        if (roundBet <= Bet):
            if(roundBet == Bet):print('豪氣萬千梭哈啦!!!')
            break
        print('你沒有這麼多賭金!!!!')
    print("每猜一個數，會根據這個數字給出幾A幾B")
    print("其中A前面的數字表示位置正確的數的個數")
    print("而B前的數字表示數字正確而位置不對的數的個數")
    while True:
        guess = input("請輸入四位不重複的數字(輸入Q放棄遊戲)")
        if len(guess) == 4 and guess.isdecimal():
            (a, b) = comparison(guess, ans)
            times = timer(times)
            print("第" + str(times) + "次")
            print("你猜的數字為：" + str(guess) + " " + str(a) + "A" + str(b) + "B")
            if guess == ans:
                print("你猜對了！答案為：" + str(ans))
                if (times <= 20):
                    Bet = Bet + roundBet
                    print('你只花',times,'次就猜對了，恭喜你獲得獎金')
                    print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金
                else:
                    Bet = Bet - roundBet
                    print('你花了',times,'次才達成，小於20次即可獲得獎金')
                    print('你現在總賭金有',Bet,'元，再接再厲下次一定更好!!')#獲勝扣賭金 
                break
        elif guess == "Q" or guess == "q":
            print("好可惜！你已放棄遊戲！")
            break
        else:
            print("輸入錯誤，請重新輸入")  
    return Bet
# guessNumGame()
