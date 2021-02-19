import time 
  
def timex(function): 

    def wrapper(*args, **kwargs): 
        begin = time.time() 
        result = function(*args, **kwargs) 
        end = time.time() 
          
        print(function.__name__, end-begin) 
        return result 
    return wrapper
  
@timex
def power(x):
    y = 1
    for i in range(1,x+1):
        y = y*i
    print(y)


power(51080)
