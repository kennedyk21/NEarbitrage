import random
def play(z,x,y):
     print("user: "+z[x]+" computer: "+z[y])
x=int(input("Rock-0,Paper-1,Scissors-2"))
y=random.randint(0,2)
z=["Rock","Paper","Scissors"]
if (x==y):
    print("its a draw")
elif(x==0 and y==2):
    play(z,x,y)
    print(z[x]+" wins")
elif(x==2 and y==0):
    play(z,x,y)
    print(z[y]+" wins") 
elif(x>y):
    play(z,x,y)
    print(z[x]+" wins")
elif(y>x):
    play(z,x,y)
    print(z[y]+" wins")
