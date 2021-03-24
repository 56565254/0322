import random
import time
print("歡迎光臨Myphone")
print("  ")
print("來個蹦蹦?")

print("  ")


class Condition():#寵物狀態
    def __init__(self,名字):
        self.名字 = 名字

        
    def list_Condition(self): #狀態顯示
        print('吾乃',self.名字)


while 1:
    pet = Condition(input(' 三天之上，以道為尊；萬法之中，焚香為首。今以道香、德香、無為香、無為清靜自然香、靈寶惠香，超三界三境，遙瞻百拜真香。急急如律令。請取名 謝謝:   '),)#寵物取名、出生
    print("  ")
    print("  ")

    print('朋友們若是真心對我，我必定在你贏的時候陪你君臨天下，在你輸得時候陪你東山再起。   所以你確定要叫',pet.名字,'嗎？')
    while 1:
        print('  1. Yes','\n  2. No')
        確定名字 = input()
        if 確定名字 == '1':
            print("  ")
            print("欠我錢我可以笑笑的，但背叛我，就七天回家 ")
            
            break
        elif 確定名字 == '2':
            print("  ")
            print(" 稱你一聲哥，是因為你年紀比我大，社會歷練比我深，但你做出來的事情還值不值得我稱你哥還是另一回事。 你他媽搞我? ")
            print("  ")
            break
        else :
            print("  ") 
            print( "沒有很可以，但你惹不起,就問你Yes or No")
    if 確定名字 == '1':
        break
print("  ")
print('\nGame Start','\n異空轉生  藤元括海 莫忘初衷呦 ',pet.名字,'SB 哈哈是你啦  ')
print("  ")
print('-'*50)  #分隔線

health = random.randint(50,80)
strong = 0
happy = 30
fat = random.randint(50,80)
hunger = 50
Petlist=[health,strong,happy,fat,hunger]
day=[0]
def eat():
    Petlist[0] +=4
    Petlist[3] -=2
    Petlist[4] -=5
def feel():
    Petlist[0] +=1
    Petlist[1] +=3
    Petlist[2] -=4
    Petlist[3] -=1
    Petlist[4] -=4 
def exercise():
    Petlist[0] +=1
    Petlist[1] +=1
    Petlist[2] -=4
    Petlist[3] -=3
    Petlist[4] -=4
def stool():
    Petlist[3] +=5
    Petlist[4] +=10
def play():
    Petlist[0] -=4
    Petlist[2] +=8
def Action():
    print("吃火鍋(1) 摸摸(2) 運動(3) 大便(4) 打飛機(5)")
    action=str(input("來吧寶貝"))
    if action == "1":
        eat()
        print("  ")
        print("一代一代一代一代୧〳 ＾ ౪ ＾ 〵୨")
        day[0]+=1
    elif action =="2":
        feel()
        print("  ")
        print("雅梅碟,受不了了啦୧༼ ヘ ᗜ ヘ ༽୨")
        day[0]+=1
    elif action =="3":
        exercise()
        print("  ")
        print("太快了,我不行了 (ᗒᗣᗕ)՞")
        day[0]+=1
    elif action =="4":
        stool()
        print("  ")
        print("快了快了,應到未到,已經探頭探腦了 ٩(✿∂‿∂✿)۶՞")
        day[0]+=1
    elif action =="5":
        play()
        print("  ")
        print("郎若回頭,必有緣由,不是報恩,就是報仇(╬•᷅д•᷄╬)")
        day[0]+=1
    else:
        print("  ")
        print("不怕黑社會,只怕社會黑  盆栽要剪 女人要扁   ")
        print("  ")
        print("            1到5，你他媽是在哭?  ")
        print("  ")
while 1:
    Action()
    print("  ")
    print("HP:",Petlist[0],"粗度",Petlist[1],"爽度",Petlist[2],"肥度",Petlist[3],"飢渴度",Petlist[4])
    if Petlist[0] <= 0:
        print("  ")
        print("你硬不起來,垂了QQ")
        print("生存天數:",day[0],"天")
        break
    elif Petlist[1] >=100:
        print("  ")
        print("養了特別粗的辣個男人!!")
        print("成就達成花了",day[0],"天")
        continue
    elif Petlist[2] <=0:
        print("  ")
        print("你的女孩不性福抑鬱死了QQ")
        print("生存天數:",day[0],"天")
        break
    elif Petlist[2] >=100:
        print("  ")
        print("養了幸福的小女孩!!")
        print("  ")
        print("成就達成花了",day[0],"天")
        continue
    elif Petlist[3] <=0:
        print("  ")
        print("你的Justin bieber太瘦死了GG")
        print("  ")
        print("生存天數",day[0],"天")
        break
    elif Petlist[3] >=100:
        print("  ")
        print("你的曾阿牛肥死了QQ")
        print("  ")
        print("生存天數:",day[0],"天")
        break
    elif Petlist[4] <=0:
        print("  ")
        print("你的柯博文餓死了QQ")
        print("  ")
        print("生存天數:",day[0],"天")
        break
    elif Petlist[4] >=100:
        print("  ")
        print("你的柯文哲吃太多撐死了QQ")
        print("  ")
        print("生存天數:",day[0],"天")
        break
    else:
        continue
