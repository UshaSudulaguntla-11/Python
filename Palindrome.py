n=int(input("Enter the value of n:"))
rev=0
rem=0
original=n
while(n>0):
  rem=n%10
  rev=rev*10+rem
  n=n//10
if(rev==original):
  print("Palindrome")
else:
  print("Not a Palindrome")
