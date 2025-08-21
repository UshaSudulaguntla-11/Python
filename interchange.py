n=int(input("Enter the value of n:"))
l=[]
for i in range(n):
  ele=int(input("Enter a number:"))
  l.append(ele)
print("Before interchanging:",l)
l[0],l[-1]=l[-1],l[0]
print("After interchanging:",l)



