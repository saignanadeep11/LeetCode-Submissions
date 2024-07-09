class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans=0.0
        timeSum=customers[0][0]
        for a,t in customers:
            if a>timeSum:
                timeSum=a
            timeSum+=t
            ans+=(timeSum-a)
            # print(timeSum,ans)
        return ans/len(customers)
        