
import borunte

IP = "192.168.3.1"
# IP = "127.0.0.1"
PORT = 9760

robot = borunte.Borunte(IP,PORT)
robot.open()
# robot.version()
#robot.getAxisPosition(1)
robot.position(0,200,900,40,0,0)
#robot.setIO(4,6,1)
robot.close()
