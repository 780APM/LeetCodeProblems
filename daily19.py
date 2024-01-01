from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if g[child_i] <= s[cookie_j]:  # if the cookie can satisfy the child
                child_i += 1  # move to the next child
            cookie_j += 1  # move to the next cookie
        return child_i  # the number of content children

# test cases
sol = Solution()  # create an instance of the Solution class
g = [1,2,3]  # list of children
s = [1,1]  # list of cookies
print(sol.findContentChildren(g,s))  # call the method on the instance

g = [1,2]  # list of children
s = [1,2,3]  # list of cookies
print(sol.findContentChildren(g,s))  # call the method on the instance

g = [10,9,8,7]  # list of children
s = [5,6,7,8]  # list of cookies
print(sol.findContentChildren(g,s))  # call the method on the instance