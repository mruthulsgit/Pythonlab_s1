ls=input("enter list of words:").split()
print(len(sorted(ls,key=lambda x:len(x),reverse=True)[0]))