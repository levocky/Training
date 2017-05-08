#fname = raw_input("Enter file name: ")
#fh = open(fname)
fh = open("romeo.txt")
lst = list()

for line in fh:
    words = line.rstrip().split()
    
    for word in words:
        if word == None or word == "":
            pass
        lst.append(str(word))
        
print(words)


print ("First ", len(lst), "\n", lst)

lst = list(set(lst))

lst = lst.sort()

print (len(lst))
lst = sorted(lst)
print (type(lst))
print ("Second ", len(lst), "\n", lst)
#print(s)  
