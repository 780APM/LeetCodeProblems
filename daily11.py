class Solution(object):
    def buyChoco(self, arr, key): # O(n^2)
        ans = float('inf') # float('inf') is the same as float('infinity'), largest possible value 
        for i in range(len(arr)): 
            for j in range(len(arr)): 
                if i != j: # exclude the current cell 
                    total = arr[i] + arr[j] # total cost
                    ans = min(ans, total) # minimum cost 

        fin = key - ans # final cost
        if(fin>=0): # if final cost is greater than or equal to 0
            return fin # return final cost 
        else: # otherwise 
            return key 
# test case
s = Solution() 
arr = [3, 4, 1, 9] # array of chocolate prices
key = 15 # key value 
print(s.buyChoco(arr, key)) # 12
