#cows and bulls
import random
play = 'Y'
while play=='Y':
    number = ''.join(random.sample('0123456789',4))
    #print(random.randint(1000,9999))
    #print(number)
    num_dict = {}
    guessed=0 #flag to check if the user ran out of chances without getting it right
    for i in range(0,4):
        a=number[i]
        num_dict[i+1] = a
    #print(num_dict)
    for j in range(10):
        cows=0
        bulls=0
        n = input('Enter your number:')
        n_dict={}
        for i in range(0,4):
            n_dict[i+1] = n[i]
        bull_items = {k:num_dict[k] for k in num_dict if k in n_dict and num_dict[k]==n_dict[k]}
        cow_items = {k:num_dict[k] for k in num_dict if num_dict[k] in n_dict.values() and num_dict[k]!=n_dict[k]}
        bulls=len(bull_items)
        cows=len(cow_items)
        print(bulls,' Bulls')
        print(cows,' Cows')
        if bulls==4 and cows==0:
            print('Congrats..You guessed it right. You took ',j+1,' turns to guess!')
            guessed=1
            break
    if guessed==0:
        print('The correct ans is: '+ number)
    print('Want to play again. Press Y to continue. Press any other key to exit.')
    play=input()
    
