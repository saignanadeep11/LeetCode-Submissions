class Solution:
    def minimumLength(self, s: str) -> int:
        arr=[0]*26
        for i in s:
            arr[ord(i)-ord('a')]+=1
        ans=0
        for i in arr:
            if i>2:
                if i%2==0:
                    ans+=2
                else:
                    ans+=1
            else:
                ans+=i
        return ans