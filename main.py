
from kivy.app import App
from kivy.uix.widget import Widget

from eye_widget import EyeWidget  # noqa


class PrismCalcWidget(Widget):
    pass


class PrismCalcApp(App):
    def build(self):
        widget = PrismCalcWidget()
        for ew in widget.children[0].children:
            ew.init()
        return widget


if __name__ == '__main__':
    PrismCalcApp().run()
