fh = open('palindrome.txt','w')
n = int(input("Enter a number: ")) 
sum = 0  
temp = n 
while(n>0): 
    digit = (n%10) 
    sum = sum*10 + digit 
    n = n//10 
 
if(sum==temp): 
    fh.write("It's a Palindrome.") 
else: 
    fh.write("It's not a Palindrome.")
fh.close()