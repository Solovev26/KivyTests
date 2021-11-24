from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
#from plyer import
from jnius import autoclass

Window.size = (1080 / 3, 2340 / 3)


class MyApp(App):

    def build(self):
        self.title = 'SGPS'
        ## Заглушка бэкграунда
        fl = FloatLayout()
        #fl.add_widget(Image(source='back1.jpg'))

        bl = BoxLayout(padding=[50, 350], spacing=20)

        ## mute button
        bl.add_widget(Button(text="Mute me plz",
                             font_size=20,
                             on_press=self.btn_press_mute,
                             ))

        ## background button
        bl.add_widget(Button(text="Background\nmode on",
                             font_size=20,
                             on_press=self.btn_press_background,
                             ))
        fl.add_widget(bl)
        return fl

    ## action for backgroun button
    def btn_press_background(self, instance):
        print('background mode')

    ## action for mute button
    def btn_press_mute(self, instance):
        print('silent mode')
        AudioManager = autoclass('android.media.AudioManager')
        mode = AudioManager()
        mode.RINGER_MODE_SILENT


if __name__ == "__main__":
    MyApp().run()