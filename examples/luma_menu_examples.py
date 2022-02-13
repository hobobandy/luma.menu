# -*- coding: utf-8 -*-
import logging
import sys

from luma.menu.userinterface import UserInterface
from luma.menu.devices.adafruit3531 import Display, Controls

from examples.SimpleController import SimpleController
from examples.CascadeController import CascadeController


if __name__ == "__main__":
    """
    example logging to follow workflow
    """
    # Prepare formatter
    formatter_core = logging.Formatter('%(asctime)s %(levelname)s - %(module)s - %(message)s', '%H:%M:%S')
    # Console handler
    handler_console = logging.StreamHandler(sys.stdout)
    handler_console.setLevel(logging.DEBUG)  # Debug output goes only to a log file (less spammy in console)
    handler_console.setFormatter(formatter_core)
    # Configure root logging
    logging.basicConfig(level=logging.DEBUG, handlers=(handler_console,))

    """
    luma.menu bootstrap
    """
    ui = UserInterface(display=Display(contrast=1), controls=Controls())
    ui.add_controller(SimpleController)
    ui.add_controller(CascadeController)
    # Alternative
    # ui.add_controller((SimpleController, CascadeController))
    ui.main()