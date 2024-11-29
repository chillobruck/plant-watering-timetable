import datetime
import plyer
import getpass

from tools import Commands

file = Commands(url="C:/Users/user/Desktop/tools/plant_watering/v2/files/data.txt")
file.read_file()

date_today = datetime.datetime.now()
notification_plants = []

for plant_info in file.main_data.items():
    # e.g. items = ('Crasula', {'days_without_watering': 14, 'last_watering': '04.11.2024'})
    arr = plant_info[1]  # {'days_without_watering': 14, 'last_watering': '04.11.2024'}
    last_watering = datetime.datetime.strptime(arr['last_watering'], '%d.%m.%Y')

    name = plant_info[0]
    comparing_date = last_watering + datetime.timedelta(days=arr['days_without_watering'])

    if comparing_date <= date_today:
        notification_plants.append(name)

        if date_today - comparing_date > datetime.timedelta(days=1):
            file.change_setting(name, 'last_watering',
                                (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d.%m.%Y'))

# file.save_file()
notification_message = f'Пора полить растения. Нужно полить {", ".join(notification_plants).upper()}'

file.save_file()
if notification_plants:
    plyer.notification.notify(message=notification_message,
                              app_name='Напоминания',
                              title='Напоминание о поливе')

USER_NAME = getpass.getuser()
