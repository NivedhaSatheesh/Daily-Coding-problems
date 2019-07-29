from collections import deque 
  
 
def printMax(arr, n, k): 
      
    
    Qi = deque() 
      
    # Process first k elements of array 
    for i in range(k): 
        
        # For every element, the previous smaller elements are useless 
        
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 
          
        # Add new element at rear of queue 
        Qi.append(i); 
     
     for i in range(k, n): 
          
        # The element at the front of the queue is the largest element of previous window
        print(str(arr[Qi[0]]) + " ", end = "") 
          
        # Remove the elements which are out of this window 
        while Qi and Qi[0] <= i-k: 
              
            # remove from front of deque 
            Qi.popleft()  
          
        # Remove all elements smaller than the currently being added element  
        
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 
          
        # Add current element at the rear of Qi 
        Qi.append(i) 
      
    # Print the maximum element of last window 
    print(str(arr[Qi[0]])) 
      
# Driver programm to test above fumctions 
if __name__=="__main__": 
    arr = [10, 5, 2, 7, 8, 7] 
    k = 3
    printMax(arr, len(arr), k) 
