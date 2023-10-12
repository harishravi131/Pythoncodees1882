import random
import time
start=time.time()
print('There will be 5 questions and you will be timed')
flag=0
for i in range(5):
    if flag==0:
        a=random.randint(1,19)
        b=random.randint(1,19)
        print('Product ',a,' ',b,' equals')
        c=int(input())
        d=a*b
        if(c==d):
            print('Correct')
        else:
            print('wrong, the correct answer is ',d)
            flag=1
if flag==0:
    stop=time.time()
    timeelapsed=stop-start
    print('Your time is ',timeelapsed)

