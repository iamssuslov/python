class Buffer:
    def __init__(self):
        self.lst = []

    def add_data(self, data):
        if len(self.lst) >= 5:
            print('Буфер переполнен')
            self.lst.clear()
            return

        self.lst.append(data)

    def get_data(self):
        print(f'Данные из буфера: {self.lst}')


if __name__ == '__main__':
    buffer = Buffer()

    buffer.add_data(1)
    buffer.add_data('2')
    buffer.add_data(3.0)

    buffer.get_data()
