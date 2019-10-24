def add(a,b):
    r = a + b
    print (r)

def add(a,b,c):
    r = a + b + c
    print (r)

add (3,4,7)


def add(datatype, *args): 
   
    if datatype =='int': 
        answer = 0
          
    if datatype =='str': 
        answer ='' 
  
    for x in args: 
  
        answer = answer + x 
  
    print(answer) 
  
# Integer 
add('int', 5, 6) 
  
# String 
add('str', 'Hello ', 'world') 