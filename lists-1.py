# Create a dictionary of 5 names as keys and their age as values. Find the name of the oldest person

names={"Bob":12,"Sunny":8,"John":9,"Steven":14,"Mike":11}
ages=[]
name=""
old=0
for i in names:
    if names[i] > old:
        name=i
        old=names[i]
print(name)
