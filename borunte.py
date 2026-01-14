import socket
import json

class Borunte:
    def __init__(self,ip,port):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.addr = (ip,port)

    def open(self):
        self.s.connect(self.addr)

    def close(self):
        self.s.close()

    def send(self,json_to_send:dict):
        json_to_send["dsID"] = "HCRemoteMonitor"
        if("queryAddr" in json_to_send):
            json_to_send["cmdType"] = "query"
        else:
            json_to_send["cmdType"] = "command"
        self.s.send(bytes(json.dumps(json_to_send),"UTF-8"))
        received = json.loads(self.s.recv(1024).decode("UTF-8"))
        print ("Sent: {}".format(json_to_send))
        print ("Received: {}".format(received))
    def query(self,q:str):
        self.send({      
        "queryAddr":[q]
        })

    def version(self):
        self.query("version")

    def getAxisPosition(self,n:int):
        self.query(f"axis-{n}")
    
    def getPosition(self,n:int):
        self.query(f"world-{n}")

    def setIO(self,boardID:int,pin:int,enable:bool):
        #  "d1":输出板ID（0～3：IO板，4～6：M值，7：EUIO），"d2":输出点ID，"d3":输出状态（0：OFF，1：ON） 
        self.send({
             "cmdData":["modifyOutput",str(boardID),str(pin),"1" if enable else "0"]
        })

    def position(self,x:float,y:float,z:float,u:float,v:float,w:float):
        json_to_send = {         
        "cmdData":["rewriteDataList","800","6","0",
                   str(int(x*1000)),
                   str(int(y*1000)),
                   str(int(z*1000)),
                   str(int(u*1000)),
                   str(int(v*1000)),
                   str(int(w*1000))]
        }
        self.send(json_to_send)
