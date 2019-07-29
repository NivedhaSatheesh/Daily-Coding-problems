# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
#return the minimum cost which achieves this goal
def minColorCost(array):
    result = []
    helper(array, result, 0, -1, 0, "")
    return min(result)

def helper(array, result, curr_house, prev_color, curr_cost, curr_sequence):
   if curr_house == len(array):
     result.append((curr_cost, curr_sequence))
     return
   for i in range(0, len(array[0])):
      if i != prev_color:
      helper(array, result, curr_house + 1, i, array[curr_house][i] + curr_cost, curr_sequence + str(i))

arr = [[1,2,3,4], [1,2,1,0], [6,1,1,5], [2,3,5,5]]
print(minColorCost(arr))
