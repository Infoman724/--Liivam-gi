from random import*
KNB=["k", "n", "b"]
text=str(input("Играем в камень ножницы бумага! игаем с AI?/Player ?"))
if text=="AI":
    print("Вы можете выбрать:Камень-k,Ножницы и Бумагу-b")
    print()
    print("Ответы БОТА:0-k,1-n,2-b")
    print()
while text=="AI":
     while 1:
        print()
        a=str(input("player1>>>"))
        m=KNB.index(a)
        print()
        BOT=randint(0,2)
        print("BOT кидает:",BOT)
        print()
        if m==BOT :
            print("ничья")
        elif m==2 and BOT==0 or m==0 and BOT==1 or m==1 and BOT==2 :
            print("player1 win")
            print()
        else:
            print("BOT win")



            