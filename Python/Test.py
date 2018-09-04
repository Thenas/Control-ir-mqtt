import Control_IR as ctrl 

inFocus = ctrl.ControlMQTT("broker.mqttdashboard.com",topic="test1")
inFocus.addButton(0x20250AF,"Apagar")
inFocus.PushButton("Apagar")
print("ok")