from itertools import permutations
from random import shuffle
 
try:
    raw_input
except:
    raw_input = input
try:
    from itertools import izip
except:
    izip = zip
 
digits = '123456789'
size = 4
 
def parse_score(score):
    score = score.strip().split(',')
    return tuple(int(s.strip()) for s in score)
 
def scorecalc(guess, chosen):
    a, b = 0, 0
    for i in range(4):
        if guess[i] == ans[i]:
            a += 1
        elif guess[i] in ans:
            b += 1
    return a,b
 
choices = list(permutations(digits, size))
shuffle(choices)
answers = []
scores  = []
 
print ("Playing Bulls & Cows with %i unique digits\n" % size)
 
while True:
    ans = choices[0]
    answers.append(ans)
    #print ("(Narrowed to %i possibilities)" % len(choices))
    score = raw_input("Guess %2i is %*s. Answer (Bulls, cows)? "
                      % (len(answers), size, ''.join(ans)))
    score = parse_score(score)
    scores.append(score)
    #print("Bulls: %i, Cows: %i" % score)
    found =  score == (size, 0)
    if found:
        print ("Ye-haw!")
        break
    choices = [c for c in choices if scorecalc(c, ans) == score]
    if not choices:
        print ("Bad scoring? nothing fits those scores you gave:")
        print ('  ' +
               '\n  '.join("%s -> %s" % (''.join(an),sc)
                           for an,sc in izip(answers, scores)))
        break