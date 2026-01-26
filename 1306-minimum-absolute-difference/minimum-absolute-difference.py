class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        if len(arr) == 2:
            return [[arr[0],arr[1]]]

        result = []
        min_diff = float('inf')

        for i in range(len(arr)-1):
            curr_diff = arr[i+1] - arr[i]

            if curr_diff == min_diff:
                result.append([arr[i], arr[i+1]])
            else:
                if curr_diff < min_diff:
                    result = [[arr[i], arr[i+1]]]
                    min_diff = curr_diff
                    
                
        return result

