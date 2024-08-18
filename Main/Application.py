from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    def OnSubmit(self):
        TextInput = self.ids.TextInput
        InputText = TextInput.text
        OutputLabel = self.ids.OutputLabel
        OutputLabel.text = InputText
        TextInput.text = ""

class Shopping(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    Shopping().run()