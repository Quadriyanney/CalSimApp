import kivy

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
Window.size = (250, 400)


class CalLayout(BoxLayout):

	'''The Main Widget of the Calculator App which inherits the BoxLayout class, it helps to display all other widgets'''

	def __init__(self, **kwargs):
		super(CalLayout, self).__init__(**kwargs)
		
		self.result_copy = ""
	
	def on_number_button_press(self, text):

		'''This method is called whenever a number button is clicked and the text on the button is shown in the textbox'''
		
		if self.textbox.text == "Math Error" or self.textbox.text == self.result_copy:
			self.textbox.text = ""
			self.textbox.text += text
		else:
			self.textbox.text += text
		pass

	def on_operand_button_press(self, text):

		'''This method is called whenever an operand button is clicked and the text on the button is shown in the textbox'''

		if self.textbox.text == "Math Error":
			self.textbox.text = ""
			self.textbox.text += text
		else:
			self.textbox.text += text
		pass

	def clear(self):

		'''This method is used to clear the textbox'''

		self.textbox.text = ""
		self.textbox.focus = True
		pass


	def display_answer(self, text):

		'''This method is used to display the answer of the operation in the textbox'''

		if self.textbox.text == "":
			pass
		
		else:
			try:
				self.result = eval(self.textbox.text)
				self.result_copy = str(self.result)
				self.textbox.text = ""
				self.textbox.insert_text(str(self.result))
			
			except:
				self.textbox.text = "Math Error"

		pass

class Cal_SimApp(App):

	'''This is the main App which inherits from the App class in kivy'''

	def build(self):

		'''This method helps to return the root widget (i.e. the CalLayout) of an App'''
		
		return CalLayout()
		pass
	

if __name__ == '__main__':
	Cal_SimApp().run()