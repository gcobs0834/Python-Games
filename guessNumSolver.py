from itertools import permutations
from random import shuffle
 
try:
    raw_input
except:
    raw_input = input

digits = '0123456789'
size = 4

def parse_score(score):
    score = score.strip().split(',')
    return tuple(int(s.strip()) for s in score)

def scorecalc(guess, ans):
    a, b = 0, 0
    for i in range(size):
        if guess[i] == ans[i]:
            a += 1
        elif guess[i] in ans:
            b += 1
    return a,b
 
choices = list(permutations(digits, size))
shuffle(choices)
answers = []
scores  = []
# [(1,2)]
 
print ("猜數字遊戲共有{}個不重複的數字".format(size))
 
while True:
    ans = choices[0]
    answers.append(ans)
    print ("(剩下{}組)".format(len(choices)))
    score = raw_input("第{}次: 是{}嗎? 幾a幾b? ".format(len(answers), ''.join(ans)))
    score = parse_score(score)
    scores.append(score)
    print("{} A, {} B".format(score[0], score[1]))
    found =  score == (size, 0)
    if found:
        print ("恭喜!")
        break
    choices = [c for c in choices if (scorecalc(c, ans) == score)]
    if not choices:
        print ("你確定這幾組都不是你的答案嗎? ")
        print ('  ' +
               '\n  '.join("{}->{}".format(''.join(an),sc)
                           for an,sc in zip(answers, scores)))
        break

