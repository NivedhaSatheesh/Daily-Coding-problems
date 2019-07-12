# Daily-Coding-problems

# Problem 1

#Question: Given a list of numbers and a number k, return whether any two numbers from the list add up to k

#Function that returns True if any two numbers adds to k, else returns False. The array is first sorted.

def sum1(num,k):
    num_sorted=sorted(num)
    num2=num_sorted
    res=""
    i=0
    j=len(num)-1
    while i<len(num) and j>=0:
        value1=num_sorted[i]
        value2=num2[j]
        diff=value1+value2-k
        if diff==0:
            return True
            res="True"
        elif diff>0:
            j-=1
        elif diff<0:
            i+=1
    if res=="True":
        return True
    else:
        return False 
        
num=[10,15,3,7]
k=35
sum1(num,k)
