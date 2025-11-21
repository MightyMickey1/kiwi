import pyvisa
import time

rm = pyvisa.ResourceManager()
SigGen = rm.open_resource('TCPIP0::192.168.0.70::INSTR')

ID = SigGen.query('*IDN?')
print(ID);
SigGen.write('FUNC SIN')  # Select the sweep function
SigGen.write('SWE:STAT ON')  # Enable frequency sweep
SigGen.write('SWE:SPAC LIN')  # Select linear sweep mode
SigGen.write('FREQ:STAR 1000')  # Set start frequency to 1 kHz
SigGen.write('FREQ:STOP 10000')  # Set stop frequency to 10 kHz
SigGen.write('SWE:TIME 10')  # Set sweep time to 10 s
SigGen.write('TRIG:SOUR IMM')  # Select internal trigger source
SigGen.write('OUTP ON')  # Enable output connector of CH1
