# -*- coding: utf-8 -*-
from luma.menu import View
from luma.menu.widgets import Scrollbar, Titlebar, Menu


class SimpleView(View):
    _title = "SIMPLE EXAMPLE"
    
    def __init__(self, ctrl):
        super().__init__(ctrl)
        self.interval = 60
    
    def create_widgets(self):
        self.title = Titlebar(self, text=self._title)

        self.main_menu = Menu(self, xy=(0,12,120,64), title="SIMPLE EXAMPLE")
        self.main_menu.add_text("Open source software is")
        self.main_menu.add_text("made better when users")
        self.main_menu.add_text("can easily contribute")
        self.main_menu.add_text("code and documentation")
        self.main_menu.add_text("to fix bugs and add")
        self.main_menu.add_text("features.")
        self.main_menu.add_text("Learn more about how to")        
        self.main_menu.add_text("make Python better for")      
        self.main_menu.add_text("everyone.")        
        self.menu = self.main_menu
        
        # @todo should this be passed to the menu(s)?
        self.scrollbar = Scrollbar(self)
        
        self.layout.append(self.title)
        self.layout.append(self.main_menu)
        self.layout.append(self.scrollbar)
    