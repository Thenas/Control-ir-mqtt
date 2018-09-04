import paho.mqtt.client as mqtt
class ControlMQTT(object):
    def __init__(self,host,topic="raiz"):
        self.NumButtons = 0
        self.buttons ={}
        self.client = mqtt.Client("Control")
        self.topic = topic
        self.host = host
        try:
            self.client.connect(self.host)
        except ValueError as e:

            print("Algo salio mal :( error" + str(e))


            
    """ Metodos """
    def addButton(self,code=None, ButtonName=None):
        if code is None or ButtonName is None: 
            print("Error: Codigo y/o Nombre vacios")
            return 0
        else:
            self.buttons[str(ButtonName)] = code
            self.NumButtons+=1
            return 1 

    def PushButton(self,ButtonName):
        self.client.publish(self.topic,self.buttons[ButtonName])
     
    
        