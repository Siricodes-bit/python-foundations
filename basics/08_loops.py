'''
Covering the loops concepts
'''
# Using For loop
for i in range(1,11):
    print("number:",i,end='\n')

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L',
         'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for k in alphabets :
    print("Alphabets:",k)
string = "Hello! How are you bro, are you okay?"
list_string = string.split(" ")
print(list_string)
for j  in list_string:
    print("String:",j)

# Using While Loop

i = 0
while i < 100:
    if i % 2 == 0 :
        print("Even numbers:",i,end=" ")
    i+=1

# Using break , continue, pass

for i in range(1,11):           # skipping when both i and j are even
    for j in range(5,10):
        if i % 2 == 0 and j % 2 == 0:
            continue
        print(f'{i} {j} ')

for l in range(25,51):
    if l == 40:
        break
    print(l)

for u in range(1,7):
    if u % 3 == 0:
        pass
    print(u)
