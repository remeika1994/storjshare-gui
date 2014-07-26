#
# The Kivy interface for DriveMiner.
#
# me@leefallat.ca - 2014
#

from kivy.app import App
from kivy.properties import Property
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
import kivy.utils

class DriveMiner(Widget):	
	storage_percent = Property('0%')
	storage_bar = NumericProperty(0)
	lower_storage_limit = Property('0')
	upper_storage_limit = Property('0 GB')
	free_amount = Property('0 GB')
	used_amount = Property('0 GB')
	total_amount = Property('0 GB')
	
	# The events are bound in the driveminer.kv file.
	def app_cancel_callback(self, instance):
		# Put your code here for when the cancel button is pressed
		print("[x] released")
		
	def settings_callback(self, instance):
		# Same as the first callback function
		print("[SETTINGS] released")
		
	def go_callback(self, instance):
		# Same as the first callback function
		print("[GO] released")
	

class DriveMinerApp(App):
	def build(self):
		return DriveMiner()
		
if __name__ == "__main__":
	DriveMinerApp().run();