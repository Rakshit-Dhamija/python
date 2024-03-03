import random

guess = 0

def again():
    guess = 0
    word = random.choice(["absence","abuse","account","accident","beneath","bend","benefit","biology","bitter","candidate","campaign","camera","capacity","capture","deaf","daughter","deal","decorate","dialogue","economy","finance","educate","efficient","supportive","elderly","flight","folk","flame","frustration","garbage","gather","gentle","global","hilarious","intelligence","jazz","knife","longevity","momument","nonsense","nobody","turmeric","utilize","sashimi","reconfigure","wheat","yellowish","zone"])
    space = "_ "*len(word)
    space1 = space.split()
    while "".join(space1) != word:
        player = str(input("Your word guess: "))
        indexthing= [i for i, j in enumerate(word) if j == player]
        if player in word:
            if word.count(player) == 1 and len(player)==1:
                index = word.index(player)
                space1[index]=player
                print(" ".join(space1))
                guess +=1
                print("Correct!!!")
                print("- - - - - - - - - - - - - - - - - -")
            if word.count(player) > 1 and len(player)==1:
                for i in indexthing:
                    space1[i] = player
                    print(" ".join(space1))
                    print("Correct!!!")
                    print("- - - - - - - - - - - - - - - - - -")
                    guess += 1
            if len(player) > 1 and player in word:
                listOfIndex = []
                for i in list(player):
                    listOfIndex.append(word.index(i))
                    space1[listOfIndex[0]:listOfIndex[-1]+1] = list(player)
                    print(" ".join(space1))
                    print("Correct")
            if len(player) > 1 and player == word:
                print("You've got correct word: ",word)
                print("You've guessed for ", str(guess+1)," times")
                raise SystemExit(0)
            else: 
                print(" ".join(space1))
                print("Wrong!!!")
                guess += 1
                print("- - - - - - - - - - - - - - - - - -")
again()
