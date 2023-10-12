import random
import time
win=0
print('The computer rolls the dice for yourself and machine')
for i in range(10):
    if(win==0):
        
        a=random.randint(1,6)
        b=random.randint(1,6)
        print('You got ',a,'Computer got ', b)
        if(a==6):
            print('You won')
            win=1
        elif(b==6):
            print('Computer won')
            win=1
            
        time.sleep(2)
