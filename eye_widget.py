import functools as ft
import math

from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.uix.floatlayout import FloatLayout


def degrees(value):
    """Converts value in radians to positive value in degrees"""
    result = math.degrees(value)
    if result < 0:
        return 360 + result
    else:
        return result


class EyeWidget(FloatLayout):

    x_value = NumericProperty(0)
    y_value = NumericProperty(0)
    base = StringProperty('')
    value = StringProperty('')
    triangle_points = ListProperty([])

    def init(self):
        for btn, values in [
            ('y_minus', (False, -.25)),
            ('y_plus', (False, +.25)),
            ('x_minus', (True, -.25)),
            ('x_plus', (True, +.25)),
        ]:
            self.ids[btn].bind(on_press=ft.partial(self.change_value, *values))
        self.ids['reset'].bind(on_press=self.reset)
        self.bind(x_value=self.update)
        self.bind(y_value=self.update)
        self.bind(size=self.update)

    def triangle(self, degree):
        width = self.width * 0.3
        points = []
        for offset in [-0.1, 0.1, math.pi, -0.1]:
            points += [
                self.center_x + width * math.cos(degree + offset),
                self.center_y + width * math.sin(degree + offset),
            ]
        return points

    def change_value(self, axis, value, _):
        if axis:
            self.x_value += value
        else:
            self.y_value += value

    def update(self, instance, _):
        base = math.atan2(instance.y_value, instance.x_value)
        instance.base = '{:.2f}'.format(degrees(
            base
        ))
        instance.value = '{:.2f}'.format(math.sqrt(
            instance.x_value ** 2 + instance.y_value ** 2
        ))
        if instance.x_value or instance.y_value:
            instance.triangle_points = instance.triangle(base)
        else:
            instance.triangle_points = []

    def reset(self, _):
        self.x_value = 0
        self.y_value = 0
