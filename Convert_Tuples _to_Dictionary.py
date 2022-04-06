# initializing tuples
test_tup1 = ('GFG', 'is', 'best')
test_tup2 = (1, 2, 3)
  
# printing original tuples
print("The original key tuple is : " + str(test_tup1))
print("The original value tuple is : " + str(test_tup2))
  
# Using Dictionary Comprehension
# Convert Tuples to Dictionary
if len(test_tup1) == len(test_tup2):
    res = {test_tup1[i] : test_tup2[i] for i, _ in enumerate(test_tup2)}
  
# printing result 
print("Dictionary constructed from tuples : " + str(res))
