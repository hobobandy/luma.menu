# -*- coding: utf-8 -*-
from luma.menu import View
from luma.menu.widgets import Scrollbar, Titlebar, Menu


class CascadeView(View):
    _title = "CASCADE EXAMPLE"
    
    def __init__(self, ctrl):
        super().__init__(ctrl)
        self.interval = 3
    
    def create_widgets(self):
        self.title = Titlebar(self, text=self._title)
                
        self.power_menu = Menu(self, xy=(0,12,120,64), title="POWER OFF")
        self.power_menu.add_text("Are you sure?")
        self.power_menu.add_command("Yes", command=self.ctrl.power_off)
        self.power_menu.add_command("No", command=self.ctrl.cancel_power_off)
        self.power_menu.hide()
        
        self.main_menu = Menu(self, xy=(0,12,120,64), title="CASCADE EXAMPLE")
        self.main_menu.add_text("Hello, world!")
        self.main_menu.add_text("")
        self.main_menu.add_text("Foo: {foo}")
        self.main_menu.add_text("Bar: {bar}")
        self.main_menu.add_command("Power Off 1 →", command=self.ctrl.show_power_menu)
        self.main_menu.add_text("This is an example")
        self.main_menu.add_text("of scrollable views.")
        self.main_menu.add_text("------------------------")
        self.main_menu.add_command("Power Off 2 →", command=self.ctrl.show_power_menu)

        self.menu = self.main_menu
        
        # @todo should this be passed to the menu(s)?
        self.scrollbar = Scrollbar(self)
        
        self.layout.append(self.title)
        self.layout.append(self.power_menu)
        self.layout.append(self.main_menu)
        self.layout.append(self.scrollbar)
    
    def show_poweroff_message(self):
        self.title = Titlebar(self, text="WARNING!")
        
        self.poweroff_message = Menu(self, xy=(0,12,120,64), title="POWER OFF")
        self.poweroff_message.add_text("Wait until the green LED")
        self.poweroff_message.add_text("stops flashing to safely")
        self.poweroff_message.add_text("unplug power cable.")
        self.poweroff_message.show()
        
        self.layout = list()
        self.layout.append(self.title)
        self.layout.append(self.poweroff_message)
        self.force_redraw()
    