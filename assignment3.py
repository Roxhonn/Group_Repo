# Find all numbers which are multiple of 17, but not the multiple of 5, between 2000 and 2500?

for n in range(2000,2051):
 if n%17 == 0:
     if n%5 !=0:
       print (n)
         