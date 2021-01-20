filename = open("","r")
dictionary={}
with open('ident.txt','r') as f:
    for line in f.readlines():
        a,b = line.split()
        dictionary[a] = int(b)