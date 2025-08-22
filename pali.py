str=str(input("Enter a string:"))
rev_str=""
for i in str:
	rev_str=i+rev_str
if(rev_str==str):
	print(str,"is a palindrome")
else:
	print(str,"is not a palindrome")
