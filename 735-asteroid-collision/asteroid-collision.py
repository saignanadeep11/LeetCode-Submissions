class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        n=len(ast)
        p1=0
        ans=[]
        while(p1<n):
            if not ans:
                ans.append(ast[p1])
                p1+=1
                continue
            k=ans.pop()
            if k<0:
                ans.append(k)
                ans.append(ast[p1])
                p1+=1
            elif ast[p1]>0:
                ans.append(k)
                ans.append(ast[p1])
                p1+=1
            elif ast[p1]==k:
                p1+=1
                continue
            else:
                if k>abs(ast[p1]):
                    ans.append(k)
                    p1+=1
                    continue
                elif k==abs(ast[p1]):
                    p1+=1
                    continue
                while(k<abs(ast[p1])):
                    if not ans:
                        ans.append(ast[p1])
                        p1+=1
                        break
                    k=ans.pop()
                    if k<0:
                        ans.append(k)
                        ans.append(ast[p1])
                        p1+=1
                        break
                    elif k==abs(ast[p1]):
                        p1+=1
                        break
                    elif k>abs(ast[p1]):
                        ans.append(k)
                        p1+=1
                        break
        return ans