# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyvisa
import time

rm = pyvisa.ResourceManager()
vna = rm.open_resource("TCPIP0::<VNA_IP_ADDR>::INSTR")
response = vna.query("*IDN?")
print(response)
vna.write('SYST:FPR') #System reset
vna.write('DISP:WIND ON') #turn on window
vna.write("CALC:CUST:DEF 'sa_meas', 'Spectrum Analyzer', 'A'") #Select Spectrum analyzer mode 
vna.write('DISP:WIND:TRAC:FEED "sa_meas"') #display the spectrum analyzer
vna.write("CALC:PAR:SEL 'sa_meas'")
vna.write('SENS:FREQ:CENTER 150 MHz') #set the center at 500MHz
vna.write('SENS:FREQ:SPAN 50 MHZ') #set the span at 100MHz
vna.write('CALC:MARK ON') #Turn on a marker
vna.write('CALC:MARK:FORM MLOG') #set the query format to magnitude log
vna.write('CALC:MARK:FUNC MAX') #set the marker mode to max
vna.write('CALC:MARK:FUNC:TRAC ON') #turn on auto trace 
while True:
    peak = vna.query('CALC:MARK:Y?')    # marker Y readout
    freq = vna.query('CALC:MARK:X?')    # marker X readout
    print('Frequency:', (float(freq[1:5]) * pow(10,(float(freq[16:19]))))/(pow(10,6)), 'MHz') # String weird stuff
    print('Peak:', float(peak[0:5])*(pow(10,(float(peak[16:19])))), 'dBm')  # more weird string stuff
    time.sleep(1)
