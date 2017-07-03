class DeviceData(object):
    def __init__(self):
        self.devicedata = []

    @property
    def devicedata(self):
        return self.devicedata

    @devicedata.setter
    def devicedata(self, value):
        self.devicedata = value

    @devicedata.getter
    def devicedata(self):
        self.devicedata = [
            {'LRT': '8.243', 'Type': 'DJI Mavic', 'STR': '4.39'},
            {'LRT': '5.243', 'Type': 'Parrot BeBop', 'STR': 'Close'},
            {'LRT': '7.11', 'Type': 'Parrot Ebee', 'STR': 'Close'},
            {'LRT': '5.3', 'Type': 'Parrot DISCO', 'STR': '11.12'},
            {'LRT': '3.20', 'Type': 'Yuneec Typhoon', 'STR': '2.13'},
            {'LRT': '5.44', 'Type': 'Yuneec', 'STR': '5.23'},
            {'LRT': '1.12', 'Type': 'DJI Pro 4', 'STR': '1.10'},
            {'LRT': '2', 'Type': 'Parrot Sumo', 'STR': '2.3555'}
        ]

    @devicedata.deleter
    def devicedata(self):
        self.davicedata = self.davicedata.clear()
