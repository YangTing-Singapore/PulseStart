from pymeasure.instruments.hp import HP81130A

pulse = HP81130A("GPIB0::10:INSTR")
print(pulse.id)