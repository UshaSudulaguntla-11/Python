n=int(input("Enter the value of n:"))
l=[]
for i in range(n):
  ele=int(input("Enter a number:"))
  l.append(ele)
print("Original list is",l)
x=int(input("Enter an element to remove:"))
l.remove(x)
print(x,"is removed successfully")
print("Updated List",l)
