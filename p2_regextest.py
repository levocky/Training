import re
x = 'We just received $10.00 for cookies.'
x = 'TAG: <span class="comments">2</span>'
#y = re.findall('[0-9.]+',x)
y = re.findall('[0-9.]+',x)
y = int(y[0])

# + float(y[1])/10000
print y

#print int(y)
