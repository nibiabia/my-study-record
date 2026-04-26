# 归并两个有序数组
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


# 示例 1：

# 输入：nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
# 输出：[1, 2, 2, 3, 5, 6]
# 解释：需要合并[1, 2, 3] 和[2, 5, 6] 。
# 合并结果是[1, 2, 2, 3, 5, 6] ，其中斜体加粗标注的为 nums1 中的元素。
# 示例 2：

# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 解释：需要合并[1] 和[] 。
# 合并结果是[1] 。
# 示例 3：

# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1
# 输出：[1]
# 解释：需要合并的数组是[] 和[1] 。
# 合并结果是[1] 。
# 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

原先自己敲得代码：


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        if p1 == -1:
            while p >= 0:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1


核心优化思路：只需要盯紧 nums2
我们从后往前合并时，会出现两种结束情况：

p1 先走完（小于 0）： 说明 nums1 的元素已经全部排到末尾了，此时前面空出来的位子，直接把 nums2 剩下的元素填进去就行。

p2 先走完（小于 0）： 这是最理想的情况。说明 nums2 里的元素已经全合并好了，而 nums1 剩下的元素本来就好好地待在数组的最前面，它们不需要进行任何移动！

结论： 只要 nums2 里的元素还没搬完（p2 >= 0），我们就得继续排；一旦 nums2 搬完了，合并就自然结束了。


最终标答：


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p, p1, p2 = m + n - 1, m - 1, n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
