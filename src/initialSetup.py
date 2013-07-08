import clock
import continousAsignation
import cpu
import hdd
import io
import irq
import kernel
import memory
import pcb
import programInstruction
import resourcesManager
import scheduler
import shell
import timer
import mmu

aScheduler = scheduler.Fifo()
aMemory = memory.Memory(50)
aFit = continousAsignation.FirstFit()
anAsignation = continousAsignation.ContinousAsignation(aMemory, aFit)
aMMU = mmu.MMU(anAsignation)
anIRQ = irq.IRQ()
anIRQHandler = irq.IRQHandler(anIRQ)
anIO = io.IO(anIRQ)
aCPU = cpu.CPU(anIRQ)
aTimer = timer.Timer(anIO, aCPU, 3)
aClock = clock.Clock(aTimer)
aResourcesManager = resourcesManager.ResourcesManager(anIO, aCPU, aMMU)
aShell = shell.Shell()

aKernel = kernel.Kernel(aScheduler, anIRQ, aResourcesManager, aShell)

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

aKernel.loadProgram(program1)
aKernel.loadProgram(program2)
aKernel.loadProgram(program3)

#for x in aMemory.memory:
#    print x

aClock.run()

