#PROJECT
import random
score=0
ans='y'
print('Choose the part you want to do \n 1. To learn the table of any number \n 2. Mathamatical calculation \n 3. Guess the word')
check=int(input('\nEnter the option:'))

while check<=4:
    if check==1:
        while ans=='y' or 'Y':
            number=int(input("\nEnter the number you want to get table of:"))
            print("The table is: \n ")
            for i in range(1, 11):
                print(number, 'x', i, '=', number*i)
            ans =input("Do you want to calculte another table ans in y or no:")
            if ans=='y':
                continue
            else:
                print('\nChoose the part you want to do \n 1. To learn the table of any number \n 2. Mathamatical calculation \n 3. Guess the word')
                check=int(input('\nEnter the option:'))
                break
                

    elif check==2:
        for i in range(6):
            if (i==5):
                print("score =" , score)
                print ("game over")
                print('choose the part you want to do \n 1. To learn the table of any number \n 2. Mathamatical calculation \n 3. Guess the word')
                check=int(input('\nEnter the option:'))
                break
            print("\n 1.+ \n 2.- \n 3.* \n 4. / \n 5. exit")
            operators=int(input("\nThe operation you want to do?\n"))
            a=random.randint(1,999)
            b=random.randint(1,999)
            print("First number:",a)
            print("Second number:",b)
            if operators==1:
                s=a+b
                sum=int(input("Enter your answer:"))
                if(s==sum):
                    score+=2
                    print("Answer is:",s)
                    print("Your score =" , score)
                else:
                    score=score
                    print("Answer is:",s)
                    print("Your score =" , score)
               
            elif operators==2:
                d=a-b
                diff=int(input("Enter your answer:"))
                if(d==diff):
                    score+=2
                    print("Answer is:",d)
                    print("Your score=",score)
                else:
                    score=score
                    print("Answer is:",d)
                    print("Your score=",score)
                
            elif operators==3:
                p=a*b
                prod=int(input("Enter your answer:"))
                if(p==prod):
                    score+=2
                    print("Answer is:",p)
                    print("Your score=",score)
                else:
                    score=score
                    print("Answer is:",p)
                    print("Your score=",score)
                
            elif operators==4:
                q=a/b
                quotient=float(input("Enter your answer:"))
                if(q==quotient):
                    score+=2
                    print("Answer is:",q)
                    print("Your score=",score)
                else:
                    score=score
                    print("Answer is:",q)
                    print("Your score=",score)
            else:
                print('\n\nchoose the part you want to do \n 1. To learn the table of any number \n 2. Mathamatical calculation \n 3. Guess the word')
                check=int(input('\nEnter the option:'))
               


    elif check==3:
        print("*"*2,"WELCOME TO THE GUESSING GAME","*"*2)
        ch=("paradise","cat","dog","alphabets","elephant","travel","cricket","summer","ballon","dinosaur","great")
        word=random.choice(ch)
        print("Here are the number of letters in the word:")
        n= ' '
        turns=10
        while turns>0:
            fail=0
            for i in word:
                if i in n:
                    print(i)
                else:
                    print("_")
                    fail+=1
            if fail==0:
                print("You Win the game!")
                print("The correct word is:",word)
                break
            j=input("Guess a character:")
            n+=j
            if j not in word:
                turns-=1
                print("That's a wrong choice")
                print("You have",turns,"more guesses")
                if turns==0:
                    print("You Loose!")
        print('\nChoose the part you want to do \n 1. To learn the table of any number \n 2. Mathamatical calculation \n 3. Guess the word')
        check=int(input('\nEnter the option:'))                

    elif check>=4:
        print("\nEnter the number between 1 to 3")
        print('\nChoose the part you want to do \n 1. To learn the table of any number \n 2. Mathamatical calculation \n 3. Guess the word')
        check=int(input('\nEnter the option:'))
        
