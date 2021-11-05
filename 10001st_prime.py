
# Python
import itertools

def is_prime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
            
    return prime        
        
    

p = 0
for x in itertools.count(1):
    if is_prime(x):
        if p == 10001:
            print(x)
            break
        p +=1    

# Make sure you are using  int(n**0.5)+1 instead of n/2  otherwise it may takes 30 seconds or even more to run your codes.
# Also remember to use break command.
