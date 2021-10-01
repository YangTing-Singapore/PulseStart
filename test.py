from os import write
import pyvisa
import pandas as pd
import matplotlib.pyplot as plt
import csv    

rm = pyvisa.ResourceManager()
print(rm.list_resources())

# hp_pulse = rm.open_resource("GPIB0::10::INSTR")
tds = rm.open_resource("GPIB0::6::INSTR")
channel="CH2"
source = ":DAT:SOU {}".format(channel)
tds.write(source)
tds.write(":DAT:ENC ASCI")
tds.write(":DAT:WID 2")
tds.write(":DAT:STAR 4500")
tds.write(":DAT:STOP 5500")
curve = tds.query(":CURV?")
curve_slicing = curve[7:-1]
print(curve_slicing)