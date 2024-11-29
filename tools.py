import datetime


class Commands:
    def __init__(self, url):
        self.main_data = {}
        self.url = url

    def read_file(self) -> None:  # Чтение файла
        file = open(self.url, 'r')
        try:
            file_text = file.read().split(';')
            file_text.pop(-1)

            main_data = {}
            for data in file_text:
                data = data.split('/')
                main_data[data[0]] = {'days_without_watering': int(data[1]),
                                      'last_watering': data[2]}
            self.main_data = main_data

        except IndexError:
            print('Неожиданная ошибка в чтении файла.')
            self.main_data = {}
        file.close()

    def save_file(self) -> None:
        file_final_text = ''
        for items in self.main_data.items():
            # e.g. items = ('Crasula', {'days_without_watering': 14, 'last_watering': '04.11.2024'})
            arr = items[1]  # {'days_without_watering': 14, 'last_watering': '04.11.2024'}
            name = items[0]
            days_without_watering = arr.get('days_without_watering')
            last_watering = arr.get('last_watering')

            file_final_text += f'{name}/{days_without_watering}/{last_watering};'

        file = open(self.url, 'w')
        file.write(file_final_text)
        file.close()

    def print_file(self) -> str:
        file_final_text = ''
        for items in self.main_data.items():
            # e.g. items = ('Crasula', {'days_without_watering': 14, 'last_watering': '04.11.2024'})
            arr = items[1]  # {'days_without_watering': 14, 'last_watering': '04.11.2024'}
            name = items[0]
            days_without_watering = arr.get('days_without_watering')
            last_watering = arr.get('last_watering')

            file_final_text += f'{name}/{days_without_watering}/{last_watering};'
        print(file_final_text.replace(';', '\n'))
        return file_final_text

    def add_element(self, name: str, days_without_watering: int) -> None:
        self.main_data[name] = {'days_without_watering': days_without_watering,
                                'last_watering': datetime.datetime.now().strftime('%d.%m.%Y')}

    def delete_element(self, name: str) -> None:
        try:
            self.main_data.pop(name)

        except KeyError:
            print('Plant not found')

    def change_setting(self, plant_name: str, setting: str, new_setting: str | int) -> None:
        try:
            if setting == 'name':
                print(self.main_data)
                self.main_data[new_setting] = self.main_data.pop(plant_name)
            else:
                self.main_data[plant_name][setting] = new_setting

        except KeyError:
            print('Plant not found')
