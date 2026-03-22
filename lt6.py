移除元素

# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

# 假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

# 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
# 返回 k。


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                for j in range(i+1, len(nums)):
                    nums[j-1] = nums[j]
                n -= 1
            else:
                i += 1
                k += 1
        return k


# 刚开始敲得代码 O(n**2)   有错误：数组边界未更新
你的核心思路是：遇到等于 val 的元素，就把后面的元素全部往前移一位将它覆盖。这个想法很直观，
但在 Python 中直接原地修改列表时，len(nums) 并不会随着你的覆盖而变小。


方法一：修复你现有的思路(暴力移位)
如果你想坚持原本“整体往前挪”的思路，你需要引入一个变量来记录**“当前数组的有效长度”**，并在每次移位后把这个长度减 1，循环的条件也要随之改变：

Python


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)  # 用一个变量记录有效长度
        i = 0
        while i < n:  # 遍历到有效长度即可
            if nums[i] == val:
                for j in range(i + 1, n):
                    nums[j - 1] = nums[j]
                n -= 1    # 关键：移位后，有效长度减 1。注意这里 i 不加 1，因为要继续检查移过来的新元素
            else:
                i += 1
        return n  # 最终 n 就是留下来的元素个数


方法二：更优的思路 —— 快慢双指针(推荐)你现在的做法每次遇到目标值都要把后面所有元素移动一遍，时间复杂度是 $O(n ^ 2)$。
更标准、高效的解法是使用双指针，只需要遍历一次数组，时间复杂度 $O(n)$。
快指针(fast)：负责寻找那些不需要被移除的元素。慢指针(slow)：指向下一个要用来存放新元素的位置。
 def removeElement(self, nums: List[int], val: int) -> int:
      slow = 0  # 慢指针，记录当前有多少个不等于 val 的元素

       for fast in range(len(nums)):
            # 如果快指针找到一个不是 val 的元素，就把它丢到慢指针的位置
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        # 遍历结束后，slow 的值正好就是不等于 val 的元素的数量 k
        return slow
建议： 在力扣中处理这类“数组原地移除/修改”的题目，双指针法是最常用也是最考察的核心思想，建议重点掌握方法二。
