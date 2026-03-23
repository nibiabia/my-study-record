双指针主要用于遍历数组，两个指针指向不同的元素，从而协同完成任务。


# 1.两数之和

# 给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

# 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数
# 假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。


# 示例 1：

# 输入：numbers = [1,2,4,6,10], target = 8
# 输出：[1,3]
# 解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。
# 示例 2：

# 输入：numbers = [2,3,4], target = 6
# 输出：[0,2]
# 示例 3：

# 输入：numbers = [-1,0], target = -1
# 输出：[0,1]

思路：使用双指针，一个指针指向值较小的元素，一个指针指向值较大的元素。指向较小元素的指针从头向尾遍历，指向较大元素的指针从尾向头遍历。

如果两个指针指向元素的和 sum == target，那么得到要求的结果；
如果 sum > target，移动较大的元素，使 sum 变小一些；
如果 sum < target，移动较小的元素，使 sum 变大一些。
数组中的元素最多遍历一次，时间复杂度为 O(N)。只使用了两个额外变量，空间复杂度为 O(1)。


根据上面给的思路自己敲得：


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, big = 0, len(numbers)-1
        while True:
            if numbers[small] + numbers[big] == target:
                return [small, big]
            elif numbers[small] + numbers[big] < target:
                small += 1
            else:
                big -= 1
        return [small, big]


# 1. 优化循环条件（防御性编程）
# 虽然题目说明了“假设数组中存在且只存在一对符合条件的数字”，所以用 while True: 不会报错。
# 但在实际工程开发中，或者遇到没有保证必定有解的变体题时，最好使用 while small < big: 。
# 这样当指针相遇还没有找到目标值时，循环能够安全退出，避免死循环越界。

# 2. 减少重复计算
# 在你的 if 和 elif 判断中，numbers[small] + numbers[big] 最多会被相加计算两次。
# 你可以把它提取成一个变量，每次循环只计算一次。虽然加法开销很小，但这是一个很好的代码习惯，能减少一次数组读取和加法运算。

# 3. 代码格式规范(PEP 8)
# 在逗号后和操作符两边加上空格，可以大大提高代码的可读性（例如 small, big = 0, len(numbers) - 1）。

看完优化建议后尝试自己改进：


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, big = 0, len(numbers)-1
        sum = numbers[small] + numbers[big]
        while small < big:
            if sum == target:
                return [small, big]
            elif sum < target:
                small += 1
            else:
                big -= 1


# 为什么会错？
# 在你的代码中，sum 只在循环开始前计算了一次。
# 进入 while 循环后，虽然你的指针 small 和 big 在不断移动（small += 1 或 big -= 1），但是 sum 的值并没有跟着更新，它一直固定在初始状态的值。


最终标答：


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, big = 0, len(numbers) - 1

        while small < big:
            # 把求和放在循环内部，每次指针移动后都重新计算！
            current_sum = numbers[small] + numbers[big]

            if current_sum == target:
                return [small, big]
            elif current_sum < target:
                small += 1
            else:
                big -= 1

        return []
