# 524. 通过删除字母匹配到字典里最长单词

# 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

# 如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。


# 示例 1：

# 输入：s = "abpcplea", dictionary = ["ale", "apple", "monkey", "plea"]
# 输出："apple"
# 示例 2：

# 输入：s = "abpcplea", dictionary = ["a", "b", "c"]
# 输出："a"

思路：通过删除字符串 s 中的一个字符能得到字符串 t，可以认为 t 是 s 的子序列，我们可以使用双指针来判断一个字符串是否为另一个字符串的子序列。

# 自己敲：


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        best_word = ""
        s_len = len(s)
        d_len = len(dictionary)
        for i in range(d_len):
            word = dictionary[i]
            w_len = len(word)
            q = 0
            p = 0
            while q < w_len and p < s_len:
                if s[p] == word[q]:
                    p += 1
                    q += 1
                else:
                    p += 1
            if (q == w_len and w_len > len(best_word)) or (q == w_len and w_len == len(best_word) and word < best_word):
                best_word = word
        return best_word


# 优化代码：
class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        best_word = ""
        s_len = len(s)

        # 直接遍历 dictionary 中的单词，比用索引 i 更 Pythonic
        for word in dictionary:
            w_len = len(word)
            p = 0  # 指向主串 s
            q = 0  # 指向字典词 word

            # 条件1：只要有一个指针走到底，就停止比对
            while p < s_len and q < w_len:
                if s[p] == word[q]:
                    q += 1  # 只有字符相等时，字典词的指针才往右移
                p += 1      # 主串的指针每次循环都必须往右移寻找下一个字符

            # 循环结束后，如果 q 走完了 word 的长度，说明匹配成功
            if q == w_len:
                # 条件2：更新 best_word 的逻辑
                if w_len > len(best_word):
                    best_word = word
                # 长度相同时，直接用 < 比较字母序
                elif w_len == len(best_word) and word < best_word:
                    best_word = word

        return best_word

# 思路优化：
# 与其每次找到一个匹配的单词后，再去辛苦地比较它是不是“最长且字母序最小”的，不如我们一开始就把整个字典按照“最优 -> 最次”的顺序排好队。

# 只要队伍排好了，我们从头开始找，第一个匹配成功的单词，就绝对是全局最优解！ 找到就可以直接 return（提前结束程序），


# 在 Python 中如何实现这种排序？
# Python 的 sort() 函数极其强大，它允许我们通过传入一个 key 来指定复杂的排序规则。我们可以用一个 lambda 匿名函数返回一个元组(Tuple) 来实现多级排序。


# Python
# dictionary.sort(key=lambda x: (-len(x), x))
# 这行代码是怎么工作的？
# 对于字典里的每一个单词 x，它会生成一个比较标准：(-len(x), x)。

# -len(x) 是什么意思？
# Python 默认是从小到大（升序）排序的。我们希望长度长的在前面，怎么办？加个负号！
# 比如单词 "apple" 长度是 5，"ale" 长度是 3。
# 加了负号后变成了 - 5 和 - 3。因为 - 5 < -3，所以 "apple" 会被排在 "ale" 前面。这就完美实现了长度降序。

# x 是什么意思？
# 当两个单词长度相同时（比如 "apple" 和 "apply"），-len(x) 都是 - 5，打成平手。
# 这时，Python 就会看元组的第二个元素，也就是单词 x 本身。
# Python 对字符串默认就是按字母序从小到大（升序）排列的。所以 "apple" 自然会排在 "apply" 前面。
class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        # 1. 对字典进行排序
        # 规则：先按长度降序排（-len(x)），长度相同的按字母序升序排（x）
        dictionary.sort(key=lambda x: (-len(x), x))

        s_len = len(s)

        # 2. 从头开始遍历排好序的字典
        for word in dictionary:
            w_len = len(word)
            p = 0  # 指向 s
            q = 0  # 指向 word

            # 双指针匹配逻辑
            while p < s_len and q < w_len:
                if s[p] == word[q]:
                    q += 1
                p += 1

            # 3. 见证奇迹的时刻
            if q == w_len:
                # 只要匹配成功，直接返回！
                # 因为排序规则保证了，我们第一个找到的，一定是符合条件的最优解
                return word

        # 如果遍历完字典都没找到，返回空字符串
        return ""
