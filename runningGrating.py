#!/usr/bin/env python2.6

from psychopy import visual, core #import some libraries from PsychoPy
import numpy as np
import time

#sz = [1680,1050]
sz = [800,600]
win = visual.Window(sz,
                    fullscr=False, 
                    screen=0, 
                    monitor="test", 
                    winType='pygame', 
                    units="deg")

win.setRecordFrameIntervals(True);



#create some stimuli

#fixation = visual.PatchStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

#draw the stimuli and update the window
tempFreqHz = 2
frameRateHz = 60
oris = np.r_[0:360:45]
waitTimeS = 1

def drawOneGrating(pTempFreqHz, pNFrames, pOri, waitTimeS):
    stT = time.time()

    grating = visual.PatchStim(win=win, mask="circle", size=200, pos=[0,0], sf=0.05, ori=pOri)
    cyclesPerFrame = 1.0 / (frameRateHz / tempFreqHz)
    print(cyclesPerFrame)

    # wait on a gray screen
    while (time.time() - stT) < waitTimeS:
        pass
    
    grating.draw()
    win.flip()
    for frameN in range(pNFrames-1):
        grating.setPhase(cyclesPerFrame, '+')#advance phase by 0.05 of a cycle
        grating.draw()
        #fixation.draw()
        win.flip()

    grating.setContrast(0)
    grating.draw()
    win.flip()
    
    del(grating)


nFramesPerStim = 60
while True:  # run forever
    for tOri in oris:
        drawOneGrating(tempFreqHz, nFramesPerStim, tOri, waitTimeS)
    

#pause, so you get a chance to see it!
#core.wait(1.0)

#print(win.frameIntervals)

import numpy as np
print(np.mean(win.frameIntervals));
print(np.std(win.frameIntervals));
