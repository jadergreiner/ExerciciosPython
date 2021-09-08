from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    nome = StringProperty('')
    sobrenome = StringProperty('')
    result = StringProperty('Aguardando...')

    def mudar(self, *args):
        self.result ='Dados enviados com sucesso! Obrigado'


class MainApp(App):
    def build(self):
        return MyBoxLayout()


MainApp().run()
