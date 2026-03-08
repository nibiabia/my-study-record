# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

# 注意：本题相对原题稍作改动


# 示例 1：

# 输入： [1,2,3,1]
# 输出： 4
# 解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
# 示例 2：

# 输入： [2,7,9,3,1]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
# 示例 3：

# 输入： [2,1,4,5,3,1,1,3]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

class Solution:
    def massage(self, nums: List[int]) -> int:
        length = len(nums)
        match length:
            case 0:
                return 0
            case 1:
                return nums[0]
            case 2:
                if nums[0] >= nums[1]:
                    return nums[0]
                else:
                    return nums[1]
            case length if length > 2:  # 根据哈吉米给的思路自己敲的史代码


class Solution:
    def massage(self, nums: List[int]) -> int:
        length = len(nums)

        match length:
            case 0:
                return 0
            case 1:
                return nums[0]
            case 2:
                # 顺手优化：直接返回两个里面的最大值，不用写 if-else
                return max(nums[0], nums[1])
            case _:
                # 兜底情况：长度大于 2 的时候走这里

                # 1. 准备空白账本
                # *：在 Python 里，如果把它用在列表上，它就不是数学里的乘号了，而是**“重复操作符”**（复制）。
                dp = [0] * length

                # 2. 填入前两天的已知最优解
                dp[0] = nums[0]
                dp[1] = max(nums[0], nums[1])

                # 3. 开启循环，从第 3 天（索引是 2）开始往后算
                for i in range(2, length):
                    # 核心转移方程：今天最优解 = max(昨天最优解, 前天最优解 + 今天时长)
                    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

                # 4. 账本最后一页的记录，就是整个数组的最优解
                return dp[-1]


# 最终优化：
class Solution:
    def massage(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        for num in nums:
            curr = max(prev1, prev2+num)
            prev2 = prev1
            prev1 = curr
        return prev1


1
