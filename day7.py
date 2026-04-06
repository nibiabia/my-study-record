# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score

#     def get_score(self):
#         print(self.__score)

#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError("Invalid score!")


# Li = Student("Liyuting", 100)
# print(Li.name)
# Li.get_score()
# Li.set_score(99)
# Li.get_score()

# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender.lower() in ['male', 'female']:
            self.__gender = gender
        else:
            raise ValueError("Invalid!")


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
