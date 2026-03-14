# 找最长公共前缀
# 排序法 (Sorting) —— 针对面试的“黑科技”
# 如果你追求代码简洁度
# 排序后，整个数组中最不相似的两个字符串一定是第一个（最小）和最后一个（最大）。
# 逻辑推理： 如果第一个字符串和最后一个字符串在某个位置 $i$ 拥有相同的字符，那么夹在它们中间的所有字符串，在位置 $i$ 也必然是同一个字符

# #看了下哈吉米给我的代码：
# 自己真正敲的时候又有点不一样


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i != len(first) and i != len(last) and first[i] == last[i]:  # 这里
            i += 1
        return strs[0][:i]

# 哈吉米给我的解释
# # 1. 为什么 != 在这里是安全的？
# 在你的 while 循环里，i 是从 0 开始递增的（i += 1）。

# 因为 i 每次只加 1，所以它一定会正好撞到 len(first) 这个数值。

# 一旦 i == len(first)，i != len(first) 就会变为 False，循环停止。

# 2. 为什么通常推荐用 < ？
# 虽然 != 能跑通，但在工程实践中，程序员更习惯用 < ，原因有二：

# 防御性编程(Defensive Programming)： 如果你的循环逻辑很复杂，或者 i 在循环体内因为某种意外一次加了 2（跳过了那个相等的值）， != 就会变成死循环。而 < 是一种“保底”，只要 i 超过了长度，逻辑就会强行停止。

# 语义习惯： 在处理数组索引时， < 直观地表达了“在合法范围内”的意思。


# 标答：
def longestCommonPrefix(strs):
    if not strs:
        return ""

    # 1. 字典序排序
    strs.sort()

    # 2. 取出首尾两个字符串
    first = strs[0]
    last = strs[-1]
    i = 0

    # 3. 只比较这两个字符串
    # 注意防止索引越界
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]


# 这段代码在面试中非常讨喜，因为它展示了你对内置函数和逻辑简化的理解

# 打家劫舍2 没错，这是前面的动态规划问题的稍微变动，看完题目依旧不会。。。
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。


# 示例 1：

# 输入：nums = [2, 3, 2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 示例 2：

# 输入：nums = [1, 2, 3, 1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 3：

# 输入：nums = [1, 2, 3]
# 输出：3

# 根据评论区的思路，又回看了之前按摩师的解题步骤
# 其实就是把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。然后自己敲的漏洞百出的代码：
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev1 = 0
        for num in nums[0:n-2]:
            curr1 = max(prev1, prev2+num)
            prev1 = curr1
            prev2 = prev1
        prev22 = 0
        prev11 = 0
        for num in nums[1:n-1]:
            curr2 = max(prev11, prev22 + num)
            prev22 = prev11
            prev11 = curr2
        return max(prev1, prev11)


# 1.当你执行 prev1 = curr1 时，prev1 的值已经被覆盖成了最新的状态。接着你执行 prev2 = prev1，这就导致 prev2 也变成了最新的状态，而不是上一轮的 prev1。这会完全扰乱动态规划的状态转移。
# 正确写法：必须先更新 prev2，再更新 prev1
# 2.Python 的切片 nums[start:end] 是左闭右开的（包含 start，不包含 end）
# 3.在你的代码中，计算单排房屋最高金额的逻辑被重复写了两遍（分别用 prev1 和 prev11 相关的变量）。在编程中，这不太符合 DRY (Don't Repeat Yourself) 原则
# 改进建议：你可以把这段计算单排房屋的逻辑提取成一个内部的辅助函数 robRange，这样不仅代码看起来非常清晰，而且只需维护一处逻辑，不容易出错

# 改进：
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def robrange(start, end):
            prev1 = 0
            prev2 = 0
            for num in nums[start:end]:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(robrange(0, n-1), robrange(1, n))


# 1.由于切片的存在，整体的空间复杂度又被拉回到了 O(N)
# 改进方案：直接通过索引遍历
# 为了达到真正的 O(1)空间复杂度，我们可以直接使用 range(start, end) 生成索引，并通过索引去访问原数组
# 2.命名规范： Python 中函数名通常推荐使用小写字母加下划线的 snake_case 风格，比如 rob_range
# 3.优雅的变量交换： Python 支持多元赋值，你可以用一行代码完成状态的滚动更新，这在写动态规划时非常优雅


# 完美标答：
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rob_range(start, end):
            prev1 = 0
            prev2 = 0
            # 使用索引遍历，避免切片产生额外空间，实现真正的 O(1) 空间复杂度
            for i in range(start, end):
                curr = max(prev1, prev2 + nums[i])
                prev1, prev2 = curr, prev1  # 先计算等号右边的所有值，然后再同时赋给等号左边
            return prev1

        return max(rob_range(0, n - 1), rob_range(1, n))


# # 217. 存在重复元素
# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

# 示例 1：

# 输入：nums = [1, 2, 3, 1]

# 输出：true

# 解释：

# 元素 1 在下标 0 和 3 出现。

# 示例 2：

# 输入：nums = [1, 2, 3, 4]

# 输出：false

# 解释：

# 所有元素都不同。

# 示例 3：

# 输入：nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

# 输出：true


# 哈吉米给的思路：直接把整个数组转换为一个「集合（Set）」。
# 因为集合天生会自动去重，转换完成后，只需比较原数组的长度和新集合的长度。
# 如果长度不相等，说明一定有重复元素被去掉了。
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)
        if (len(sets) == len(nums)):
            return False
        else:
            return True  # 我敲得狗屎代码


# 建议：
# 1.当前： if (len(sets) == len(nums)):
# 改进： if len(sets) == len(nums):    代码风格更Pythonic
# 2.遇到 if 判断条件: return False else: return True 这种结构时，其实可以直接返回判断条件本身（或者它的反面）
# 直接写成 return len(sets) != len(nums) 即可

# 但从纯算法逻辑来看：它必须把整个数组完整转换成一遍集合
# 进一步的优化版：利用哈希表（或者集合 Set）查找速度极快的特性，手动遍历，边查边存
最终标答：


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()          # 改名为 seen，意为“已经看过的数字”
        for num in nums:
            if num in seen:
                return True   # 只要在“看过的数字”里，就提前终止
            seen.add(num)     # 没看过，就加到“看过的数字”里
        return False
