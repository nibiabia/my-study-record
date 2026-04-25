# # 多态的实现类型：
# # 1.继承+方法重写
# class Animal:
#     def speak(self):
#         pass


# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")


# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")


# class Cow(Animal):
#     def speak(self):
#         print("哞")


# def animal_sound(animal):
#     animal.speak()


# dog = Dog()
# cat = Cat()
# cow = Cow()
# animal_sound(dog)
# animal_sound(cat)
# animal_sound(cow)

# # 2.Duck Typing


# class Duck:
#     def fly(self):
#         print("鸭子飞")


# class Airplane:
#     def fly(self):
#         print("飞机飞")


# def let_fly(duck):
#     duck.fly()


# let_fly(Duck())
# let_fly(Airplane())

# 获取对象信息
print(type(123))
print(type('abc'))
print(type(None))
print(type([1, 2, 3]))
print(type(abs))
type(3.14)
type({"a": 1})
type(('a', 'b'))
type({1, 2})
type(True)


class Person:
    pass


p = Person()
print(type(p))  # <class '__main__.Person'>
