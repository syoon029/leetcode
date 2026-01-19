class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 1. 2D Prefix Sum 배열 생성 (계산 편의를 위해 크기를 1 더 크게 잡음)
        sums = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                sums[r][c] = sums[r-1][c] + sums[r][c-1] - sums[r-1][c-1] + mat[r-1][c-1]
        
        ans = 0
        k = 1 # 현재 찾으려는 정사각형의 변의 길이
        
        # 2. 행렬을 탐색하며 최대 변의 길이 탐색
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                # (r, c)를 우측 하단으로 하는 변의 길이 k인 정사각형이 가능한지 확인
                while k <= min(r, c):
                    # 정사각형 합 계산
                    current_sum = sums[r][c] - sums[r-k][c] - sums[r][c-k] + sums[r-k][c-k]
                    
                    if current_sum <= threshold:
                        ans = k
                        k += 1 # 더 큰 정사각형이 있는지 확인하기 위해 k 증가
                    else:
                        break # 현재 위치에서 k보다 큰 정사각형은 불가능
                        
        return ans