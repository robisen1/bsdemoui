class TableHeader(Label):
    pass

class DeviceInfo(Label):
    pass


class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.get_devicedata()
        self.display_data()

    def get_devicedata(self):
        self.data = [
            {'LRT' : '8.243','Type' :'DJI Mavic' ,'STR': '4.39'},
            {'LRT': '5.243', 'Type': 'Parrot BeBop', 'STR' : 'Close'},
            {'LTR' : '2','Type' : 'Parrot Sumo', 'STR' : '2.3555'}
        ]

    def display_data(self):
        self.clear_widgets()
        for i in xrange(len(self.data)):
            row = self.create_header()
            row = self.create_player_info(i)
            for item in row:
                self.add_widget(item)

    def create_header(self):
        first_column = TableHeader('Last Recived Time(Sec)')
        second_column = TableHeader('Classification Type')
        third_column = TableHeader('Session Time Remaining (Sec)')
        return [first_column, second_column, third_column]

    def create_player_info(self, i):
        first_column = DeviceInfo(text=self.data[i]['name'])
        second_column = DeviceInfo(text=self.data[i]['score'])
        third_column = DeviceInfo(text=self.data[i]['car'])
        return [first_column, second_column, third_column]
