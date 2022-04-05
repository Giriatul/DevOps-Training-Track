# Python3 code to demonstrate working of 
# Convert key-value String to dictionary
# Using map() + split() + loop
  
# initializing string
test_str = 'gfg:1, is:2, best:3'
  
# printing original string
print("The original string is : " + str(test_str))
  
# Convert key-value String to dictionary
# Using map() + split() + loop
res = []
for sub in test_str.split(', '):
    if ':' in sub:
        res.append(map(str.strip, sub.split(':', 1)))
res = dict(res)
  
# printing result 
print("The converted dictionary is : " + str(res)) 
