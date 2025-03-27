import random as r

password = ""
a = [0,1,2,3,4,5,6,7,8,9]
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c = ['!','@','#','$','%','^','&','*','(',')']

x = int(input("No. of characters:"))
y = int(input("No. of integers: "))
z = int(input("No. of special characters: "))

while x:
    m = r.randint(0,2)
    if m == 0 and y > 0:
        y-= 1
        x -= 1
        password = password + str(a[r.randrange(len(a))])
    elif m == 1 and z > 0:
        z -= 1
        x -= 1
        password = password + c[r.randrange(len(c))]
    elif m == 2 and x > y + z:
        x -= 1
        password = password + b[r.randrange(len(b))]

print(f"Password = {password}")