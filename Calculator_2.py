#The ALU has digital circuits for sum, subtraction, multiplication and comparision.
#The challenge here would be to write the code for division, square root, trignometric and other fuctions
#The following python code just needs python install of 30 MB and was written by Dr. Harish Ravi on 24 Nov 2019

x='2555'; #4 digit number
y='1445'; #4 digit number

#Doing representation of two digit product
product=int(x[3])*int(y[3])+10*(int(x[2])*int(y[3])+int(x[3])*int(y[2]))+\
        100*(int(x[1])*int(y[2])+int(x[1])*int(y[3])+int(x[3])*int(y[1]))+\
        1000*(int(x[0])*int(y[3])+int(x[3])*int(y[0])+int(x[2])*int(y[1])+int(x[1])*int(y[2]))+\
        10000*(int(x[0])*int(y[2])+int(x[2])*int(y[0])+int(x[1])*int(y[1]))+\
        100000*(int(x[0])*int(y[1])+int(y[0])*int(x[1]))+\
        1000000*(int(x[0])*int(y[0]))

#Doing representation of digit sum and subtraction
add=int(x[3])+int(y[3])+10*(int(x[2])+int(y[2]))+100*(int(x[1])+int(y[1]))+1000*(int(x[0])+int(y[0]))
sub=int(x[3])-int(y[3])+10*(int(x[2])-int(y[2]))+100*(int(x[1])-int(y[1]))+1000*(int(x[0])-int(y[0]))

#Showing output,
print('Product of ',x,' and' ,y,' ', product,int(x)*int(y))
print('Sum of',x,' and' ,y,' ',add)
print('Subtraction  ',x,' and' ,y,' ',sub)

#Dividing x a two digit number by z a single digit number
z='3'# Single digit number
ha=1;# While loop flag
j=0; # Increasing the quotient in the loop until the product exceeds the divisor
while ha:
    
    r=int(x[1])+10*int(x[0])-j*int(z[0]);
    if(r<int(z[0])):
        ha=0; #Setting the while loop flag to 0 to come out of the loop
    j=j+1; #incrementing the quotient until it divides
        
j=j-1; # Reducing the quotient as we counted one past

#Getting the decimal point of the quotient
ha=1;
h=0;
while ha:
    
    r2=r*10-h*int(z[0]);
    if(r2<int(z[0])):
        ha=0;
    h=h+1;
h=h-1;
print('division of ',x,' and' ,z,' ',j,'.',h)

#Finding square root by subtracting successively the contribution from most significant digit.
sq='314';
ha=1;
a=0;
while ha:
    luv=int(sq[0])*100+int(sq[1])*10+int(sq[2])-100*a*a;
    a=a+1;
    if luv<0:
        ha=0;

a=a-2;
ha=1;
b=0;
while ha:
    luv2=int(sq[0])*100+int(sq[1])*10+int(sq[2])-100*a*a-(20*a+b)*b;
    b=b+1;
    if luv2<0:
        ha=0;
b=b-2;

ha=1;
c=0;
while ha:
    luv3=100*(int(sq[0])*100+int(sq[1])*10+int(sq[2])-100*a*a-(20*a+b)*b)-c*(200*a+20*b+c);
    c=c+1;
    if luv3<0:
        ha=0;
c=c-2;


print('Square root of ',sq , ' ',10*a+b,'.',c)





        
    










        
    
