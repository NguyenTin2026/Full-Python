# ## ITERATION ##
# *** Spyder Python Console History Log ***
 ## Program ##
 
where = input('You are in the lost forest. Go left or right?')
while where == 'right':
     where = input ('You are in the lost forest. Go left or right')
     print ('You out of the lost forest!')
     
# ## WAY 2 ##
n = 0
where = input('Go left or right?')
while where == 'right':
    n = n + 1
    print (n)
    where = input('Go left or right?')
print ('You go out!')     

# ## WAY 3 ##
n = 0
where = input('Go left or right?')
while where == 'right':
    n = n + 1
    if n > 2:
       print (':(')
    where = input('Go left or right?')
print ('You go out!')  

    
 
# ## while LOOPS WITH NUMBERS ##  
n = int(input('Enter a non-negative integer:'))
while n > 0:
    print ('x')
    n = n - 1
    
    
# ## EXAMPLE ##
while True:
    print ('noooooo') 
    
    
# ## RANGE ##
# ## fOR I IN RANGE (1,4,1): ##  print (i)
    i = 1,2,3
    print (1,2,3)
# ## fOR j IN RANGE (1,4,2): ##  print (j*2) 
    j = 1,3
    print (2,6)
# ## FOR ME IN RANGE (4,0,-1) ## print ('$'*me)
    me = (4,3,2,1)
    print ('$'*me)
    
# ## mysum ##
mysum = 0
for i in range (10):
    mysum += i      # means: mysym = mysum + i 
    print (mysum)

# ## EXAMPLE ABOUT mysum ##
# For example, if start=3 and end=5 then the sum should be 12.
mysym = 0
start = 3    # start = ?
end = 5      # end = ?
for i in range (start, end+1): # means: for i in range of (start, end+1):
    print ('i=',i)
    mysum += i
    print  (mysum)
    
    
# ## for LOOPS and range ##
# Factorial implemented with a while loop (seen this already) and a for loop 
x = 4
i = 1
factorial = 1
while i <= x:     # Uses a while loop
     factorial *= i 
     i += 1
     print (f'{x} factorial is {factorial}')    
     
     
x = 4
factorial = 1
for i in range (1, x+1, 1):  # Uses a for loop
     factorial *= 1
     print (f'{x} factorial is {factorial}')         
    
# ## even_num ##  
even_num = 0  
for i in range (5):
    # your code here
    # i  is 0,1,2,3,4
    if i%2==0:
           even_num += 1
print(even_num)    

s = 'demo loops - fruit loops'
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print ('There is an i or u')
        
# ## 
an_letters = 'aefhilmnorsxAEFHILMNORSX'
word = input('I will cheer for you! Enter a word:') 
times = int(input('Enthusiasm level (1-10):'))

for w in word:
    if w in an_letters:
        print ('Give me an' + w + ':' + w)
        print ('What does that  spell?')
        for i in range(times) :
            print (word,'!!!')

# ## You try it ##
s = 'abca'            
seen = ''
count = 0
for char in s:
   if char not in seen : 
    seen = seen + char
    print(len(seen))
    

# ## GUESS-AND-CHECK ##
## SQUARE ROOT with while loop ##
guess = 0
x = int(input('Enter an integer:'))
while guess**2 < x:
    guess = guess + 1 
    if guess **2 == x:
        print ('Square root of', x, 'is', guess)
    else:
        print (x, 'is not a perfect square')


# ## GUESS-AND-CHECK ##
## SQUARE ROOT with while loop for NEGATIVE NUMBER ##      
guess = 0
neg_flag = False
x = int(input('Enter a positive integer:'))
if x < 0:
    neg_flag = True
while guess **2 < x:
    guess = guess + 1
if guess **2 == x:
    print ('Square root of', x, 'is', guess)
else:
    print (x, 'is not a perfect square')
if neg_flag:
    print ('Just checking... did you mean', -x, '?')



# ## You try it ##
found = False
secret = 100
for i in range (1,11):
  # i is 1,2,3,4...11
   if i == secret:
    found = True
if not found:
    print('not found')
else: 
    print ('found')
    
    
    
# ## GUESS-AND-CHECK CUBE ROOT POSITIVE CUBES ##
cube = int(input('Enter an integer:'))
for guess in range(cube+1):
    if guess **3 == cube:
        print ('Cube root of', cube, 'is', guess)
        

# ## GUESS-AND-CHECK CUBE ROOT NEGATIVE CUBES ##
cube = int(input('Enter an integer:'))
for guess in range(abs(cube+1)):
    if cube < 0:
        guess = - guess
        print ('Cube root of', +str(cube)+ 'is' +str(guess))    



## ANOTHER EXAMPLE ##
for alyssa in range(1):
    for ben in range(1):
        for cindy in range(1):
            total = (alyssa + ben + cindy == 10)
            two_less = (ben == alyssa -2)
            twice = (cindy == 2*alyssa)
            if total and two_less and twice:
                print (f'Alyssa sold {alyssa} tickets')
                print (f'Ben sold {ben} tickets')
                print (f'Cindy sold {cindy} tickets')
                
                
## ANOTHER WAY ##
for alyssa in range(1001):
    ben = max(alyssa -20, 0)
    cindy = alyssa * 2
if ben + cindy + alyssa == 1000:
   print ('Alyssa sold' + str(alyssa) + 'tickets')
   print ('Ben sold' + str(ben) + 'tickets')
   print ('Ciindy sold' + str(cindy) + 'tickets')    



## BINARY NUMBER ##
X = 0 
for i in range(10):
    x += 0.1
print (x==1) 
print (x, 'is the same as', 10*0.1)
           
    