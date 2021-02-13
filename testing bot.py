import string
x="hello world"
y=list(string.ascii_lowercase)
z=''
for i in x:
    try:
        z=z+" "+str(y.index(i))
    except:
        z=z+" "+str(i)

print (z)