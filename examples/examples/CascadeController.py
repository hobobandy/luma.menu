# -*- coding: utf-8 -*-
from luma.menu import Controller

from .CascadeModel import CascadeModel
from .CascadeView import CascadeView


class CascadeController(Controller):
    def __init__(self, ui, display, controls):
        super().__init__(ui, display, controls)
        
        # Override with our own Model/View
        self.model = CascadeModel()
        self.view = CascadeView(self)
    
    def draw_view(self):
        format_args = {
            "foo": self.model.get_bar(),
            "bar": self.model.get_foo()
        }
        self.view.update(format_args)
    
    def show_main_menu(self, event):
        if event == "button_a_pressed":
            self.view.show_menu(self.view.main_menu)
        elif event == "button_b_pressed":
            self.view.show_menu(self.view.main_menu)
        else:
            raise NotImplementedError
    
    def show_power_menu(self, event):
        if event == "button_a_pressed":
            self.view.show_menu(self.view.power_menu)
        elif event == "button_b_pressed":
            self.view.show_menu(self.view.main_menu)
        else:
            raise NotImplementedError
    
    def power_off(self, _):
        self.view.show_poweroff_message()
        self.model.power_off()
    
    def cancel_power_off(self, _):
        self.view.show_menu(self.view.main_menu)
    