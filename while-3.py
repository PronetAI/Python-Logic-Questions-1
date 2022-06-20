# Create an empty list. Keep on adding random integers between 1 and 10 to this list till it contains a multiple of 5 as well as a multiple of 10
import random
group=[]
five=False
ten=False
while True:
    num=random.randint(1,10)
    group.append(num)
    for i in group:
        if i % 5:
            five=True
        if i % 10:
            ten=True
    if five==True and ten==True:
        break
print(group)
