# 练习：创建一个简单的计算器类
# 要求：

# 创建一个名为 Calculator 的类
# 类中包含以下方法：
# __init__(self)：初始化方法
# add(self, a, b)：返回a + b的结果
# subtract(self, a, b)：返回a - b的结果
# multiply(self, a, b)：返回a * b的结果
# divide(self, a, b)：返回a / b的结果（注意除零错误）

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Divisor can not be zero!"
        else:
            return a / b


calc = Calculator()
print(calc.add(2, 3))
print(calc.divide(1, 0))
