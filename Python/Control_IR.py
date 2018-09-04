import paho.mqtt.client as mqtt
class ControlMQTT(object):
    def __init__(self,host,topic="raiz"):
        self.NumButtons = 0
        self.buttons ={}
        self.client = mqtt.Client("Control")
        self.topic = topic
        self.host = host
        try:
            client.Conect(host)
        except expression as identifier:
            print(identifier)
        

    def addButton(code=None, ButtonName=None):
        if code is None or ButtonName is None: 
            print("Error: Codigo y/o Nombre vacios")
            return 0
        else:
            self.buttons[str(ButtonName)] = str(code)
            self.NumButtons+=1
            return 1 

    def PushButton(ButtonName):
        client.publish(self.topic,self.buttons[ButtonName])
     
    
        