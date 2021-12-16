from random import randint

def guessPassword(Bet):
    times = 0
    lowest=1
    highest=1000
    answer=randint(lowest, highest)

    print("=====歡迎來到終極密碼=====")
    while True:
            roundBet = int(input('請選擇這次的賭注:'))
            if (roundBet <= Bet):
                if(roundBet == Bet):print('豪氣萬千梭哈啦!!!')
                break
            print('你沒有這麼多賭金!!!!')
    print("請猜一個介於1~100之間的數字")

    while True:

        guess = input('密碼介於'+str(lowest)+'~'+str(highest)+'之間\n')

        if guess == "q" or guess == "Q":
            print("你已經離開遊戲囉～")
            break

        try:
            guess = int(guess) 
        except ValueError:
            print('格式錯誤，請輸入數字\n')
            continue

        if guess == answer:
            print('答對了!')
            if (times <= 20):
                Bet = Bet + roundBet
                print('你只花',times,'次就猜對了，恭喜你獲得獎金')
                print('你現在總賭金有',Bet,'元，真的是太厲害了!!')#獲勝加賭金
            else:
                Bet = Bet - roundBet
                print('你花了',times,'次才達成，小於20次即可獲得獎金')
                print('你現在總賭金有',Bet,'元，再接再厲下次一定更好!!')#獲勝扣賭金
            break
        elif guess < lowest or guess > highest:
            print('請輸入'+str(lowest)+'~'+str(highest)+'之間的整數\n')
            continue

        if guess < answer:
            lowest = guess
            times = times + 1    
        else:
            highest = guess
            times = times + 1
    return Bet        
# guessPassword()
