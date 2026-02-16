import random
n=random.randint(1,10)
guesses=0
while True:
    guess=int(input('1 dan 10gacha son kirit '))
    guesses+=1
    if n==guess:
        print('topding🎉')
        break
    else:
        print('xato')
    
    if guesses>=3:
        print('yutqazdingiz')
        break
        
