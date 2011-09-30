# window_monitor_test.py
import pyglet

screen_l = pyglet.window.get_platform().get_default_display().get_screens()

window_l = []

print pyglet.version
print """

This tests whether pyglet can put new windows on other monitors

*note* if you get a beach ball on the mac, click back in the console

"""

print screen_l

print "You have %d screens, 0 ... %d" % ( len( screen_l), len( screen_l) - 1)

while True:
        screen_index = int( raw_input("enter a number between 0 and %d, inclusive " % ( len(screen_l) - 1)))
        print "Using screen", screen_l[ screen_index]

        window_l.append( pyglet.window.Window( screen=screen_l[ screen_index], visible=False))
        print "created window on screen", window_l[-1].screen
        print "showing ..."
        window_l[ -1].set_visible() 
