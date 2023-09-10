from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabels(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.HEX_COLOR_CODE = {"ZAFFRE": "#0014a8", "ZOMP": "#39a78e", "WINE": "#722f37", "WINTERGREEN": "#56887d",
                               "WISTERIA": "#c9a0dc", "TURQUOISE": "#00ffef", "TEAL BLUE": "#367588",
                               "SHAMROCK GREEN": "#009e60",
                               "ROYALBLUE": "#4169e1", "PALETURQUOISE": "#afeeee"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for color in self.HEX_COLOR_CODE:
            temp_button = Button(text=color)
            temp_button.bind(on_press=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        color = instance.text
        self.status_text = f"{color}'s number is {self.HEX_COLOR_CODE[color]}"

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()


DynamicLabels().run()
