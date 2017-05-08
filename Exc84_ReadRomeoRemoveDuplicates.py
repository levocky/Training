fh = open("romeo.txt")
lst = list()
words = list()

for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word == None or word =="":
            pass
        lst.append(str(word))

# remove duplicates
lst = list(set(lst))
lst = sorted(lst)
print (lst)
