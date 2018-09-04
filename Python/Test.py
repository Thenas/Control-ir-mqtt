import Control_IR as ctrl 

inFocus = ctrl.ControlMQTT("broker.mqttdashboard.com",topic="testtopic/1")
inFocus.addButton("0xE172E817","Apagar")
inFocus.PushButton("Apagar")
print("ok")