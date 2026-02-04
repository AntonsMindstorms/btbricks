"""
btbricks - A MicroPython Bluetooth library for controlling LEGO hubs.

This package provides tools for remote controlling LEGO hubs and linking
smart hubs through the official LEGO Bluetooth protocol. You can also
use it to create custom Bluetooth peripherals like RC controllers or MIDI
devices compatible with LEGO hubs.
"""

__version__ = "0.2.6"
__author__ = "Anton Vanhoucke"
__license__ = "MIT"

from .bt import (
    BLEHandler,
    UARTCentral,
    UARTPeripheral,
    RCReceiver,
    RCTransmitter,
    MidiController,
    R_STICK_HOR,
    R_STICK_VER,
    L_STICK_HOR,
    L_STICK_VER,
    BUTTONS,
    L_TRIGGER,
    R_TRIGGER,
    SETTING1,
    SETTING2,
)
from .bthub import (
    BtHub,
    OFF,
    PINK,
    PURPLE,
    DARK_BLUE,
    BLUE,
    TEAL,
    GREEN,
    YELLOW,
    ORANGE,
    RED,
    WHITE,
)

from .bthub import BtHub as SmartHub

__all__ = [
    "BLEHandler",
    "UARTCentral",
    "UARTPeripheral",
    "RCReceiver",
    "RCTransmitter",
    "MidiController",
    "R_STICK_HOR",
    "R_STICK_VER",
    "L_STICK_HOR",
    "L_STICK_VER",
    "BUTTONS",
    "L_TRIGGER",
    "R_TRIGGER",
    "SETTING1",
    "SETTING2",
    "BtHub",
    "SmartHub",
]
