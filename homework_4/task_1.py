from datetime import datetime

if __name__ == "__main__":
    current_date_time = datetime.now()
    print("Текущий день и время:", current_date_time)

    date1 = datetime(2020, 1, 1)
    date2 = datetime(2023, 10, 10)
    delta = date2 - date1
    print("Разница между двумя датами:", delta)

    date_string = "2023-10-10 15:00:00"
    date_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print("Сконвертированный строковый объект в datetime:", date_obj)
