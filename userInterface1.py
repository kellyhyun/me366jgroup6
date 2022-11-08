import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button # You would need futhermore this
from kivy.uix.boxlayout import BoxLayout
# import pythontest as pt
import UIhelperTEST as helper


class MyApp(App):

    def build(self):
        return Launch()


class Launch(BoxLayout):

    def say_hello(self):
        print ("hello")


class ButtonApp(App):
     
    def build(self):
        layout = BoxLayout()

        # use a (r, g, b, a) tuple
        btn1 = Button(text ="MidiTest",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(150, 250))
 
        # bind() use to bind the button to function callback
        btn1.bind(on_press = self.callback)
        
        btn2 = Button(text ="Song 1",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
 
        # bind() use to bind the button to function callback
        btn2.bind(on_press = self.callback2)
        
        exitB = Button(text ="exit",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(16, 16),
                   size_hint =(.2, .2),
                   pos =(300, 0))
        exitB.bind(on_press = self.close_application)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(exitB)
        
        return layout
 
    # callback function tells when button pressed
    def callback(self, event):
        print("miditest")
        helper.tester('MidiTest.csv')
        
    def callback2(self, event):
        print("song1")
        # tester('Song1.csv')
        
    def close_application(self, event):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()
  
         
 
# creating the object root for ButtonApp() class
root = ButtonApp()

if __name__ == '__main__':
    root.run()
    # MyApp().run()
    Window.close()
    
