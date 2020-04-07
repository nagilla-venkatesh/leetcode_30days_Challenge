"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution():
   def isHappy(self, n):
      """
      :type n: int
      :rtype: bool
      """
      return self.solve(n,{})


   def solve(self,n,visited):
      if n == 1:
         return True
      if n in visited:
         return False
      visited[n]= 1
      n = str(n)
      l = list(n)
      l = list(map(int,l))
      temp = 0
      for i in l:
         temp += (i**2)
      return self.solve(temp,visited)

"""
Solution:
To solve this, we will follow these steps −

Here we will use the dynamic programming approach, and solve this using recursion
Base case is, when n = 1, then return true
When n is already visited, return false
mark n as visited
n := n as string, l := list of all digits in n
temp := squared sum of all digits
return function recursively with parameter temp and visited list
"""