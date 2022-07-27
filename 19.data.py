#datetime
import datetime
from datetime import timedelta #позволяет использовать инт тайп в дате через timedelta()

# now = datetime.datetime.now()
# # print(now)
#
#
# date_2 = datetime.date(2022, 5, 25)
# time_2 = datetime.time(13,30)
# all_data = datetime.datetime.combine(date_2, time_2)
# print(now.strftime("%a")) #отображает часть слова
# print(now.strftime("%A")) #отображает полностью
# print(date_2)
# print(time_2)
# print(all_data)

# new_time = now.date() - date_2
# print(new_time)


#
# now = datetime.datetime.now()
# days = 30
# end_date = now + timedelta(days)
# print(end_date)


date = datetime.date(2022, 6, 22)
etap1 = 30
etap2 = 20
etap3 = 50
#  1 способ ===============================================================================================
# stage1 = date + timedelta(etap1)
# print(stage1, "Конец 1 этапа")
#
# stage2 = stage1 + timedelta(etap2)
# print(stage2, "Конец 2 этапа")
#
# stage3 = stage2 + timedelta(etap3)
# print(stage3,"Конец 3 этапа")
#==========================================================================================================
#2 способ

# year = int(input("Year: "))
# month = int(input("Month: "))
# day = int(input("Day: "))
# data = datetime.datetime(year, month, day)
#
# def devide_time(date):
#     stage1 = date + timedelta(30)
#     stage2 = stage1 + timedelta(20)
#     stage3 = stage2 + timedelta(50)
#     print(f"{stage1} Конец 1 этапа!")
#     print(f"{stage2} Конец 2 этапа!")
#     print(f"{stage3} Конец 3 этапа!")
#     return stage1, stage2, stage3 #если много переменных то возвращает в ТЮПЛ, если один то datetime ТИП
# devide_time(data)


#
# lists = ['ps4', 'dota', 'll', 'warcraft']
#
# def arenda(rent, product):
#     now = datetime.datetime.now()
#     item_time = now + timedelta(rent)
#     print(f"{product} должны вернуть {item_time}")
#     return {
#         f"{product}" : item_time
#     }
#
# arenda(2,lists[0])
#
# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M"))
# #strp из строки в дату


strin = 