# Using a while loop, print from 1-10 but skip 6 with a hello next to each number

num=0
while num != 10:
    num=num+1
    if num==6:
        pass
    elif num!=6:
        print("Hello:",num)
