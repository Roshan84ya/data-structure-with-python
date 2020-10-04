#question
"""


Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.




"""
#approoach
"""
here simply i've used dictionary(digit as the key and frequency as the value) and to store the frequency of each digit and calculated the max frequency from it
and then iterared through the dictionary took only those element which have frequency= maximum frequency and then i operated on our nums list and
finding the first occurance of that number and the last ocuurace of that digit
and the storing difference of maximum index and minimum index in our ans
and next time we will store the min(ans , difference of indexes)
space complexity O(n) time complexity O(k*n)
where n is number of element in the nums list and k is the numbers having same frequency

"""

#solution
from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        l=d.values()
        ma=max(l)
        ans=999999
        for i in d:
            if d[i]==ma:
                count=0
                
                for j in range(len(nums)):
                    if nums[j]==i and count==0:
                        idms=j
                        idmax=j
                        count=1
                    elif nums[j]==i:
                        idmax=j
                        
                        
                ans=min(ans,idmax - idms +1)
                #print(ans)
                if ans==ma:
                    break
        return ans
            
                        
        
        
        
