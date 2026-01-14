
import borunte

# IP = "192.168.3.1"
IP = "127.0.0.1"
PORT = 9760

robot = borunte.Borunte(IP,PORT)
robot.open()
# robot.version()
# robot.getAxisPosition(0)
robot.position(16,114,849,39,3.9,-9.7)
robot.setIO(4,6,1)
robot.close()