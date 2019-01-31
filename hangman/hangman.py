import os
import random

try:
    def print_count(count,msg):
        os.system("clear")
        print('\n'+msg+'\n')
        print("Hint:",WORD[1])
        print(count)
        print("Guessed alphabet ->",end=' ')
        for k in word_tbl.keys():
            if word_tbl[k] == 2:
                print(k.upper(),end=' ')
        print()

    def print_word(answer,wrd_tbl):
        missing = 0
        for c in answer:
            if(c==' '):
                print(' ',end='')
            elif(wrd_tbl[c.lower()] == 2):
                print(c,end='')
            else:
                missing += 1
                print('_',end='')
        print()
        return missing

    WORD_CATAGORIES = [x[:-5] for x in os.listdir("./data/") if ".wpsv" in x]
    count = 0
    word_tbl = {}
    tmp = ord('a')
    #print(WORD_CATAGORIE)
    print("Select Word catagories")
    for i in range(len(WORD_CATAGORIES)):
        print(f"({i+1}) {WORD_CATAGORIES[i]}")
    cat_ind = int(input("Select via number ('1', '2', ... only): "))
    WORD = open(f"./data/{WORD_CATAGORIES[cat_ind-1]}.wpsv").read().split('\n')[:-1]
    WORD = WORD[random.randint(0,len(WORD)-1)].split('|')
    print("Hint:",WORD[1])
    for i in range(26):
        c_char = chr(tmp+i)
        if c_char in WORD[0].lower():
            word_tbl[c_char] = 1
        else:
            word_tbl[c_char] = 0
    print_word(WORD[0], word_tbl)
    while(count<=10):
        guess = input("Guess: ").lower()
        if guess not in word_tbl.keys():
            print_count(count,"That not a alphabet")
            #raise IOError
            continue
        if word_tbl[guess] == 2:
            print_count(count,"You already guess that ^^")
        elif word_tbl[guess] == 0:
            count += 1
            word_tbl[guess] = 2
            print_count(count, f"Oh no!! '{guess}' is not in your word")
        else:
            word_tbl[guess] = 2
            print_count(count, f"Yeah!! '{guess}' is in your word")
        if(print_word(WORD[0], word_tbl)==0):
            print("Gotcha~ you discover all the alphabet :)")
            break
    if(count == 11):
        print("Your hangman can't make it! Try again next time :(")
#except:
except Exception as e: 
    print()
    print(e)
    print("Something want wrong. Make sure you got the latest version from 'https://github.com/WisTiCeJEnT/theinternship-exam-2019'")
