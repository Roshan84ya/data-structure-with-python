"""
135. Candy
Hard

978

165

Add to List

Share
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candy=[1]*len(ratings)
        for i in range(1,n):
            if ratings[i-1]<ratings[i] and candy[i-1]>=candy[i]:
                candy[i]+=candy[i-1]
        ratings=ratings[::-1]
        candy=candy[::-1]
        for i in range(1,n):
            if ratings[i-1]<ratings[i] and candy[i-1]>=candy[i]:
                candy[i]+=candy[i-1]
                if abs(candy[i]-candy[i-1])>1:
                    candy[i]=candy[i-1]+1
       
            
        print(candy[::-1])
            
        return sum(candy)
                
        
            
        
        
