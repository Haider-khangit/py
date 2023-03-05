import random
def Game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            print("you Won")
        else:
            print("you lost")
    elif comp=='g':
        if you=='w':
            print("You Won")
        else:
            print("you lost")
    elif comp=='w':
        if you=="s":
            print("you Won")
        else:
            print("you lost")


rand=random.randint(1,3)
print("Players's Turn: Snake (S), Gun(G) and Water(W)")
if(rand==1):
     comp ='s'
elif(rand==2):
    comp = 'g'
else:
    comp='w'

you=input('Players Turn: Snake (S), Gun(G) and Water(W)')
a=Game(comp,you)
print(a)