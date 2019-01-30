import os
import random

def print_count(count,msg):
    os.system("clear")
    print(msg)
    print("Hint:",WORD[1])
    print(count)

try:
    WORD_CATAGORIES = [x[:-5] for x in os.listdir("./data/") if ".wpsv" in x]
    count = 0
    word_tbl = {}
    tmp = ord('a')
    #print(WORD_CATAGORIE)
    print("Select Word catagories")
    for i in range(len(WORD_CATAGORIES)):
        print(f"({i+1}) {WORD_CATAGORIES[i]}")
    cat_ind = int(input("Select via number ('1', '2', ... only): "))
    WORD = open(f"./data/{WORD_CATAGORIES[cat_ind-1]}.wpsv").read().split('\n')
    WORD = WORD[random.randint(0,len(WORD)-1)].split('|')
    print("Hint:",WORD[1])
    for i in range(26):
        c_char = chr(tmp+i)
        if c_char in WORD[0]:
            word_tbl[c_char] = 1
        else:
            word_tbl[c_char] = 0
    while(count<=10):
        guess = input("Guess: ")
        if guess not in word_tbl.keys():
            print_count(count,"That not a alphabet")
            continue
            #raise IOError
        if word_tbl[guess] == 2:
            print_count(count,"You already guess that ^^")
            continue
        elif word_tbl[guess] == 0:
            count += 1
            print_count(count, f"Wrong!! '{guess}' is not in your word")
            word_tbl[guess] = 2
        else:
            print_count(count, f"True!! '{guess}' is in your word")
            word_tbl[guess] = 2
except:
    print()
    print("See yaa")