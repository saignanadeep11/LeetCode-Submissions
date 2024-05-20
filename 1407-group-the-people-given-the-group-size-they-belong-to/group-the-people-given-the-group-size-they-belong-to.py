class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group={}
        n=len(groupSizes)
        ans=[]
        for i in range(n):
            if groupSizes[i] in group:
                arr=group[groupSizes[i]]
                if(len(arr)>=groupSizes[i]):
                    ans.append(arr)
                    group[groupSizes[i]]=[]
                group[groupSizes[i]].append(i)
            else:
                group[groupSizes[i]]=[i]
        for k in group:
            if len(group[k])>0:
                ans.append(group[k])
        # print(group)
        return ans