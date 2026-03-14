# 14. 最长公共前缀
# 简单

# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。


# 示例 1：

# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：

# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。

# 根据哈吉米给的详细思路自己手敲的狗屎代码：
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length1 = len(strs[0])
        length2 = len(strs)

        for i in range(length1):
            for j in range(1, length2):
                if (strs[j][i] != strs[0][i] or len(strs[j])-1 < i):  # 计算机是从左往右执行 or 判断的
                    break

        return strs[0][0:i]


1.  # IndexError: string index out of range
# 如果 strs[j] 的长度比较短（比如 $i=4$ 而 strs[j] 只有 3 个字符），计算机会先执行左边的 strs[j][i]。
# 这时候，因为它已经越界了，程序会直接崩溃报错，根本没机会运行右边的长度检查。
# 修正方法：先检查长度，再检查字符。

2.  # break 的作用范围：
# 问题所在：在 Python 中，break 只能跳出最近的一层循环（即 for j 那个循环）。
# 后果：当你发现不匹配时，break 只是停止了对其他字符串在当前位置 $i$ 的检查，但外层的 for i 循环还会继续往后跑。


# 哈继美给的标答：
  def longestCommonPrefix(self, strs: List[str]) -> str:
       # 边界检查：如果输入列表为空，直接返回空字符串
       if not strs:
            return ""

        # 以第一个字符串作为基准，长度为 length，字符个数为 count
        length = len(strs[0])
        count = len(strs)

        # 外层循环：对比第一个字符串的每一个字符索引 i
        for i in range(length):
            char = strs[0][i]

            # 内层循环：对比剩余的每一个字符串 strs[j]
            for j in range(1, count):
                # 检查两个条件（注意顺序！）：
                # 1. i 是否已经达到了 strs[j] 的长度（说明 strs[j] 更短，已经比完了）
                # 2. strs[j] 在第 i 个位置的字符是否不等于基准字符 char
                if i == len(strs[j]) or strs[j][i] != char:
                    # 一旦满足其一，说明公共前缀到此为止，直接返回
                    return strs[0][:i]

        # 如果整个循环都走完了还没触发 return，
        # 说明 strs[0] 里的每一个字符都在其他字符串里找到了对应的位置，所以最后直接返回 strs[0]。
        return strs[0]
# 若没有公共前缀，return strs[0][:0],而strs[0][0:0] 在 Python 中得到的结果正是空字符串 ""
#这个方法时间复杂度最优