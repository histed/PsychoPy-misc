#!/usr/bin/env python2.6

from psychopy import visual, core, monitors #import some libraries from PsychoPy
import numpy as np
import time

# monitor setup
#sz = [800,600]
sz = [1680,1050]
#mon = monitors.Monitor('SamsungSZ', width=48.3, distance=25.0, gamma=1.0, size=1600, verbose=True)
mon = monitors.Monitor('test')


win = visual.Window(sz,
                    fullscr=True, #False, 
                    screen=0, 
                    monitor=mon, 
                    winType='pyglet', 
                    units="deg")

win.setRecordFrameIntervals(True);



#create some stimuli

#fixation = visual.PatchStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

#draw the stimuli and update the window
tempFreqHz = 2
frameRateHz = 60
oris = np.r_[0:360:45]
waitTimeS = 1
sfCPD = 20

def drawOneGrating(pTempFreqHz, pNFrames, pOri, waitTimeS):
    stT = time.time()

    grating = visual.PatchStim(win=win, mask="circle", size=200, pos=[0,0], sf=1.0/sfCPD, ori=pOri)
    cyclesPerFrame = 1.0 / (frameRateHz / tempFreqHz)
    print(cyclesPerFrame)

    # wait on a gray screen
    while (time.time() - stT) < waitTimeS:
        pass
    
    grating.draw()
    lastFrT = time.time()
    win.flip()

    for frameN in range(pNFrames-1):
        timeEl = time.time() - lastFrT
        grating.setPhase(tempFreqHz*timeEl, '+')#advance phase by 0.05 of a cycle
        print tempFreqHz*timeEl
        lastFrT = time.time()
        grating.draw()
        #core.wait(0.01)
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
