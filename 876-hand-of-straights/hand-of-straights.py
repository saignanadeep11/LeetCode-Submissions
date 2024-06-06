# import numpy as np
import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0: return False
        hand.sort()
        # arr=np.array(hand)
        # print(n,arr.reshape(groupSize,n//groupSize))
        d=collections.defaultdict(int)
        for i in range(0,n):
            d[hand[i]]+=1
        # print(d)
        for i in range(n//groupSize):
            s,e=0,0
            idx=0
            for j in (d.keys()):
                if idx>=groupSize:
                    break
                if d[j]>0:
                    if idx==0:
                        s=j
                    if idx==groupSize-1:
                        e=j
                    d[j]-=1
                    idx+=1
                
            # print(d)
            if e-s>=groupSize:
                return False
        if sum(d.values())>0:return False
        return True
       