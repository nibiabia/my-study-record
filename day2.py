def sum(*args):  # 来实现一个可变参数的求和
    ax = 0
    for i in args:
        ax += i
    return ax


# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    count = 0

    def counter():
        nonlocal count
        count = count + 1
        return count
    return counter


# 使用方式：
c1 = make_counter()   # c1 现在是一个函数
print(c1())           # 1
print(c1())           # 2
print(c1())           # 3
