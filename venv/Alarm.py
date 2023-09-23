# -*- coding: utf-8 -*-
# Будильник

from datetime import datetime
import playsound


class Alarm_:

    def __init__(self):
        print("init")


    def validate_time(self, alarms_time):  # Проверка правильности введенных данных
        if len(alarms_time) != 8:
            return "Неверный формат, попробуйте снова"
        else:
            if int(alarms_time[0:2]) > 23:
                return "Неверный формат часов, попробуйте снова"
            elif int(alarms_time[3:5]) > 59:
                return "Неверный формат минут, попробуйте снова"
            elif int(alarms_time[6:8]) > 59:
                return "Неверный формат секунд, попробуйте снова"
            else:
                return "ok"


    @classmethod
    def run_Alarm(cls):
        while True:
            alarm_time = input("Введите время будильника в следующем формате 'HH:MM:SS' \n Время будильника: ")
            validate = validate_time(alarm_time)
            if validate != "ok":
                print(validate)
            else:
                print(f"Будильник установлен на время {alarm_time}...\n")
                break
        alarm_hour = int(alarm_time[0:2])
        alarm_min = int(alarm_time[3:5])
        alarm_sec = int(alarm_time[6:8])
        while True:
            now = datetime.now()

            current_hour = now.hour
            current_min = now.minute
            current_sec = now.second

            if alarm_hour == current_hour and alarm_min == current_min and alarm_sec == current_sec:
                print("Подъем!")
                playsound.playsound(r"C:\Users\Lamar\PycharmProjects\Virtual Assistant\Alarm.mp3")
                break