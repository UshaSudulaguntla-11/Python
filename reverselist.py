n=int(input("Enter the value of n:"))
l=[]
for i in range(n):
  ele=int(input("Enter a number:"))
  l.append(ele)
print("Original list is",l)
print("Reversed List is",l[::-1])
