class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2Arr=[0]*26
        for i in words2:
            arr=[0]*26
            for j in range(len(i)):
                arr[ord(i[j])-ord('a')]+=1
            for j in range(26):
                word2Arr[j]=max(word2Arr[j],arr[j])
        ans=[]
        for i in range(len(words1)):
            arr=[0]*26
            for j in range(len(words1[i])):
                arr[ord(words1[i][j])-ord('a')]+=1
            bool=True
            for j in range(26):
                if word2Arr[j] and word2Arr[j]>arr[j]:
                    bool=False
                    break
            if bool:
                ans.append(words1[i])

        return ans