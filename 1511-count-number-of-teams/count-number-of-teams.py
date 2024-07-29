class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans=0
        n=len(rating)
        for mid in range(n):
            left_small=0
            right_big=0
            for i in range(mid-1,-1,-1):
                if rating[mid]>rating[i]:
                    left_small+=1
            for i in range(mid+1,n):
                if rating[mid]<rating[i]:
                    right_big+=1
            ans+=left_small*right_big
            left_big=mid-left_small
            right_small=n-1-mid-right_big
            ans+=left_big*right_small
        return ans