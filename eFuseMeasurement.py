from os import write
import pyvisa
import pandas as pd
import matplotlib.pyplot as plt
import csv, numpy as np
from time import sleep
site = "Try"
dut = "DUT14"
rm = pyvisa.ResourceManager()

hp_pulse = rm.open_resource("GPIB0::10::INSTR")
tds = rm.open_resource("GPIB0::6::INSTR")
smu = rm.open_resource("GPIB0::24::INSTR")

smu.write(":SOUR:FUNC VOLT")
smu.write(":SOUR:VOLT:MODE FIX")
smu.write(":SOUR:VOLT:RANG 2.1")
smu.write(":SOUR:VOLT 1.8")
smu.write(":CURR:PROT 20E-3")
smu.write(":OUTP 1")


# def oscilloscope():
tds.write(":CH1:SCA 500E-3")
tds.write(":CH2:SCA 500E-3")
tds.write(":CH3:SCA 500E-3")
tds.write(":CH4:SCA 2E-3")
tds.write(":CH1:POS 0")
tds.write(":CH2:POS 0")
tds.write(":CH3:POS 0")
tds.write(":CH4:POS 0")
tds.write(":CH1:IMP FIF")
tds.write(":CH2:IMP MEG")
tds.write(":CH3:IMP MEG")
tds.write(":CH4:IMP MEG")
tds.write(":CH1:COUP DC")
tds.write(":CH2:COUP DC")
tds.write(":CH3:COUP DC")
tds.write(":CH4:COUP DC")
tds.write(":CH1:YUN 'V'")
tds.write(":CH2:YUN 'V'")
tds.write(":CH3:YUN 'V'")
tds.write(":CH4:YUN 'A'")
tds.write(":CH1:PRO 1E0")
tds.write(":CH2:PRO 1E1")
tds.write(":CH3:PRO 1E1")
tds.write(":CH4:PRO 2E-1")

tds.write(":HORIZONTAL:MAIN:SCALE 2E-6")
tds.write("HOR:DEL:TIM 7e-6")
tds.write(":FPA:PRESS SINGLESEQ")

sleep(1)

print(hp_pulse.query(":SYST:ERR?"))
print(tds.query(":EVMSG?"))

hp_pulse.write(":PULS:PER 12US")
hp_pulse.write(":PULS:WIDT1 6US")
hp_pulse.write(":PULS:WIDT2 2US")
hp_pulse.write(":PULS:DEL2 2US")

hp_pulse.write(":VOLT1:HIGH 900MV")
hp_pulse.write(":VOLT1:LOW 0V")
hp_pulse.write(":VOLT2:HIGH 1.1V")
hp_pulse.write(":VOLT2:LOW 0V")

hp_pulse.write(":ARM:SOUR MAN")
hp_pulse.write(":ARM:MODE STAR")
hp_pulse.write(":ARM:SENS POS")

# Step: Turn on the HP Pulse Generator output 1 and 2
hp_pulse.write(":OUTP1 0")
hp_pulse.write(":OUTP2 1")

hp_pulse.write(":TRIG:COUN 2")
hp_pulse.write(":TRIG:SOUR INT")
hp_pulse.write(":DIG:PATT OFF")

hp_pulse.write("*TRG")

sleep(1)

def get_curve(channel):
    source = ":DAT:SOU {}".format(channel)
    tds.write(source)
    tds.write(":DAT:ENC ASCI")
    tds.write(":DAT:WID 2")
    tds.write(":DAT:STAR 0")
    tds.write(":DAT:STOP 10000")
    waveform_preamble = tds.query(":WFMP?")
    fileName = "{}\{}\WaveformPreamble_{}.csv".format(site, dut, channel)
    waveform_preamble_dataframe = pd.DataFrame(list(waveform_preamble[8:].split(";")), columns=["Waveform_Preamble"])
    waveform_preamble_dataframe.to_csv(fileName)
    # y_mult = float(waveform_preamble_dataframe["Waveform_Preamble"][12][6:])
    # nr_pt = float(waveform_preamble_dataframe["Waveform_Preamble"][5][6:])
    y_mult = float(tds.query(":WFMP:YMU?")[14:-1])
    x_zero = float(tds.query(":WFMP:XZE?")[14:-1])
    x_interval = float(tds.query(":WFMP:XIN?")[14:-1])
    nr_pt = float(tds.query(":WFMP:NR_P?")[14:-1])
    curve = tds.query(":CURV?")
    curve_slicing = curve[7:-1]
    return curve_slicing, y_mult, x_zero, x_interval, nr_pt

# Python code to convert string to list
def Convert(string):
    li = list(string.split(","))
    return li

curve_ch1 = get_curve('CH1')
curve_ch2 = get_curve('CH2')
curve_ch3 = get_curve('CH3')
curve_ch4 = get_curve('CH4')

# timeFrame = np.arange(curve_ch1[2], curve_ch1[4], curve_ch1[3])
# print(curve_ch1[1])
# print(curve_ch1[2])
print("Time interver: ", curve_ch1[3])
# print(curve_ch1[4])
ch1_data = Convert(curve_ch1[0])
ch2_data = Convert(curve_ch2[0])
ch3_data = Convert(curve_ch3[0])
ch4_data = Convert(curve_ch4[0])

dataframe = pd.DataFrame(list(zip(ch1_data, ch2_data, ch3_data, ch4_data)), columns=["CH1", "CH2", "CH3", "CH4"])
fileName2 = "{}\{}\PostProgramming_Vg1.1V_Vd1.8v{}.csv".format(site, dut, dut)
dataframe.to_csv(fileName2)

print(dataframe)

smu.write(":OUTP OFF")
hp_pulse.write(":OUTP2 0")