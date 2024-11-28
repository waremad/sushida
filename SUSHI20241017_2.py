# pip install keyboard
# python3
#Windows PowerShell

from sura import sura
from imedoko import imadoko
from kunhebo import kunhebo
from itti import itti
from unshift import unshift
from kaneroo import kanaroo
from readtxt import readtxt
from bkunhebo import bkunhebo
from suranhe import suranhe
import keyboard
import random
import time

#def cprint(self="tesuto",pt=[0,0],title="テスト",kana="てすと",turn=0,score=0):
def cprint(self="tesuto",pt=[0,0],title="テスト",kana="てすと",turn=0,score=[0,0,1]):
    print("\n\n\n")

#    print(turn," SCORE :",score//1)
    print(turn," SCORE :",int(score[0]//1)," WPS :",((score[1]/score[2])*10 // 1)/10)

    print(f'\033[38;2;255;255;255m{kana}\033[0m')
    print(f'\033[1;38;2;255;255;255m{title}\033[0m')
    if len(self) < pt[0]:
        print("len(self) != len(pt)")
        return 0
    for i in range(len(self)):
        if pt[0]<=i:
            if pt[1]==1 and pt[0]==i:#赤
                print(f'\033[1;38;2;255;0;0m{self[i]}\033[0m', end="")
            else:#白
                print(f'\033[1;38;2;255;255;255m{self[i]}\033[0m', end="")
        else:#黒
            print(f'\033[38;2;127;127;127m{self[i]}\033[0m', end="")
    print("\n")

dic = readtxt()
turn = 0
score = [0,0,1]
bef = ""

while not(turn == 10):
    turn = turn + 1

    rkey = list(dic.keys())
    title = random.choice(rkey)
    kana = dic[title]
    dic.pop(title)



#    print(kana,kanaroo(kana))
    ls = kanaroo(kana)
#    print(ls)
    lsp = [0,0]
    tx = ""
#    print(ls)
    for i in ls:
        if len(i) != 0:
            tx = tx + i[0]

    pt = [0,0]
    

    bakkuW = ""
#    print(tx)

    title = suranhe(title)
    kana = suranhe(kana)

    syokai = True    

#    time.sleep(0.5)
    start = time.time()


#    cprint(tx,pt,title,kana,turn,score)

    while not(pt[0] >= len(tx)):
        out = False
    #    print(pt[0],len(tx)-1)
        while not(out):
            if len(tx) > pt[0]+1:
#                print(tx,pt,tx[pt[0]:pt[0]+1],tx[pt[0]:pt[0]+1] == "\n")
                while len(tx) > pt[0]+1 and ( tx[pt[0]:pt[0]+1] == "\n" or tx[pt[0]] == " " or tx[pt[0]] == "　"):
                    pt[0] = pt[0] + 1
#                    print(pt)
#            print(tx[pt[0]],tx,pt,tx[pt[0]] == " ",tx[pt[0]] == "　")
#            print(tx,tx[pt[0]],tx[pt[0]] == " ",tx[pt[0]] == "　")
            tx = ""
            for i in ls:
                tx = tx + i[0]
    #        print(out,tx[pt[0]])

            if syokai:
                cprint(tx,pt,title,kana,turn,score)
                syokai = False

            # キーイベントを待機
            event = keyboard.read_event()

            # キーが押された場合、キーの種類を表示
            if event.event_type == keyboard.KEY_DOWN:  # キーが押された場合
                oshift = keyboard.is_pressed("shift")
                
#            print("test:",out,bef)
#            print(0,bef,1,event.name)
            if (bef == "" or "shift" in bef) and len(event.name) == 1:
    #            print(tx,pt,oshift,event.name)
                if itti(tx,pt,oshift,event.name):
                    pt[0] = pt[0] + 1
                    pt[1] = 0
                    out = True
                    cprint(tx,pt,title,kana,turn,score)
                    if "shift" in bef:
                        bakkuW = unshift(event.name)
                    else:
                        bakkuW = ""
                else:
    #                print(pt,ls)
                    lsp =  imadoko(pt,ls)
    #                print(lsp)
    #                bool1 = False
    #                for i in range(len(ls[lsp[0]])):
    #                    if (ls[lsp[0]])[i][lsp[1]] == event.name:
    #                        bool1 = True
    #                print(bool1)
                    if kunhebo(ls,lsp,event.name):
                        ls2 = ls[lsp[0]]
                        ls[lsp[0]] = []
                        for i in ls2:
                            if i[lsp[1]] == event.name:
                                ls[lsp[0]].append(i)
                        pt[0] = pt[0] + 1
                        pt[1] = 0
                        out = True
                        tx = ""
                        for i in ls:
                            tx = tx + i[0]
                        cprint(tx,pt,title,kana,turn,score)
                    elif bkunhebo(ls,lsp,event.name):
                        ls2 = ls[lsp[0]-1]
                        ls[lsp[0]-1] = []
                        for i in ls2:
#                            print(ls2,i)
                            if len(i) > len(ls2[0]):
                                if i[len(ls2[0])] == event.name:
                                    ls[lsp[0]-1].append(i)
                        pt[0] = pt[0] + 1
                        pt[1] = 0
                        out = True
                        tx = ""
                        for i in ls:
                            tx = tx + i[0]
                        cprint(tx,pt,title,kana,turn,score)
                    elif bakkuW == event.name:
                        pass
                    elif pt[1] == 1:
                        pass
                    else:
#                        print(bef,pt,tx,event.name,ls,)
                        pt[1] = 1
                        cprint(tx,pt,title,kana,turn,score)
            bef = event.name
            if keyboard.is_pressed(event.name)==False:
                bef = ""
#        print(pt[0],len(tx)-1)
    score = [score[0] + (len(ls) / (time.time() - start)) * 60, score[1] + len(ls) , score[2] + (time.time() - start)]
print("end"," SCORE :",int(score[0]//1)," WPS :",((score[1]/score[2])*10 // 1)/10," WORDS :",score[1]," TIME :",((score[2])*100 // 1)/100)