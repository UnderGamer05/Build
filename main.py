from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
	
	def build(self):
		text = Label(text="Hello")
		return text
	

MyApp().run()