import clock
import timer
import cpu
import scheduler
import memory
import programInstruction
import pcb
import Queue

"""Instanciation of Kernel's components"""

memory = memory.Memory()
fifo = scheduler.Fifo()
cpu = cpu.CPU(fifo, memory)
timer = timer.Timer(cpu)
clock =  clock.Clock(timer)

"""Instantiation of program and some instructions"""

program1 = programInstruction.Program()
program2 = programInstruction.Program()
program3 = programInstruction.Program()
instruccion1 = programInstruction.IOInstruction()
instruccion2 = programInstruction.CPUInstruction()
instruccion3 = programInstruction.EndInstruction()

"""Matching up programs with instructions"""

program1.add(instruccion2)
program1.add(instruccion2)
program1.add(instruccion2)
program1.add(instruccion1)
program1.add(instruccion1)
program1.add(instruccion3)
program2.add(instruccion1)
program2.add(instruccion1)
program2.add(instruccion1)
program2.add(instruccion2)
program2.add(instruccion2)
program2.add(instruccion3)
program3.add(instruccion1)
program3.add(instruccion2)
program3.add(instruccion1)
program3.add(instruccion2)
program3.add(instruccion1)
program3.add(instruccion3)

"""Creating the 3 respective pcbs"""

pcb1 = pcb.PCB(1)
pcb2 = pcb.PCB(2)
pcb3 = pcb.PCB(3)

"""Loading the programs in memory"""

memory.loadProgram(program1, pcb1.getID())
memory.loadProgram(program2, pcb2.getID())
memory.loadProgram(program3, pcb3.getID())

"""Assigning the pcbs to the Scheduler"""

fifo.addProcess(pcb1)
fifo.addProcess(pcb2)
fifo.addProcess(pcb3)

"""Starting up the clock"""
clock.run()

