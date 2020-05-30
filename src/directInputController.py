import os
import ctypes
import win32api
import time
from win32api import GetSystemMetrics

computerWidth=GetSystemMetrics(0)
computerHeight=GetSystemMetrics(1)
class MouseButton:
   class up:
      left= 0x0004
      middle = 0x0040
      right = 0x0010
   class down:
      left= 0x0002
      middle = 0x0020
      right = 0x0008

class keyboardButton:
    n1=0x02
    n2=0x03
    n3=0x04
    n4=0x05
    n5=0x06
    n6=0x07
    n7=0x08
    n8=0x09
    n9=0x0A
    n0=0x0B
    Q=0x10
    W=0x11
    E=0x12
    R=0x13
    T=0x14
    Y=0x15
    U=0x16
    I=0x17
    O=0x18
    P=0x19
    Delete = 0xD3 + 1024
    A=0x1E
    S=0x1F
    D=0x20
    F=0x21
    G=0x22
    H=0x23
    J=0x24
    K=0x25
    L=0x26
    Enter = 0x1C
    Z=0x2C
    X=0x2D
    C=0x2E
    V=0x2F
    B=0x30
    N=0x31
    M=0x32
    Period = 0x34
    Lctrl= 0x1D
    Space = 0x39
    Escape = 0x01

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def set_pos(x, y):
    x = 1 + int(x * 65536./computerWidth)
    y = 1 + int(y * 65536./computerHeight)
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(x, y, 0, (0x0001 | 0x8000), 0, ctypes.pointer(extra))
    command = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))
 
def left_click():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, MouseButton.down.left, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
 
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, MouseButton.up.left, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def right_click():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, MouseButton.down.right, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
 
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, MouseButton.up.right, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))    

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
