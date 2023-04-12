#take input from user of number of organism
number=float(input("Starting number of organisms/species: "))
#take input from user of percantage
percantage=float(input("Average daily percentage increase: "))
#take input from user of how many days of data should print here
total=int(input("Enter the number of days to display the final data: "))
print("Day Approximate        Population")
print("------------------------------------------")
#c is for output
c=number
print(1,"                      ",c,"\n")
for i in range(1,total):
#formula for final output
  c=number+(number*(percantage/100))
  number=c
  print(i+1,"                      ",c,"\n")