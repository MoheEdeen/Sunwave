from http.client import TOO_MANY_REQUESTS
from re import T
from socket import IPV6_JOIN_GROUP
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import math
from functools import partial
from kivy.clock import Clock

Window.size = (390, 884)


class SplashScreenWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ACPWindow(Screen):
    def get_num_of_month(self):
        try:
            month_input = int(str(self.ids.month_input.text))
            if (month_input > 12 or month_input < 1):
                self.ids.month_input.text = ""
                self.ids.month_input.hint_text = "Month number should be between 1 and 12"
            else:
                self.ids.months_grid.clear_widgets(
                    children=self.ids.months_grid.children)
                self.ids.power_label.text = ""
                self.ids.average_label.text = ""
                self.ids.submit_button.text = "Submit"
                self.ids.submit_button.disabled = False
                counter = 0
                for i in range(math.ceil(float(month_input/3))):
                    self.ids.months_grid.rows += 1
                for i in range(self.ids.months_grid.rows):
                    if counter == month_input:
                        break
                    for j in range(month_input):
                        self.ids.months_grid.add_widget(TextInput(hint_text=f'Month #{j+1}', background_normal='', halign="center", multiline=False,
                                                        height=30, font_name="Fonts/ARLRDBD.TTF", input_filter="float",
                                                        background_color=(46/255, 54/255, 59/255, 0), foreground_color=(1, 1, 1, 1)))
                        counter += 1
        except ValueError:
            pass

    def average_months(self):
        total_consumption = 0
        counter = 0
        month_input = int(str(self.ids.month_input.text))
        for child in self.ids.months_grid.children:
            if child.text == "":
                child.hint_text = "Fill Me"
            else:
                total_consumption += float(str(child.text))
                counter += 1
        if counter == month_input:
            avg = total_consumption / month_input
            self.power = avg / 130
            self.power = round(self.power, 2)
            self.ids.submit_button.text = "Submitted!"
            self.ids.submit_button.disabled = True
            self.ids.power_label.text = f"Power: {str(self.power)} KW"
            self.ids.average_label.text = f"Average: {str(avg)} W"
            self.manager.screens[1].ids.Numofsolarpannels.disabled = False


# Kivy buttons


class RoundedButton4(Button):
    pass


class NumberOfSolarPanelWindow(Screen):
    def submit_available(self):
        self.ids.submit_watt.text = "Submit"
        self.ids.submit_watt.disabled = False

    def calculate_num_of_solar_panels(self):
        try:
            power = (self.manager.screens[2].ids.power_label.text).split()
            power = (float(power[1]))*1000
            watt_peak = self.ids.watt_peak.text
            if watt_peak == "":
                self.ids.watt_peak.hint_text = "Fill Me"
            elif not isinstance(power, float):
                raise ValueError
            else:
                watt_peak = float(watt_peak)
                num_of_solar_panels = round(float(power/watt_peak))
                self.load = (num_of_solar_panels * power)/1000
                self.ids.submit_watt.text = "Submitted!"
                self.ids.submit_watt.disabled = True
                self.ids.solar_panel_label.text = f"Number: {str(num_of_solar_panels)}"
                self.ids.expected_load.text = f"Load: {str(self.load)} KW"
                self.manager.screens[1].ids.recommendedinverter.disabled = False
        except:
            pass


class RecommendedInverterWindow(Screen):
    def load_bearing(self):

        try:
            self.manager.screens[5].ids.phase_chooser.text = "What is the Inteneted Phase?"
            self.manager.screens[6].ids.phase_chooser_sma.text = "What is the Inteneted Phase?"
            self.manager.screens[7].ids.phase_chooser_huawei.text = "What is the Inteneted Phase?"
            bearing_load = (float(self.manager.screens[3].load)) * 1.15
            bearing_load = round(bearing_load, 3)
            self.ids.bearing_load_label.text = f"Bearing load: {str(bearing_load)} KW"
            self.manager.screens[1].ids.circuitbreaker.disabled = False
        except:
            pass
# code created by mohe edeen abu maizer


class ABBWindow(Screen):
    def phase_type(self, phase):
        if str(phase) == "What is the Inteneted Phase?":
            self.ids.abb_box.clear_widgets(
                children=self.ids.abb_box.children)
        elif str(phase) == "Three Phase":
            self.ids.abb_box.clear_widgets(
                children=self.ids.abb_box.children)
            self.ids.abb_box.add_widget(RoundedButton4(font_size="18", halign="center", valign="center",
                                        size_hint=(1, None), pos_hint={'center_x': 0.5, 'bottom': 1}, text="ABB: \n11KW", on_press=lambda x: self.mppt("\n11KW")))
        else:
            values = ["\n1.5KW", "\n2.5KW", "\n3.3KW", "\n3.5KW"]
            self.ids.abb_box.clear_widgets(
                children=self.ids.abb_box.children)
            for value in values:
                self.btn = RoundedButton4(font_size="18", halign="center", valign="center",
                                          size_hint=(1, None), pos_hint={'center_x': 0.5, 'bottom': 1}, text=f"ABB: {value}")
                self.btn.bind(on_press=lambda x, bounded_value=value:
                              self.mppt(bounded_value))
                self.ids.abb_box.add_widget(self.btn)

    def mppt(self, kw):
        if ((kw == "\n11KW") or (kw == "\n3.5KW")):
            self.ids.mppt_text.text = "MPPT: 2"
        else:
            self.ids.mppt_text.text = "MPPT: 1"


class SMAWindow(Screen):
    def phase_type(self, phase):
        if str(phase) == "What is the Inteneted Phase?":
            self.ids.sma_box.clear_widgets(
                children=self.ids.sma_box.children)
        elif str(phase) == "Three Phase":
            values = ["\n5KW", "\n6KW", "\n8KW", "\n10KW"]

            self.ids.sma_box.clear_widgets(
                children=self.ids.sma_box.children)
            for value in values:
                self.ids.sma_box.add_widget(RoundedButton4(font_size="18", halign="center", valign="center",
                                                           size_hint=(1, None), pos_hint={'center_x': 0.5, 'bottom': 1}, text=f"SMA: {value}"))

        else:
            self.ids.sma_box.clear_widgets(
                children=self.ids.sma_box.children)
            values = ["\n3KW", "\n3.6KW", "\n4KW", "\n5KW", "\n6KW"]
            for value in values:
                self.ids.sma_box.add_widget(RoundedButton4(font_size="18", halign="center", valign="center", size=(0, 80),
                                                           size_hint=(1, None), pos_hint={'center_x': 0.5, 'bottom': 1}, text=f"SMA: {value}"))

    # code created by mohe edeen abu maizer


class HuaweiWindow(Screen):
    def phase_type(self, phase):
        if str(phase) == "What is the Inteneted Phase?":
            self.ids.huawei_box.clear_widgets(
                children=self.ids.huawei_box.children)
        elif str(phase) == "Three Phase":
            self.ids.huawei_box.clear_widgets(
                children=self.ids.huawei_box.children)
            values = ["\n12KW", "\n15KW", "\n17KW", "\n20KW"]
            for value in values:
                self.btn = RoundedButton4(font_size="18", halign="center", valign="center",
                                          size_hint=(1, None), pos_hint={'center_x': 0.5, 'bottom': 1}, text=f"Huawei: {value}")
                self.btn.bind(on_press=lambda x, bounded_value=value:
                              self.mppt(bounded_value))
                self.ids.huawei_box.add_widget(self.btn)
        else:
            self.ids.huawei_box.clear_widgets(
                children=self.ids.huawei_box.children)
            values = ["\n3KW", "\n4.5KW", "\n5.52KW",
                      "\n6KW", "\n6.9KW", "\n7.5KW", "\n9KW"]
            for value in values:
                self.btn = RoundedButton4(font_size="18", halign="center", valign="center",
                                          size_hint=(1, None), pos_hint={'center_x': 0.5, 'bottom': 1}, text=f"Huawei: {value}", size=(0, 50))
                self.btn.bind(on_press=lambda x, bounded_value=value:
                              self.mppt(bounded_value))
                self.ids.huawei_box.add_widget(self.btn)

    def mppt(self, kw):
        self.ids.mppt_text.text = "MPPT: 2"


class CircuitBreakerWindow(Screen):
    def submit_available(self):
        self.ids.submit_max_current.text = "Submit"
        self.ids.submit_max_current.disabled = False

    def calculate_circuit_breaker(self):
        try:
            max_current = self.ids.max_current.text
            self.circuit_breaker = float(max_current) * 1.2
            self.ids.circuit_breaker_value.text = f"Circuit Breaker: {str(self.circuit_breaker)} Amps"
            self.ids.submit_max_current.text = "Submitted!"
            self.ids.submit_max_current.disabled = True
            self.manager.screens[1].ids.crosssection.disabled = False
        except:
            pass


class CrossSectionCablesWindow(Screen):
    def underground(self):
        try:
            self.ids.cross_section_cables_value.text = ""
            cross_section = self.manager.screens[8].circuit_breaker / 0.7656
            cross_section = round(cross_section, 2)
            self.ids.cross_section_cables_value.text = f"Cross Section: {str(cross_section)} mm"
        except:
            pass

    def free_air(self):
        try:
            self.ids.cross_section_cables_value.text = ""
            cross_section = self.manager.screens[8].circuit_breaker / 0.744
            cross_section = round(cross_section, 2)
            self.ids.cross_section_cables_value.text = f"Cross Section: {str(cross_section)} mm"
        except:
            pass


class ThirdWindow(Screen):
    def clear(self):
        self.ids.calc_input.text = "0"

    # When button is pressed:
    def button_press(self, button):
        text_box_value = self.ids.calc_input.text
        if ("ERROR" in text_box_value):
            text_box_value = "0"
        if (text_box_value == "0"):
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text += f"{button}"

    # Decimals
    def dec(self):
        text_box_value = self.ids.calc_input.text
        nums = text_box_value.split("+")
        if "+" in text_box_value and "." not in nums[-1]:
            self.ids.calc_input.text += f"."
        elif ("." in text_box_value):
            pass
        else:
            self.ids.calc_input.text += f"."

    # math
    def math(self, sign):
        self.ids.calc_input.text += f"{sign}"

    # Equate
    def equate(self):
        text_box_value = self.ids.calc_input.text
        fixed_text = text_box_value.replace("×", "*")
        fixed_text = fixed_text.replace("÷", "/")
        fixed_text = fixed_text.replace("^", "**")
        try:
            ans = eval(fixed_text)
            if (len(str(ans)) > 6):
                ans = format(ans, ".2E")
            self.ids.calc_input.text = str(ans)
        except:
            self.ids.calc_input.text = "ERROR"

        '''
        # Addition
        if ("+" in text_box_value):
            answer = 0.0
            nums = text_box_value.split("+")
            for num in nums:
                answer += float(num)

            self.ids.calc_input.text = str(answer)
        '''
    # Backspace

    def delete(self):
        text_box_value = self.ids.calc_input.text
        text_box_value = text_box_value[:-1]
        self.ids.calc_input.text = text_box_value

    # Change num sign
    def change_sign(self):
        text_box_value = self.ids.calc_input.text
        if ("-" in text_box_value):
            self.ids.calc_input.text = f"{text_box_value.replace('-','')}"
        else:
            self.ids.calc_input.text = f"-{text_box_value}"


class WindowManager(ScreenManager):
    pass


class Sunwave(App):
    global screen_manager
    screen_manager = ScreenManager()
    # code created by Mohe Edeen Abu Maizer

    def build(self):
        screen_manager.add_widget(SplashScreenWindow(name="splash_screen"))
        screen_manager.add_widget(SecondWindow(name="second_window"))
        screen_manager.add_widget(ACPWindow(name="annual_consumption_page"))
        screen_manager.add_widget(NumberOfSolarPanelWindow(
            name="NumberOfSolarPanelWindow_page"))
        screen_manager.add_widget(RecommendedInverterWindow(
            name="RecommendedInverterWindow_page"))
        screen_manager.add_widget(ABBWindow(name="ABB_window"))
        screen_manager.add_widget(SMAWindow(name="SMA_window"))
        screen_manager.add_widget(HuaweiWindow(name="Huawei_window"))
        screen_manager.add_widget(
            CircuitBreakerWindow(name="CircuitBreakerWindow_page"))
        screen_manager.add_widget(CrossSectionCablesWindow(
            name="CrossSectionCablesWindow_page"))
        screen_manager.add_widget(ThirdWindow(name="third_window"))

        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)

    def change_screen(self, dt):
        screen_manager.current = "second_window"
        return KV


KV = Builder.load_file("main.kv")


if __name__ == "__main__":
    Sunwave().run()
