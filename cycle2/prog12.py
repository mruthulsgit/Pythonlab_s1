a=list(input("Enter the word:"))
b=['a','A','e','E','i','I','o','O','U','u']
j=[x for x in a if x in b]
print(j)