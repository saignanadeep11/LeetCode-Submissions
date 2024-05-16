class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
      
      d={}
      
      def dp(i,j,flag):
        if(i>j):
          return 0
        if(i,j,flag) in d:
          return d[(i,j,flag)]
        res=0 if flag else math.inf 
        if(flag):
          res =max(res,nums[i]+dp(i+1,j,False),nums[j]+dp(i,j-1,False))
        else:
          res= min(res,dp(i+1,j,True),dp(i,j-1,True))
        d[(i,j,flag)]=res
        return res
      sec=sum(nums)
      one=dp(0,len(nums)-1,True)
      sec-=one
      # print(one,sec)
      return one>=sec
        