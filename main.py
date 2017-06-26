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
    #this needs to actually be a method that starts and stips the server
    # then keeps track of how long the system has been running so it needs a
    # clock counter or paged periodic update
    def __init__(self, **kwargs):
        super(BSdemoForm, self).__init__(**kwargs)
        self.bsdemo_currenttime = "0"

    def get_apptime(self):
        self.bsdemo_currenttime = time.asctime()

class BSKivyApp(App):
    pass

if __name__ == '__main__':
	BSKivyApp().run()
