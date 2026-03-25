# 平方数之和

# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。


# 示例 1：

# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
# 示例 2：

# 输入：c = 3
# 输出：false

import math
思路：可以看成是在元素为 0~target 的有序数组中查找两个数，使得这两个数的平方和为 target，如果能找到，则返回 true，表示 target 是两个整数的平方和。

本题和 167. Two Sum II - Input array is sorted 类似，只有一个明显区别：一个是和为 target，一个是平方和为 target。本题同样可以使用双指针得到两个数，使其平方和为 target。

本题的关键是右指针的初始化，实现剪枝，从而降低时间复杂度。设右指针为 x，左指针固定为 0，为了使 02 + x2 的值尽可能接近 target，我们可以将 x 取为 sqrt(target)。

因为最多只需要遍历一次 0~sqrt(target)，所以时间复杂度为 O(sqrt(target))。又因为只使用了两个额外的变量，因此空间复杂度为 O(1)。

# 给的思路：自己敲


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        small = 1
        big = math.sqrt(c)
        while small < big:
            sum = small*small+big*big
            if sum == c:
                return True
            elif sum > c:
                big -= 1
            elif sum < c:
                small += 1
        return False


# 改错建议：
1.small 的初始值和循环条件题目要求的是非负整数，这意味着 $a$ 和 $b$ 可以是 $0$。
例如 $c = 4$ 时，可以拆解为 $0 ^ 2 + 2 ^ 2 = 4$。因此 small 应该从 0 开始，而不是 1。
$a$ 和 $b$ 也可以是同一个数，例如 $c = 2$ 时，$1 ^ 2 + 1 ^ 2 = 2$。所以 while 的循环条件必须包含等于的情况，即 while small <= big: 。
2.math.sqrt(c) 返回的是浮点数（比如 2.236）。作为指针的初始值，它必须是整数，所以需要向下取整。
为了让代码更简洁且避免额外导入模块，可以直接用 Python 的指数运算 int(c ** 0.5)。
另外，sum 是 Python 的内置保留字，最好不要用它做变量名，以防引起潜在的冲突。我们可以换成 current_sum

# 标答：


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        small = 0
        big = int(c ** 0.5)
        while small <= big:
            current_sum = small*small + big*big
            if current_sum == c:
                return True
            elif current_sum > c:
                big -= 1
            else:
                small += 1
        return False
