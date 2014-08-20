# PROBANDO PYTHON Y AGENTES

#    a.ninja.is
#    jolish@gmail.comp
#    1j0o6r
#   ssh ubuntu@ip
#    temppwd

import re

#----------------------MENSAJE---------------------
linea = '<message xmlns="jabber:client" to="agentehw@lujan.mx" from="openhab@lujan.mx/Smack" id="3LPSp-106" type="chat"><body>luz apagada</body><thread>03x3873</thread></message>'
if len(linea)>3:
    expreReg = re.compile('<|>|=|"|:|/| ')
    linea = expreReg.sub("",linea)
    linea = linea.split('body')
    mesaje = linea[1].split('body')
    print "mensaje: "
    print mesaje[0]

#---------------------REMITENTE--------------------
print ""
linea = '<message xmlns="jabber:client" to="agentehw@lujan.mx" from="openhab@lujan.mx/Smack" id="3LPSp-106" type="chat"><body>luz apagada</body><thread>03x3873</thread></message>'
if len(linea)>3:
    expreReg = re.compile('<|>|:|/| ')
    linea = expreReg.sub("",linea)
    linea = linea.split('"')
    sender = linea[5].split('Smack')
    sender = sender[0].split(',')
    print "Enviado por: "
    print sender[0]

