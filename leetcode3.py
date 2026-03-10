# 88. 合并两个有序数组
# 尝试过
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 提示
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


# 示例 1：

# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
# 示例 2：

# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 解释：需要合并 [1] 和 [] 。
# 合并结果是 [1] 。
# 示例 3：

# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1
# 输出：[1]
# 解释：需要合并的数组是 [] 和 [1] 。
# 合并结果是 [1] 。
# 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.#  题目要求原地修改 modify in—place
        """
        count = 0
        for i in range(m, m+n):
            nums1[i] = nums2[count]
            count += 1
    nums1 = sorted(nums1)  # 依旧自己敲的狗屎代码   这里nums1指向了一个新对象，不是原地修改了
    # 原始的 nums1 列表对象在内存中并没有被改变

# 哈吉米给我优化的


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 将 nums2 复制到 nums1 的后半部分
        nums1[m:] = nums2  # 不用for循环速度快了好多 list[start:end] = iterable 是替换
        # 原地排序
        nums1.sort()


# 根据哈吉米给的最优算法的思路（从后往前填），自己敲的狗屎代码
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1


# 哈吉米给的正解
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 初始化三个指针
        p1 = m - 1      # nums1 的有效末尾
        p2 = n - 1      # nums2 的末尾
        p = m + n - 1   # nums1 的真正末尾（填空位用）

        # 只要两个数组都还没遍历完
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 特殊情况处理：
        # 如果 p1 先走完了，nums2 还有剩下的数，得把它们全搬过来
        # 如果 p2 先走完了，nums1 剩下的数已经在正确位置上了，不用动
        # 补充缺失的边界情况：如果 nums1 遍历完了，但 nums2 还有剩余
        # 直接把 nums2 剩下的元素拷贝到 nums1 的前面
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
