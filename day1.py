# 你好呀小婷！开始记录啦 today 是你的第一天xxii
# 今天学的是返回函数（返回一个函数，没错又是让你头大的高阶函数之一）

# 实现一个可变参数的求和
def lazy_sum(*args):
    total = 0

    def sum():
        nonlocal total
        for i in args:
            total += i
        return total
    return sum

# >> > f = lazy_sum(1, 3, 5, 7, 9)
# >> > f
# <function lazy_sum. < locals > .sum at 0x101c6ed90 >
# >> > f()
# 25
