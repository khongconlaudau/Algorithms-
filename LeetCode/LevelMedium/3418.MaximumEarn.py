from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        """
        Bài toán: Robot di chuyển từ (0,0) đến (m-1,n-1) chỉ được đi xuống hoặc phải
        Robot có thể vô hiệu hóa tối đa 2 robber (ô có giá trị âm)
        
        Cách tiếp cận: DP 3D
        dp[i][j][k] = lợi nhuận tối đa tại ô (i,j) với k lần vô hiệu hóa đã dùng
        """
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] với k = 0,1,2 (số lần vô hiệu hóa đã sử dụng)
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Khởi tạo điểm bắt đầu
        if coins[0][0] < 0:
            dp[0][0][0] = coins[0][0]  # Không vô hiệu hóa
            dp[0][0][1] = 0           # Vô hiệu hóa robber đầu tiên
        else:
            dp[0][0][0] = coins[0][0]
        
        # Điền hàng đầu tiên (chỉ có thể đi từ trái sang phải)
        for j in range(1, n):
            for k in range(3):
                if dp[0][j-1][k] != -float('inf'):
                    if coins[0][j] < 0:
                        # Gặp robber
                        # Không vô hiệu hóa
                        dp[0][j][k] = max(dp[0][j][k], dp[0][j-1][k] + coins[0][j])
                        # Vô hiệu hóa (nếu còn lượt)
                        if k < 2:
                            dp[0][j][k+1] = max(dp[0][j][k+1], dp[0][j-1][k])
                    else:
                        # Không phải robber
                        dp[0][j][k] = max(dp[0][j][k], dp[0][j-1][k] + coins[0][j])
        
        # Điền cột đầu tiên (chỉ có thể đi từ trên xuống dưới)
        for i in range(1, m):
            for k in range(3):
                if dp[i-1][0][k] != -float('inf'):
                    if coins[i][0] < 0:
                        # Gặp robber
                        # Không vô hiệu hóa
                        dp[i][0][k] = max(dp[i][0][k], dp[i-1][0][k] + coins[i][0])
                        # Vô hiệu hóa (nếu còn lượt)
                        if k < 2:
                            dp[i][0][k+1] = max(dp[i][0][k+1], dp[i-1][0][k])
                    else:
                        # Không phải robber
                        dp[i][0][k] = max(dp[i][0][k], dp[i-1][0][k] + coins[i][0])
        
        # Điền phần còn lại của bảng
        for i in range(1, m):
            for j in range(1, n):
                for k in range(3):
                    # Từ ô trên (i-1, j)
                    if dp[i-1][j][k] != -float('inf'):
                        if coins[i][j] < 0:
                            # Gặp robber
                            # Không vô hiệu hóa
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                            # Vô hiệu hóa (nếu còn lượt)
                            if k < 2:
                                dp[i][j][k+1] = max(dp[i][j][k+1], dp[i-1][j][k])
                        else:
                            # Không phải robber
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                    
                    # Từ ô trái (i, j-1)
                    if dp[i][j-1][k] != -float('inf'):
                        if coins[i][j] < 0:
                            # Gặp robber
                            # Không vô hiệu hóa
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
                            # Vô hiệu hóa (nếu còn lượt)
                            if k < 2:
                                dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j-1][k])
                        else:
                            # Không phải robber
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
        
        # Trả về kết quả tối đa với bất kỳ số lần vô hiệu hóa nào
        return max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: Lưới đơn giản
    coins1 = [
        [0, 1, -1],
        [1, -2, 3],
        [2, -1, 0]
    ]
    print(f"Test 1: {sol.maximumAmount(coins1)}")  # Kỳ vọng: 5
    
    # Test case 2: Nhiều robber
    coins2 = [
        [10, -5, 2],
        [-3, 4, -1],
        [1, -2, 3]
    ]
    print(f"Test 2: {sol.maximumAmount(coins2)}")
    
    # Test case 3: Tất cả âm
    coins3 = [
        [-1, -2],
        [-3, -4]
    ]
    print(f"Test 3: {sol.maximumAmount(coins3)}")  # Có thể vô hiệu hóa 2 ô
