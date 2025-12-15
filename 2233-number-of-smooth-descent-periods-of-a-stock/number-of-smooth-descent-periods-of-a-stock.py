class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = len(prices)
        adj = []
        cur = set()
    
    
        for i in range(1,len(prices)):
            cur.add(i-1)
            if prices[i-1] == prices[i] + 1:
                cur.add(i)
                if i == len(prices) -1:
                    adj.append(cur)
            else:
                adj.append(cur)
                cur = set()
            
        for i in adj:
            if len(i) <= 1:
                continue
            else:
                result += int((len(i) * (len(i)-1)) / 2)
                
  
        print(adj)
        return result

