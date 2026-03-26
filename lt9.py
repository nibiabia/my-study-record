# 反转字符串中的元音字母

# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。


# 示例 1：

# 输入：s = "IceCreAm"

# 输出："AceCreIm"

# 解释：

# s 中的元音是 ['I', 'e', 'e', 'A']。反转这些元音，s 变为 "AceCreIm".

# 示例 2：

# 输入：s = "leetcode"

# 输出："leotcede"
思路：
使用双指针，一个指针从头向尾遍历，一个指针从尾到头遍历，当两个指针都遍历到元音字符时，交换这两个元音字符。

为了快速判断一个字符是不是元音字符，我们将全部元音字符添加到集合 HashSet 中，从而以 O(1) 的时间复杂度进行该操作。

时间复杂度为 O(N)：只需要遍历所有元素一次
空间复杂度 O(1)：只需要使用两个额外变量

标答：


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        left = 0
        right = len(s) - 1
        s_list = list(s)
        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)


1.哈希集合（HashSet）是一种用来存储不重复元素的数据结构。在 Python 中，它对应的就是“集合”（set）。带有极速查找功能
2. 如果用列表（List）查找假设你把元音字母放在一个列表里：vowels_list = ['a', 'e', 'i', 'o', 'u']
当程序想要判断 'u' 是不是元音字母时（执行 'u' in vowels_list），它必须像查字典一样，从头开始挨个比对：是 'a' 吗？不是。是 'e' 吗？不是。...直到第 5 次才确认 'u' 在里面。
如果数据量有 100 万个，它最差的情况就要找 100 万次。这种挨个找的方式，在算法里叫作 $O(N)$ 的时间复杂度。
3.如果用哈希集合（HashSet）查找假设你把元音字母放在一个集合里：vowels_set = {'a', 'e', 'i', 'o', 'u'}
# 或者写成 vowels_set = set("aeiou")
当程序判断 'u' 是不是元音时（执行 'u' in vowels_set），它不需要挨个找。
哈希集合内部有一个“哈希函数”，它就像一个导航仪。只要你输入 'u'，它通过一个数学公式一算，瞬间就能得出结论：“'u' 存在，并且在几号位置”。
无论这个集合里装了 5 个字母，还是装了 500 万个数据，它“算一下就知道在不在”的过程几乎是不耗时的。
这种瞬间定位的能力，在算法里叫作 $O(1)$ 的时间复杂度。
4.尝试直接修改字符串（会报错）
如果你直接对字符串的某个位置进行修改，程序会直接崩溃：

text = "leetcode"

# 尝试把第一个字母改成大写的 'L'
text[0] = "L"

# 运行后会直接报错：
# TypeError: 'str' object does not support item assignment
转换为列表后修改（成功）
为了能够自由地替换里面的字母，我们需要用 list() 把这块“石碑”打碎，装进一个**“可变”（Mutable）**的列表里。
列表就像是一个带有很多独立小格子的收纳盒，你可以随时替换任何一个格子里的东西。
text = "leetcode"

# 第 1 步：变成列表
text_list = list(text)
# 此时 text_list 变成了：['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']

# 第 2 步：修改列表里的元素（完全合法）
text_list[0] = "L"
text_list[1] = "o"

# 此时 text_list 变成了：['L', 'o', 'e', 't', 'c', 'o', 'd', 'e']

# 第 3 步：拼回字符串
new_text = "".join(text_list)
# new_text 变成了："Loetcode"
