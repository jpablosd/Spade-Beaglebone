# PROBANDO PYTHON Y AGENTES

#    a.ninja.is
#    jolish@gmail.comp
#    1j0o6r
#   ssh ubuntu@ip
#    temppwd

#MENSAJE EJEMPLO:   "{\"DEVICE\":[{\"G\":\"0\",\"V\":0,\"D\":11,\"DA\":\"001100101001000001110111\"}]}\r\n
#expreReg = re.compile('({|}|\[|\]|\")')

#MENSAJE NUESTRO: <message xmlns="jabber:client" to="agentehw@lujan.mx" from="openhab@lujan.mx/Smack" id="3LPSp-106" type="chat"><body>luz apagada</body><thread>03x3873</thread></message>'

import re


linea = '<message xmlns="jabber:client" to="agentehw@lujan.mx" from="openhab@lujan.mx/Smack" id="3LPSp-106" type="chat"><body>luz apagada</body><thread>03x3873</thread></message>'
if len(linea)>3:
    expreReg = re.compile('<|>|=|"|:|/| ')
    linea = expreReg.sub("",linea)
    linea = linea.split('body')
    mesaje = linea[1].split('body')
    print "mensaje: "
    print mesaje


print ""
linea = '<message xmlns="jabber:client" to="agentehw@lujan.mx" from="openhab@lujan.mx/Smack" id="3LPSp-106" type="chat"><body>luz apagada</body><thread>03x3873</thread></message>'
if len(linea)>3:
    expreReg = re.compile('<|>|:|/| ')
    linea = expreReg.sub("",linea)
    linea = linea.split('"')
    sender = linea[5].split('Smack')
    sender = sender[0].split(',')
    print "Enviado por: "
    print sender

