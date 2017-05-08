# Use the file name mbox-short.txt as the file name
import re
#fname = input("Enter file name: ")
#fh = open(fname)

fh = open("mbox-short.txt","r")
          
i = 0
totnum = 0
extnum = 0

for line in fh:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    i = i +1
    extnum = re.findall('[0-9]+',line)
    extnum = float(extnum[0]) + float(extnum[1])/10000
    
    print (extnum)
    
    totnum = totnum + extnum
    print(line, " ", extnum, "  ", totnum)

print (" Average for ", i , "items is: " , totnum/i)
print ("Done")


### Use the file name mbox-short.txt as the file name
##import re
##fname = raw_input("Enter file name: ")
##fh = open(fname)
##i = 0
##totnum = 0
##extnum = 0
##for line in fh:
##    if not line.startswith("X-DSPAM-Confidence:") : continue
##    i = i + 1    
##    extnum = re.findall('[0-9]+',line)
##    extnum = float(extnum[0]) + float(extnum[1])/10000
##    totnum = totnum + extnum
##    
##    
##print " Average spam confidence: " , totnum/i 
