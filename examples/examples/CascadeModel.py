# -*- coding: utf-8 -*-
import logging
import subprocess


class CascadeModel:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    @staticmethod
    def get_foo():
        return "bar"
    
    @staticmethod
    def get_bar():
        return "foo"
    
    def power_off(self):
        try:
            self.logger.info("Powering off")
            subprocess.run(['shutdown','-h','now'])
        except subprocess.CalledProcessError as e:
            self.logger.critical(f"Unexpected error while deactivating device: {e}")
            return False
        else:
            return True
