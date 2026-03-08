# ; 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# ; 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

 class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         count1 = 0
         for i in nums:
             count1 += 1
             for j in nums:
                if i + j == target：        自己敲的shi代码
# ; 题目要求你交出的是这两个数字的**“数组下标”。
# ; 但是，当你写 for i in nums: 的时候，i 拿到的是数字本身（比如例子1里的 2, 7, 11, 15），而不是它们的编号。
# ; 虽然你聪明地想用 count1 去自己数编号，但这在多重循环里非常容易算错

# ; 为了既拿到位置编号，又不重复取数字，我们需要用到 Python 里的黄金搭档：range() 和 len()。


class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         length = len(nums)
         for i in range(length):
             for j in range(i+1, length):
                 if nums[i] + nums[j] == target:
                     return [i, j]
 时间复杂度 $O(n^2)$

# ; 2. 核心“抓人”逻辑提示
# ; 想象一下，你拿着通缉令（target = 9）去排查队伍（nums = [2, 7, 11, 15]）：

# ; 第 1 步： 你遇到了第一个人 nums[0] 是 2。

# ; 你心里算了一下：我需要抓的人是 9 - 2 = 7。

# ; 你翻开你的小本子 record_book 查一下，7 登记过吗？

# ; 本子是空的，没找到。于是你把当前的 2 和它的位置 0 登记在本子上：record_book[2] = 0。 然后继续往下走。

# ; 第 2 步： 你遇到了第二个人 nums[1] 是 7。

# ; 你心里算了一下：我需要抓的人是 9 - 7 = 2。

# ; 你翻开小本子查一下，2 登记过吗？

# ; 在！ 你刚刚在第一步把它记下来了。

# ; 这时候你就集齐了！当前的人位置是 1，本子上记录的 2 的位置是 0（通过 record_book[2] 可以提取出来）。直接交卷：[record_book[2], 1]。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record_book = {}
        length = len(nums)

        for i in range(length):
            # 1. 先算一下我们需要抓的人是谁
            wanted = target - nums[i]

            # 2. 查本子：这个目标人物之前登记过吗？
            if wanted in record_book:
                # 3. 如果查到了！返回 [本子上记的那个人的位置, 当前这个人的位置 i]
                return [record_book[wanted], i]

            # 4. 如果没查到，说明当前的数字还没遇到有缘人，把它和它的位置记到本子上
            record_book[nums[i]] = i


# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 请必须使用时间复杂度为 O(log n) 的算法。


# 示例 1:

# 输入: nums = [1, 3, 5, 6], target = 5
# 输出: 2
# 示例 2:

# 输入: nums = [1, 3, 5, 6], target = 2
# 输出: 1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        middle_index = (length - 1)/2
        middle_num = nums[middle_index]
        if target == middle_num:
            return middle_index
        elif target > middle_num:
            for i in range(middle_index + 1, length):
                if target == nums[i]:
                    return i
            nums.append(target)
            sorted(nums)
            return
        else:
            for i in range(middle_index):
                if target == nums[i]:
                    return i   #自己第一次敲的史代码
# 改进： Python 里求整数商（丢弃小数部分）要用双斜杠 //。

# 陷阱 2：“砍半”只砍了一次（第 9 行和第 16 行）
# 这是导致你代码变长、变乱的最核心原因！
# 你的思路是：“我先从中间劈一刀，如果目标比中间大，我就去右边找。”
# 但是，你是怎么在右边找的呢？你用了一个 for 循环！
# 👉 改进： 我们不仅要砍第一刀，我们还要一直砍下去，直到找到为止。
# 所以我们不能用 for 循环，而是要用 while 循环配合移动左右边界来实现。
# 陷阱 3：过于老实地“排队”（第 12 - 14 行）题目说“如果不存在，返回它将会被按顺序插入的位置”。
# 你用了 nums.append(target) 把数字真的塞进去了，又用 sorted() 重新排了个序。
# 但在编程里，修改数组和重新排序都是非常耗费时间的（极其破坏 $O(\log n)$ 的要求）。
# 题目只是问你**“它该坐在哪个位置的编号”**，你不需要真的把它塞进队伍里。
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 一开始，搜索范围是整个数组
        left = 0
        right = len(nums) - 1
        
        # 只要左边界还没越过右边界，我们就继续“砍半”
        while left <= right:
            # 找到当前范围的中间点（这就相当于你的 middle_index，用 // 保证是整数）
            middle = (left + right) // 2
            
            # 剧本 1：刚好中间这个就是要找的
            if nums[middle] == target:
                return middle
                
            # 剧本 2：目标比中间的数字大，说明目标在右半边！
            elif target > nums[middle]:
                # 【你的任务】：思考一下，怎么把搜索范围缩小到右半边？
                # 提示：右边界 right 不动，左边界 left 应该移动到哪里？
                pass 
                
            # 剧本 3：目标比中间的数字小，说明目标在左半边！
            else:
                # 【你的任务】：思考一下，怎么把搜索范围缩小到左半边？
                # 提示：左边界 left 不动，右边界 right 应该移动到哪里？
                pass
                
        # 终极魔法：如果 while 循环结束了还没找到，说明 target 不在数组里。
        # 极其巧妙的是，此时 left 指针所停留在的位置，刚好就是 target 应该插入的位置！
        return left
    #此时此刻 left 指针停下的位置，绝对、刚好就是这个目标数字如果想加塞进来，应该占据的那个位置！
    1