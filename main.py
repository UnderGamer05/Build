from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label

from kivy import platform


if platform == "android":
	from android.permissions import request_permissions, Permission
	request_permissions([Permission.READ_EXTERNAL_STORAGE,
                       Permission.WRITE_EXTERNAL_STORAGE])



class AudioFileChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(AudioFileChooser, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.filechooser = FileChooserListView(filters=['*.mp3', '*.wav', '*.ogg'])
        self.add_widget(self.filechooser)

        self.label = Label(size_hint_y=0.05)
        self.add_widget(self.label)

        self.select_button = Button(text='Select', size_hint_y=0.05)
        self.select_button.bind(on_release=self.select_file)
        self.add_widget(self.select_button)

    def select_file(self, instance):
        selected = self.filechooser.selection
        if selected:
            self.label.text = selected[0]
            audio_sep(selected[0])
        else:
            self.label.text = 'No file selected'


def audio_sep(path):
	from spleeter.separator import Separator
	separator = Separator('spleeter:2stems')
	
	separator.separate_to_file(path, 'sdcard/SepAudio')
	

class AudioFileChooserApp(App):
    def build(self):
        return AudioFileChooser()

if __name__ == '__main__':
    AudioFileChooserApp().run()
