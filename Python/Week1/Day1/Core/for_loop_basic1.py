# printing integers from 0 to 150 

for i in range (151):
    print(i)



# #  Printing all the multiples of 5 from 5 to 1,000

for i in range (1001):
    if i%5==0 :
        print(i)


#Counting, the Dojo Way


for i in range (101):
    if i%10==0 :
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")    
    else :
        print (i)



# Whoa. That Sucker's Huge

sum=0 
for i in range(500001):
    if i%2==1 :
        sum=sum+i
print (sum)        
        



#Countdown by Fours

for i in range(2018,-1,-4):
    print (i)






#Flexible Counter
lowNum=2
highNum=9 
mult=3
for i in range(lowNum,highNum+1,+1):
    if i%mult==0 :
        print(i)