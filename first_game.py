'''
First Game 
date                             25-05-21
Rules of the game 
you pick one item from snake , gun , and water
Similarly 
computer pick one item from snake , gun , and water
1 i) If you pick snake and computer pick water You GET A POINT
 ii) If you pick gun and computer pick snake You GET A POINT 
iii) If you pick water and computer pick gun You GET A POINT 

2 i) If you pick snake and computer pick gun COMPUTER GET A POINT
 ii) If you pick gun and computer pick water COMPUTER GET A POINT 
iii) If you pick water and computer pick snake COMPUTER GET A POINT 

3 If you both pick same then no one get a points

'''

from random import choice
print("Welcome to 'Snake, Gun, Water' Game")
l=["Snake","Water","Gun"]
pc_count=human_count=0
n=int(input("How many times you want to play: "))
while n>0:
    print(f"*************************************Chances left: {n}")
    c=choice(l)
    a=input("Press 'S' for Snake \nPress 'G' for Gun \nPress 'W' for Water \n")
    if a in "sSGgWw":
        if (a in'sS' and c==l[2]) or (a in 'Gg' and c==l[1]) or (a in 'wW' and c==l[0]):
            pc_count+=1
            for i in range(len(l)):
                if a.capitalize()==l[i][0]:
                    print(f"You choose {l[i]} ------------ Computer choose {c} \n \t  ...You lose a point...")
        elif a.capitalize()==c[0]:
            n-=1
            print(f"You choose {c} ------------ Computer choose {c} \n \t  ^^^No-one gets a point^^^")
            continue
        else:
            human_count+=1
            for i in range(len(l)):
                if a.capitalize()==l[i][0]:
                    print(f"You choose {l[i]} ------------ Computer choose {c} \n \t  ***You win a point***")
        n-=1
    else:
        print('Your game is over_____You press the wrong key.....')
        break


if human_count>pc_count:
    print(f'Your final score: {human_count} ______________________ Computer final score: {pc_count}')
    print("********************** You Win **********************")
elif human_count==pc_count:
    print(f'Your final score: {human_count} ______________________ Computer final score: {pc_count}')
    print("^^^^^^^^^^^^^^^^^^^^^^^^ Tie ^^^^^^^^^^^^^^^^^^^^^^^^")
else:
    print(f"Your final score: {human_count} ______________________ Computer final score: {pc_count}")
    print("..................... You loose .....................")
