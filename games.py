import blackJack #21點
import blackWhiteGuess #黑白猜
import diceGame #骰子賭博遊戲
import guessNumGame #幾A幾B 猜數字
import guessPassword #終極密碼
import drinkingGame #划酒拳(五、十、十五、二十)

Bet = 0

def gameStart():

    while True:
        Bet = input('請輸入您的賭注: ')
        try:
            Bet = int(Bet)
        except ValueError:
            print("請輸入整數")
            continue
        if (Bet > 0 and Bet < 9999999999):
            break
        print('請輸入0~9999999999之間')
        
    
    while True:
        print("-----歡迎來到長青遊樂園-----")
        if (Bet == 0):
            print('哀呀啊您吃土了呢，下次再見摟')
            break
        print('您目前的賭注為',Bet,'元')
        print("0:21點")
        print("1:黑白猜")
        print("2:骰子賭博遊戲")
        print("3:幾A幾B猜數字")
        print("4:終極密碼")
        print("5:划酒拳(五、十、十五、二十)")
        gameNum = input("請選擇想要玩的遊戲之對應號碼(跳出遊戲請按Q)")

        if gameNum == "q" or gameNum == "Q":
            print("謝謝光臨，請下次再來")
            break
        
        else:

            try:
                gameNum = int(gameNum)
            except ValueError:
                print("查無此項，請重新輸入")
                continue
            if gameNum == 0:
                Bet = blackJack.blackJack(Bet)
            elif gameNum == 1:
                Bet = blackWhiteGuess.blackWhiteGuess(Bet)
            elif gameNum == 2:
                Bet = diceGame.diceGame(Bet)
            elif gameNum == 3:
                Bet = guessNumGame.guessNumGame(Bet)
            elif gameNum == 4:
                Bet = guessPassword.guessPassword(Bet)
            elif gameNum == 5:
                Bet = drinkingGame.drinkingGame(Bet)
            else:
                print("查無此項，請重新輸入")


gameStart()
