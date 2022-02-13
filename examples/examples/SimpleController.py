# -*- coding: utf-8 -*-
from luma.menu import Controller

from .SimpleModel import SimpleModel
from .SimpleView import SimpleView


class SimpleController(Controller):
    def __init__(self, ui, display, controls):
        super().__init__(ui, display, controls)
        
        # Override with our own Model/View
        self.model = SimpleModel()
        self.view = SimpleView(self)
