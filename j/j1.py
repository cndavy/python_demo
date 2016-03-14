__author__ = 'han'
import java
from java import awt
java.lang.System.out.println('Heelooo')
def exit(e): java.lang.System.exit(0)
frame = awt.Frame('AWT Example', visible=1)

button = awt.Button('Close Me!', actionPerformed=exit)

frame.add(button, 'Center')
frame.pack()


from pawt import swing

swing.test()