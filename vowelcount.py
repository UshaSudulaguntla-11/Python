str=str(input("Enter a string:"))
count=0
for i in str:
	if i in ['a','e','i','o','u','A','E','I','O','U']:
		count+=1
print("number of vowels:",count)
print("number of consonants:",len(str)-count)	
