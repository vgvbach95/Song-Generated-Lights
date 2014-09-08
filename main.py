from tQueue import tQueue
import sys, random
from oscapi import ColorsOut
from ring import Ring
from cycle import Cycle
from wave import Wave

ringWake = 50.0
cycleWake = 50.0
waveWake = 60.0

def fadeToColor(wake, pixel, backC):
	if pixel[0] - wake > backC[0]:
		pixel = (pixel[0]-wake, pixel[1], pixel[2])
	elif pixel[0] + wake < backC[0]:
		pixel = (pixel[0]+wake, pixel[1], pixel[2])
	else:
		pixel = (backC[0], pixel[1], pixel[2])
	if pixel[1] - wake > backC[1]:
		pixel = (pixel[0], pixel[1]-wake, pixel[2])
	elif pixel[1] + wake < backC[1]:
		pixel = (pixel[0], pixel[1]+ wake, pixel[2])
	else:
		pixel = (pixel[0], backC[1], pixel[2])
	if pixel[2] - wake > backC[2]:
		pixel = (pixel[0], pixel[1], pixel[2]-wake)
	elif pixel[2] + wake < backC[2]:
		pixel = (pixel[0], pixel[1], pixel[2] + wake)
	else:
		pixel = (pixel[0], pixel[1], backC[2])
	return pixel

def ringProcess(ring, color, backC):
	toBeChanged = ring.getRing()
	length = ring.ringSize()
	while length != 0 :
		index = toBeChanged.get()
		pix[index] = color
		length = length - 1

	prevRing = ring.prevRings()
	length = prevRing.getSize()
	while length != 0:
		index = prevRing.get()
		pix[index] = fadeToColor(ringWake, pix[index], backC)
		length = length -1
	if ring.isDone() != True:
		ring.advanceRing()

def cycleProcess(cycle, color, backC):	
	prev = cycle.prevCycle()
	for x in prev:
		pix[x] = fadeToColor(cycleWake, pix[x], backC)
	toBeChanged = cycle.currCycle()
	for it in toBeChanged:
		pix[it] = color
	cycle.cycleAdvance()

def waveProcess(wave, color, backC):
	prev = wave.prevWave()
	for x in prev:
		pix[x] = fadeToColor(waveWake, pix[x], backC)
	toBeChanged = wave.currWave()
	for it in toBeChanged:
		pix[it] = color
	wave.advanceWave()

if __name__ == "__main__":
	import time
	from decimal import Decimal
	from random import randint
	fourCounter = 0
	out = ColorsOut()
	pix = [(0.0,0.0,0.0)]*48
	ring = [Ring(0)]*5
	waveF = Wave(False)
	waveT = Wave(True)
	cycleF = Cycle(False)
	cycleT = Cycle(True)
	nice_pixels = [
		(424.0, 360.0, 820.0), # light purple blue  A 0
		(212.0, 160.0, 620.0), # darker Version of above A 1
		(724.0, 504.0, 880.0), # light pink purple F 2
		(524.0, 304.0, 680.0), # F 3
		(1023.0, 732.0,788.0), # light pink red D 4
		(823.0, 532.0, 588.0), # D 5
		(616.0, 824.0, 940.0), # very light blue to teal B 6
		(416.0, 624.0, 740.0), # B 7
		(932.0, 600.0, 488.0), # light burnt orange grad C 8
		(732.0, 400.0, 288.0), # C 9
		(116.0, 164.0, 324.0), # quick blue purple to dark blue A 10
		(784.0, 864.0, 904.0), # light light blue to steel blue B 11
		(584.0, 664.0, 704.0), # B 12
		(728.0, 408.0, 440.0), # pink to red D 13
		(528.0, 208.0, 220.0), # D 14
		(924.0, 636.0, 784.0), # light pink to rose D 15
		(724.0, 436.0, 584.0), # D 16
		(364.0, 200.0, 344.0), # light purple to dark quick E 17
		(164.0, 0.0, 144.0), # E 18
		(532.0, 384.0, 544.0), # light purple to dark grad E 19
		(332.0, 184.0, 344.0), # E 20
		(1000.0, 512.0, 456.0), # salmon to burnt orange long C 21
		(800.0, 312.0, 256.0), # C 22
		(0.0,0.0,0.0) #Black 23
	]
	
	pattern = open('animations/pool/pattern1.txt', 'r')
	beat = int(pattern.readline())
	
	timer = 0
	ringCounter = 0
	colorBack = 23
	colorFront = 16
	while True:
		if timer == beat:
			ring[ringCounter] = Ring(randint(0,47))
			beat = int(pattern.readline())
			ringCounter += 1
			if ringCounter == 5:
				ringCounter = 0
		if timer % 200 == 0:
			for r in ring:
				ringProcess(r, nice_pixels[colorFront], nice_pixels[colorBack])
		out.write(pix)
		timer += 1






