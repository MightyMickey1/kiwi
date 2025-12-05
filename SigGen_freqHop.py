import pyvisa
import time

freqHop = [13.6, 14.5, 16, 10, 11.7]

rm = pyvisa.ResourceManager()
SigGen = rm.open_resource('TCPIP0::192.168.0.70::INSTR')

ID = SigGen.query('*IDN?')
print(ID);
SigGen.write('FUNC SIN')
SigGen.write(f'FREQ {freqHop[0] * pow(10, 6)}')
SigGen.write('VOLT:UNIT VPP')
SigGen.write('VOLT 0.2')
SigGen.write('VOLT:OFFS 0')
SigGen.write('PHAS 0')
SigGen.write('OUTP ON')

for freq in freqHop
    SigGen.write('OUTP OFF')
    SigGen.write(f'FREQ {freq * pow(10, 6)}')
    SigGen.write('OUTP ON')
