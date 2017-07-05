from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.get_tableheaders()
        self.get_devicedata()
        self.display_data()

    def get_tableheaders(self):
        self.tabledata = [
            {'LRT': 'Last Recived Time', 'Type': 'Classification Type', 'STR': 'Session Time Remaining'},
        ]

    def get_devicedata(self):
        self.data = [
            {'LRT': '8.243', 'Type': 'DJI Mavic', 'STR': '4.39'},
            {'LRT': '5.243', 'Type': 'Parrot BeBop', 'STR': 'Close'},
            {'LRT': '7.11', 'Type': 'Parrot Ebee', 'STR': 'Close'},
            {'LRT': '5.3', 'Type': 'Parrot DISCO', 'STR': '11.12'},
            {'LRT': '3.20', 'Type': 'Yuneec Typhoon', 'STR': '2.13'},
            {'LRT': '5.44', 'Type': 'Yuneec', 'STR': '5.23'},
            {'LRT': '1.12', 'Type': 'DJI Pro 4', 'STR': '1.10'},
            {'LRT': '2', 'Type': 'Parrot Sumo', 'STR': '2.3555'}
        ]

# assembles the items to be pushed into the gridlayout widget


    def display_data(self):
        self.clear_widgets()
        print(myappstate)
        for myi in xrange(len(self.tabledata)):
            print("display data method was run")
            myrow = self.create_header(myi)
            for myitem in myrow:
                self.add_widget(myitem)

        if myappstate == True:
            for i in xrange(len(self.data)):
                row = self.create_player_info(i)
                #add all the items to the widget
                for item in row:
                    self.add_widget(item)

    def update_display(self):
        self.clear_widgets()
        print(myappstate)
        for myi in xrange(len(self.tabledata)):
            print("update data display was called")
            myrow = self.create_header(myi)
            for myitem in myrow:
                self.add_widget(myitem)

        if myappstate == True:
            for i in xrange(len(self.data)):
                row = self.create_player_info(i)
                #add all the items to the widget
                for item in row:
                    self.add_widget(item)



# this allows you to change the tableheader column names and number
    def create_header(self,i):
        first_column = TableHeader(text=self.tabledata[i]['LRT'])
        second_column = TableHeader(text=self.tabledata[i]['Type'])
        third_column = TableHeader(text=self.tabledata[i]['STR'])
        return [first_column, second_column, third_column]

# puts the data into the right column to build the table
    def create_player_info(self, i):
        first_column = PlayerRecord(text=self.data[i]['LRT'])
        second_column = PlayerRecord(text=self.data[i]['Type'])
        third_column = PlayerRecord(text=self.data[i]['STR'])
        return [first_column, second_column, third_column]
