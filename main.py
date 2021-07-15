start=input("What's Your Name: ")
print("Hello " + start)
#number=""
M1= int(input("Enter a number from 0-100 to count up by 5s: "))
for dafive in range( 0, 101):
  if dafive % 5 == 0:
    print (dafive, end=" ")

print('\n')

M2= int(input("Enter a number from 0-1000 to count up by 50s: "))
for daten in range(0, 1001):
  if daten % 50 == 0:
    print (daten, end=" ")

print('\n')

M3= int(input("Enter a number from 0-100 to count up by Odds: "))
for daodd in range(0, 101):
  if daodd % 2 != 0:
    print (daodd, end=" ")

print('\n')

M4= int(input("Enter a number from 0-100 to count up by Evens: "))
for daeven in range(0, 101):
  if daeven % 2 == 0:
    print (daeven, end=" ")

print('\n')

print("Thank you for viewing my counter " + start + "!!!! Have a Good Day!!!")
