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
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

from kivy.factory import Factory

#class GetRuningTime(Label):
#    pass
class BSdemoRoot(BoxLayout):
    pass

#class my widget
class BSdemoForm(BoxLayout):
    bsdemo_currenttime = StringProperty()
    #bsdemo_currenttime = "12"
    def __init__(self, **kwargs):
        super(BSdemoForm, self).__init__(**kwargs)
        self.bsdemo_currenttime = str(random.randint(1, 100))

    def get_apptime(self):
        self.bsdemo_currenttime = time.asctime()

class BSKivyApp(App):
    pass

if __name__ == '__main__':
	BSKivyApp().run()
