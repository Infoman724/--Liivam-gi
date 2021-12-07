from random import*
KNB=["k", "n", "b"]
text=str(input("Играем в камень ножницы бумага! игаем с AI?/Player?"))
while text=="AI":
     while 1:
        a=str(input("player1>>>"))
        m=KNB.index(a)
        print()
        BOT=randint(0,2)
        print(BOT)
   
        if m==BOT :
            print("ничья")
        elif m==2 and BOT==0 or m==0 and BOT==1 or m==1 and BOT==2 :
            print("player1 win")
            print()
        else:
            print("BOT win")
            