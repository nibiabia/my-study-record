import functools
import time
1.请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        # perf_counter() 是现代Python中测量时间间隔的最佳选择，因为它提供了最高的可用精度
        start_time = time.perf_counter()
        fn(*args, **kw)  # 你在第 10 行执行了 fn(*args, **kw)，这确实运行了原函数。


# 但是，你没有接收这个函数的返回值，也没有在 wrapper 的最后将其 return 出去。

# 因此，wrapper 默认返回了 None
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
        print(f"{fn.__name__} executed in {execution_time:.2f}ms")
    return wrapper


# 测试


@metric
def fast(x, y):
    time.sleep(0.0012)  # 让程序暂停1.2毫秒
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 修改
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.perf_counter()
        result = fn(*args, **kw)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
        print(f"{fn.__name__} executed in {execution_time:.2f}ms")
        return result
    return wrapper
# 测试


@metric
def fast(x, y):
    time.sleep(0.0012)  # 让程序暂停1.2毫秒
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


2.请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志


def decorator(fn):
    """装饰器，在函数调用前后打印日志"""
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print(f"begin call {fn.__name__}")
        result = fn(*args, **kw)
        print(f"end call {fn.__name__}")
        return result
    return wrapper


3.能否写出一个@log的decorator，使它既支持：


@log
def f():
    pass


又支持：


@log('execute')
def f():
    pass


def log(arg):
    if not isinstance(arg, str):
        func = arg

        def wrapper(*args, **kw):
            print(f"call {func.__name__}()")
            result = func(*args, **kw)
            return result
        return wrapper
    else:
        def decorator(func):
            def wrapper(*args, **kw):
                print(f"call {func.__name__}()")
                result = func(*args, **kw)
                return result
            return wrapper
        return decorator
