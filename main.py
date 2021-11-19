import kivy
import csv
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

Drinkers = []

class BoxLayoutExample(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        with open('coffee_table.csv', mode='r') as csv_file:
            csv_read_obj = csv.DictReader(csv_file)
            for row in csv_read_obj:
                Drinkers.append(row["lastname"])

        for drinker in Drinkers:
            x = dp(300)
            y = dp(100)
            b = Button(text = drinker, size_hint=(None,None), size=(x,y), font_size=24)
            self.add_widget(b)

class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class CoffeeCashApp(App):
    pass

if __name__ == '__main__':
    CoffeeCashApp().run()