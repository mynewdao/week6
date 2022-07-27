# st = ""
# print(dir(st))

# class ItSchool:
#     bootcamp = 15000
#     time = "8:30"
#
# kunduz = ItSchool()
# yasir = ItSchool()
# aliya = ItSchool()
# # print(ItSchool.__dict__)
# yasir.bootcamp = 1500
# yasir.free = True
#
# print(yasir.__dict__)
# print()
#
# print(aliya.__dict__)



#
#
# class CarCarolla:
#     wheels = 4
#     volume = 1.8
#     engine = "v6"
#     kuzov = "sedan"
#
#     def __init__(self, bumper, color, otdelka): #Конструктор или инициализатор
#         self.bumper = bumper
#         self.color = color
#         self.otdelka = otdelka
#
#
#
#
#     def get_info(self):
#         print(f"{self.bumper} , Цвет машины: {self.color}, "
#               f"Отделка машины: {self.otdelka}")
#
#     def change_otdelka(self, new_otdelka):
#         self.otdelka = new_otdelka
#
#
#
# mirlan = CarCarolla("m obves", "white", "alcantara")
# andrei = CarCarolla("v obves", "dark blue", "krokodile")
# mirlan.change_otdelka('alpaka')
# mirlan.get_info()
# andrei.get_info()


# print(mirlan.bumper)
# print(mirlan.color)
# print(mirlan.otdelka)
# print(andrei.__dict__)





# lessons_timur = {
#     "peremennye" : 100,
#     "loop": 87,
#     "func": 58,
# }
#
# lessons_nasyikat = {
#     "peremennye" : 100,
#     "loop": 90,
#     "func": 79,
# }
#
# lessons_aliya = {
#     "peremennye" : 100,
#     "loop": 78,
#     "func": 98,
# }

#
# class Student:
#     group = "python bootcamp 8:30"
#
#     def __init__(self, full_name, age, phone_number, lesson):
#         self.full_name = full_name
#         self.age = age
#         self.phone_number = phone_number
#         self.lesson = lesson
#         self.avg = 0
#
#     def get_info(self):
#         print(f"Группа {self.group} Зовут: {self.full_name} Возраст: {self.age} Номер телефона: {self.phone_number}"
#               f" Средний балл {self.avg}")
#
#
# # 1 metod
#     # def set_avg(self):
#     #     result = sum(self.lesson.values()) / len(self.lesson)
#     #     self.avg = round(result)
#
# #2 metod cherez cikl
#     def set_avg2(self):
#         count = 0
#         for i in self.lesson.values():
#             count += i
#         self.avg = round(count/len(self.lesson))
#
#
#
#
# timur = Student("Nasirdinov Timur", 18 , "+996555443322", lessons_timur)
# nasyikat = Student("Arzybaeva Nasyikat", 38 , "+996555888888", lessons_nasyikat)
# aliya = Student("Narynbekova Aliya", 18 , "+996555555555", lessons_aliya)
#
# timur.get_info()
# timur.set_avg2()
# # timur.set_avg()
# timur.get_info()
# # nasyikat.get_info()
# # nasyikat.set_avg()
# # nasyikat.get_info()
#
# # aliya.get_info()