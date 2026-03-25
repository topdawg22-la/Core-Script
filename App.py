"""
NEXUS-AUTO-OS MOBILE UI v1.0.0
Lead Architect: Gunner Blake Carr
Credentials: B.S. Systems Engineering & Software Dev (Colorado Tech)
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

# -- THE DESIGN PHILOSOPHY: RUGGED & PROFITABLE --
# Touchscreen-friendly, clear "Bi-Directional" controls.

class NexusMain(BoxLayout):
    def __init__(self, **kwargs):
        super(NexusMain, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # 1. Header with CTU Badge & Name
        header = Label(text="NEXUS-AUTO-OS | Gunner Carr (CTU)", 
                       size_hint_y=0.1, color=(1, 1, 1, 1),
                       bold=True, font_size='20sp')
        self.add_widget(header)

        # 2. Connection Status (Fake for this demo)
        status_layout = BoxLayout(size_hint_y=0.1)
        status_label = Label(text="VEHICLE LINK: Ford Lightning (2024)", color=(0, 1, 0, 1)) # Green for connected
        ecu_count = Label(text="ECUs FOUND: 18")
        status_layout.add_widget(status_label)
        status_layout.add_widget(ecu_count)
        self.add_widget(status_layout)

        # 3. Quick Action Buttons (The "Profit" Buttons)
        quick_actions = GridLayout(cols=3, size_hint_y=0.2, spacing=10)
        btn1 = Button(text="[color=ff0000]SGW UNLOCK[/color]", markup=True) # Red text for security action
        btn2 = Button(text="QUICK SCAN")
        btn3 = Button(text="CLEAR CODES")
        
        quick_actions.add_widget(btn1)
        quick_actions.add_widget(btn2)
        quick_actions.add_widget(btn3)
        self.add_widget(quick_actions)

        # 4. Core Diagnostic Log
        self.log_input = TextInput(text="[SYSTEM] Nexus-Auto-OS Engine v1.0.0 Online\n[AUDIT] Security Handshake Complete\n", 
                                   multiline=True, readonly=True, size_hint_y=0.5)
        self.add_widget(self.log_input)

        # 5. Advanced/Expert Control
        expert_btn = Button(text="[b]ADVANCED BI-DIRECTIONAL[/b]", markup=True, size_hint_y=0.1)
        expert_btn.bind(on_release=self.show_expert_menu)
        self.add_widget(expert_btn)

    # Example of a Bi-Directional Function
    def show_expert_menu(self, instance):
        """A professional 'popup' to force a system test."""
        content = BoxLayout(orientation='vertical')
        
        # Expert functions that technicians pay for (e.g., Ford DPF Regen, GM Cylinder Deactivation)
        btn_dpf = Button(text="FORCE DPF REGEN")
        btn_abs = Button(text="ABS BLEED MODE")
        btn_close = Button(text="CLOSE")

        content.add_widget(btn_dpf)
        content.add_widget(btn_abs)
        content.add_widget(btn_close)

        popup = Popup(title='Expert Bi-Directional Tests',
                      content=content, size_hint=(0.8, 0.8), auto_dismiss=False)
        btn_close.bind(on_release=popup.dismiss)
        popup.open()

class NexusApp(App):
    def build(self):
        self.title = "Nexus-Auto-OS v1.0.0 Alpha"
        return NexusMain()

if __name__ == '__main__':
    NexusApp().run()
