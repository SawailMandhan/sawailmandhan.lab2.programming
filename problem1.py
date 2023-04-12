total=0
#for taking input from user of  how many years of ranifall want to calculate
a=int(input("Enter the number of years: "))
for i in range(1,a+1):
#for printing year
  print(" For year:-",i)
#used "for" loop for taking input from user of 12 months
#for loop is for repeating function
  for j in  range(1,13):
    b=float(input("Enter the rainfall amount for the month: "+str(j)+" :"))
    total=total+b
#calculating total
print("Total rainfall:",total,"inches")
#calculating average
print("Average monthly rainfall=",total/j*a,"inches")