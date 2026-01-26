class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        if len(arr) == 2:
            return [[arr[0],arr[1]]]

        result = []
        min_diff = float('inf')

        for i in range(len(arr)-1):
            min_diff = min(min_diff,arr[i+1] - arr[i])
            print(min_diff)
        
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i],arr[i+1]])
        
        
        return result

