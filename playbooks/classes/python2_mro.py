class UIComponent:
    name = None

    def __init__(self, value):
        self.value = value

    def render(self):
        return '<{self.name}>{self.value}</{self.name}>'


class Toggle(UIComponent):
    name = 'toggle'

    def __init__(self, value):
        UIComponent.__init__(self, value)
        self.is_active = False

    def click(self):
        self.is_active = not self.is_active


class Colorable(UIComponent):
    def __init__(self, value):
        UIComponent.__init__(self, value)
        self.color = None


class ColorableToggle(Toggle, Colorable):
    def __init__(self, value, color):
        Toggle.__init__(self, value)
        self.color = color


toggle = ColorableToggle('Submit', 'blue')
print(toggle.render())
