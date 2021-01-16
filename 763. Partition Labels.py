class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        dic = {}
        for i in range(len(S)):
            if i not in dic:
                dic[S[i]] = i
            else:
                dic[S[i]] = max(dic[S[i]],i)
        
        right = dic[S[0]]
        idx = 0
        output = []
        
        while idx < len(S):
            if idx == right:
                output.append(right)
                if idx + 1 < len(S):
                    right = dic[S[idx+1]]
                    
            else:
                right = max(right,dic[S[idx]])
            idx += 1
            
        output.insert(0,-1)
        return [output[i]-output[i-1] for i in range(1,len(output))]
                
        
