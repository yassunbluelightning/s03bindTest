#s03bindTest.py
import pj
import pjTkInter as tk
import pjSound as sound
from logStdErr import logStdErrClass
lse=logStdErrClass()
lse.setProjectName("s03bindTest")
lse.errToFile()
####
tk.stopTkTimer() ####Avoid influence from the OtherApp Which Uses Timer in the Same Project;YassunAdd;2025-1001;;
tk.updateMainLabel("s03bindTest")
tk.title("This shows some of Touched, Touch Moved, Button Pressed and KeyPressed.")
tk.removeAllFromCanvas()

def keyPress(eventKeySym):
  tk.updateMainLabel("eventKeySym:" + eventKeySym)

def button(eventNum):
  tk.updateMainLabel("eventNum:" + str(eventNum))

def motion(eventX, eventY):
  tk.updateMainLabel("(eventX,eventY):("+ str(eventX) + "," + str(eventY) + ")" )

def motionCanvas(evCanvasX, evCanvasY):
  tk.updateMainLabel("(evCanvasX,evCanvasY):(" + str(evCanvasX) + "," + str(evCanvasY) + ")" )

tk.bindKeyPressFunction("s03bindTest:s03bindTest.keyPress")

tk.bindButtonFunction("s03bindTest:s03bindTest.button")

tk.bindMotionFunction("s03bindTest:s03bindTest.motion")

tk.bindMotionCanvasFunction("s03bindTest:s03bindTest.motionCanvas")

####tk.startTimerFunctionAfter("s03bindTest:s03bindTest.gameLoop", 0.2)
