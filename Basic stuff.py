""" import random
print (random.randint(1,10))
print(random.randint(30,300))

print(random.random())

answer = random.randint(1,3)
if answer ==1:
    print("yes")
if answer ==2:
    print("no")
if answer ==3:
    print("maybe") """




import random
lucky_number=random.randint(1,100)
fortune_number=random.randint(1,3)
fortune_text=''
if fortune_number ==1:
    fortune_text='have a great day'
if fortune_number ==2:
    fortune_text='it;s a tough day'
if fortune_number ==3:
    fortune_text='win lottery'
print(f"{fortune_text}, your lucky number is :{lucky_number}")
