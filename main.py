#!/usr/bin/env python
# -- coding: utf-8 --
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget



class AnchorLayoutSample(AnchorLayout):
    pass

class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("0")
    text_input_str = StringProperty("Foo")
    text_input_score = NumericProperty(0)
    #slider_value_txt = StringProperty("50%")

    
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

    def on_switch_active(self,widget):
        print("Switch: " + str(widget.active))
    
    def on_slider_value(self,widget):
        print("Slider: " + str(int(widget.value)))
        #self.slider_value_txt = f"{str(int(widget.value))}%"
    
    def on_text_validate(self,widget):
        #self.text_input_str = widget.text
        try:
            self.text_input_score = widget.text
            if self.text_input_score >= 50:
                self.text_input_str = "ผ่าน"
                print(type(self.text_input_score))
            else:
                self.text_input_str = "ไม่ผ่าน"
                print(type(self.text_input_score))

        except ValueError:
            self.text_input_str = "โปรดกรอกข้อมูลใหม่"
            print(type(self.text_input_score))





        
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

class CanvasExample1(Widget):
    pass
class CanvasExample2(Widget):
    pass
class CanvasExample3(Widget):
    pass

ProgrameTestDevByProtonApp().run()
