# Create an empty list. Keep on adding random integers between 1 and 10 to this list till it contains 5
import random
group=[]
for i in range(1,6,1):
    num=random.randint(1,10)
    group.append(num)
print(group)
