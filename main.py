'''
Simple UI for the BS Demo for RD group
RS
'''
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import random
import time
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

from kivy.factory import Factory
import labelb

#class GetRuningTime(Label):
#    pass
class BSdemoRoot(BoxLayout):
    pass

#class my widget
class BSdemoForm(BoxLayout):
    bsdemo_currenttime = StringProperty()
    device_data = ObjectProperty()
    #this needs to actually be a method that starts and stips the server
    # then keeps track of how long the system has been running so it needs a
    # clock counter or paged periodic update
    def __init__(self, **kwargs):
        super(BSdemoForm, self).__init__(**kwargs)
        self.bsdemo_currenttime = "0"

    def get_apptime(self):
        self.bsdemo_currenttime = time.asctime()
        sys_data = self.get_devicedata()

    def get_devicedata(self):
        mytestdata = ['8.243, DJI Mavic, 4.39', '5.243, Parrot BeBop, Close', '2, Parrot Sumo, 2.3555']
        self.device_data.adapter.data[:]
        self.device_data.adapter.data.extend(mytestdata)
        self.device_data._trigger_reset_populate()

# add some mock device data. this will need to be some sort of MQTT push latter

class BSKivyApp(App):
    pass

if __name__ == '__main__':
	BSKivyApp().run()
