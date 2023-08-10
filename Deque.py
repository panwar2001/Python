from collections import deque 
    
# initializing deque 
de = deque([1,2,3]) 
    
# using append() to insert element at right end  
# inserts 4 at the end of deque 
de.append(4) 
    
# printing modified deque 
print ("The deque after appending at right is : ") 
print (de) 
    
# using appendleft() to insert element at left end  
# inserts 6 at the beginning of deque 
de.appendleft(6) 
# printing modified deque 
print ("The deque after appending at left is : ") 
print (de)
de.popleft();    
print ("The deque after pop at left is : ") 
print (de)
de.pop();
print ("The deque after pop at right is : ") 
print (de)

