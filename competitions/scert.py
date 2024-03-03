#SCERT Project

def quiz():
    import sys
    import mysql.connector
    import random
    mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="quiz")
    mycursor=mydb.cursor()
    def Home():
        print('\n\n')
        f=1
        while f!=3:
            print("Welcome to Quiz")
            print("********************")
            print("1. Enter Questions")
            print("2. Take Quiz")
            print("3. Exit")
            f=int(input("Enter your choice: "))
            if f==1:
                Question()
            elif f==2:
                Quiz()
            elif f==3:
                print("Exiting the Quiz \n\n")
                mycursor.close()
                mydb.close()
                break
                #sys.exit();
            else:
                Home()
    def Question():
        print('\n\n')
        ch='Y'
        while ch=='Y' or ch=='y':
            print("Welcome to Question Portal")
            print("***********************")
            q=input("Enter the question :")
            op1=input("Enter the option 1 :")
            op2=input("Enter the option 2 :")
            op3=input("Enter the option 3 :")
            op4=input("Enter the option 4 :")
            ans=0
            while ans==0:
                op=int(input("Which option is correct answer (1,2,3,4) :"))
                if op==1:
                    ans=op1
                elif op==2:
                    ans=op2
                elif op==3:
                    ans=op3
                elif op==4:
                    ans=op4
                else:
                    print("Please choose the correct option as answer")
            mycursor.execute("Select * from question")
            data=mycursor.fetchall()
            qid=(mycursor.rowcount)+1
            mycursor.execute("Insert into question values (%s,%s,%s,%s,%s,%s,%s)",(qid,q,op1,op2,op3,op4,ans))
            mydb.commit()
            ch=input("Question added successfully.. Do you want to add more (Y/N)")
        Home()
    def Quiz():
        print('\n\n')
        print("Welcome to Quiz portal")
        print("***********************")
        mycursor.execute("Select * from question")
        data=mycursor.fetchall()
        name=input("Enter your name :")
        rc=mycursor.rowcount
        noq=int(input("Enter the number of questions to attempt (max %s):"%rc))
        l=[]
        while len(l)!=noq:
            x=random.randint(1,rc)
            if l.count(x)>0:
                l.remove(x)
            else:
                l.append(x)
        print("Quiz has started")
        c=1
        score=0
        for i in range(0,len(l)):
            mycursor.execute("Select * from question where qid=%s",(l[i],))
            ques=mycursor.fetchone()
            print("--------------------------------------------------------------------------------------------")
            print("Q.",c,": ",ques[1],"\nA.",ques[2],"\t\tB.",ques[3],"\nC.",ques[4],"\t\tD.",ques[5])
            print("--------------------------------------------------------------------------------------------")
            c+=1
            ans=None
            while ans==None:
                choice=input("Answer (A,B,C,D) :")
                if choice=='A' or choice=='a':
                    ans=ques[2]
                elif choice=='B' or choice=='b':
                    ans=ques[3]
                elif choice=='C' or choice=='c':
                    ans=ques[4]
                elif choice=='D' or choice=='d':
                    ans=ques[5]
                else:
                    print("Kindly select A,B,C,D as option only")
            if ans==ques[6]:
                print("Correct")
                score=score+1
            else:
                print("Incorrect.. Correct answer is :",ques[6])
        print("Quiz has ended !! Your final score is :",score)
        input("Press any key to continue")
    Home()
# create database quiz
# create table question(qid int,q varchar(100), op1 varchar(100),op2 varchar(100), op3 varchar(100), op4 varchar(100),ans varchar(100));

def tic():
    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '1': ' ' , '2': ' ' , '3': ' ' }
    board_keys = []
    for key in theBoard:
        board_keys.append(key)
    def printBoard(board):
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('-+-+-')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('-+-+-')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
    def game():
        turn = 'X'
        count = 0
        for i in range(10):
            printBoard(theBoard)
            print("It's your turn," + turn + ".Move to which place?")
            move=input('Enter where to place the mark between 0 to 9:')
            if int(move)<=9:
                if theBoard[move] == ' ':
                    theBoard[move] = turn
                    count += 1
                else:
                    print("That place is already filled.\nMove to which place?")
                    continue
                if count >= 5:
                    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")                
                        break
                    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break 
                    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
            else:
                print('Enter a number between 1 to 9')
                continue
            if count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'        
        restart = input("Do want to play Again?(y/n)")
        if restart == "y" or restart == "Y":  
            for key in board_keys:
                theBoard[key] = " "
            game()
    if __name__ == "__main__":
        game()

        
def number():
    import random
    n = random.randint(1, 100)
    count = 1
    guess_chances = 10
    while 1 <= guess_chances:
        num = int(eval(input("Guess the Number: ")))
        if num > n:
            print("Your guess was too high: Guess a number lower than", num)
        elif num < n:
            print("Your guess was too low: Guess a number higher than", num)
        else:
            print("You Win!")
            print(count, "gueses you took")
            break
        guess_chances -= 1
        print(guess_chances, "Guesses Left")
        count += 1
        print()
    print("Game over")
    print("Number is ", n)

def word():
    import random
    from collections import Counter
    someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon''' 
    someWords = someWords.split(' ')
    word = random.choice(someWords)        
    if __name__ == '__main__':
        print('Guess the word! HINT: word is a name of a fruit')
        for i in word:     
            print('_', end = ' ')       
        print()
        playing = True
        letterGuessed = ''               
        chances = len(word) + 2
        correct = 0
        flag = 0
        try:
            while (chances != 0) and flag == 0: 
                print()
                chances -= 1
                try:
                    guess = str(input('Enter a letter to guess: '))
                except:
                    print('Enter only a letter!')
                    continue
                if not guess.isalpha():
                    print('Enter only a LETTER')
                    continue
                elif len(guess) > 1:
                    print('Enter only a SINGLE letter')
                    continue
                elif guess in letterGuessed:
                    print('You have already guessed that letter')
                    continue
                if guess in word:
                    k = word.count(guess) 
                    for _ in range(k):   
                        letterGuessed += guess 
                for char in word:
                    if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                        print(char, end = ' ')
                        correct += 1
                    elif (Counter(letterGuessed) == Counter(word)):
                        print("The word is: ", end=' ')
                        print(word)
                        flag = 1
                        print('Congratulations, You won!')
                        break
                        break
                    else:
                        print('_', end = ' ')
            if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print('You lost! Try again..')
                print('The word was {}'.format(word))
        except KeyboardInterrupt:
            print()
            print('Bye! Try again.')
            exit()
    



while True:
    print('\n\nPromgram:')
    print('1. To play Quiz.')
    print('2. To play Tic Tac Toe.')
    print('3. To play Guess the number.')
    print('4. To play Guess the word.')
    print('5. To Exit')
    ch=int(input('Enter choice:'))
    if ch==1:
        quiz()
    elif ch==2:
        tic()
    elif ch==3:
        number()
    elif ch==4:
        word()
    elif ch==5:
        print('\n\nThank you for playing!!')
        break
    else:
        print('Enter a valid choice!!\n')
