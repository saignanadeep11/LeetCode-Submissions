class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans=0
        n=len(people)
        l=0
        r=n-1
        while l<=r:
            if(l==r):
                ans+=1
                l+=1
                r-=1
            elif(people[l]+people[r]<=limit):
                ans+=1
                l+=1
                r-=1
            else:
                ans+=1
                r-=1
            # print(ans,l,r)
            
        return ans