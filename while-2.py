# Using only one while loop and no for loops, print from 1-10 and then back to 1

num=0
state=True
while num != 11:
    if num==10:
        state=False
    if state==True:
        num=num+1
    if state==False:
        if num==1:
            break
        num=num-1
    if num==6:
        pass
    elif num!=6:
        print("Hello:",num)
