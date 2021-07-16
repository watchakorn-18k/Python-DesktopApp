#!/usr/bin/env python
# -- coding: utf-8 --
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("0")

    
    def on_button_click(self):
        if self.count_enabled == True:
            print("กดแล้วนะ")
            self.count += 1
            self.my_text = f"{self.count}"
            

    
    def on_toggle_button_state(self,widget):
        print("toggle state"+ widget.state)
        if widget.state == "normal":
            #normal
            widget.text = "ปิด"
            widget.font_name = 'fonts/ChulabhornLikitText-Light.otf'
            widget.font_size = "20dp"
            self.count_enabled = False
        else:
            #down
            widget.text = "เปิด"
            widget.font_name = 'fonts/ChulabhornLikitText-Light.otf'
            widget.font_size = "20dp"
            self.count_enabled = True


        




class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(0,100):
            #size = dp(100) + i *10
            size = dp(100) 
            b = Button(
                    text=str(i+1), 
                    size_hint=(None,None),
                    size=(size,size)
                )
            self.add_widget(b)
        

#class GridLayoutExample(GridLayout):
#   pass



class AnchorLayoutSample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
"""
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""
class MainWidget(Widget):
    pass

class ProgrameTestDevByProtonApp(App):
    pass
ProgrameTestDevByProtonApp().run()