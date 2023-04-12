#for range function
x=[]
#for taking
number=int(input("enter the range: "))
greater=int(input("enter the greater: "))
for i in range(1,number+1):
#append is for adding numbers
     x.append(i)
print("List of the numbers: ")
print(x)
#for finding greater number 
y=[]
for i in range(1,number+1):
#calculating greater number
    if(x[i-1]>greater):
      y.append(x[i-1])
else:
     pass
#printing the list of greater number 
print("List of the numbers greater than 12: ")
print(y) 
