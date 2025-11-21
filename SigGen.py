import pyvisa
import time

rm = pyvisa.ResourceManager()
SigGen = rm.open_resource('TCPIP0::192.168.0.70::INSTR')

SigGen.query('*IDN?')
SigGen.write('FUNC SIN')
SigGen.write('SWE:STAT ON')
SigGen.write('SWE:SPAC LIN')
SigGen.write('FREQ:STAR 1000')
SigGen.write('FREQ:STOP 1000000')
SigGen.write('SWE:TIME 10')
SigGen.write('TRIG:SOUR IMM')
SigGen.write('OUTP ON')
