import Control_IR as ctrl
control_inFocus = ctrl.ControlMQTT("192.168.0.11")
control_inFocus.addButton("0x05456654","Apagar")
control_inFocus.PushButton("Apagar")
"hola"