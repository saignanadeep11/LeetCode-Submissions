class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in range(len(strs)):
            s="".join(sorted(strs[i]))
            arr=dic[s]
            arr.append(strs[i])
            dic[s]=arr
        return list(dic.values())