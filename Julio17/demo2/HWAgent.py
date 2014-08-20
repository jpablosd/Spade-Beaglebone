import re, serial
import datetime, time
import spade

class agente(spade.Agent.Agent):

    class leeSensoresNinja(spade.Behaviour.Behaviour):
        def onStart(self):
            self.movimiento = datetime.datetime.now()
            self.myAgent.puerto = serial.Serial('/dev/ttyO1', 9600, timeout=1)
            print "Inicia proceso de lectura..."

        def _process(self):
            linea = self.myAgent.puerto.readline()
#            if linea != "":
#                print "Linea: " + linea
            print linea            
	    
            if len(linea) > 3:
                expreReg = re.compile('({|}|\[|\]|\")')
                linea = expreReg.sub("",linea)
		print "linea: ", linea
                linea = linea.split(',')
		print "linea: ", linea
                puertoSensor =  linea[2].split(':')
		print "puerto sensor: ",puertoSensor	
                valorSensor = linea[3].split(':')
		print "valor sensor: ", valorSensor
                print "valor strip: ", valorSensor[1].strip()
                if puertoSensor[1] == "31":
                    self.myAgent.temperatura = valorSensor[1]
                    print "La temperatura es: " +  self.myAgent.temperatura + "\n"

                elif puertoSensor[1] == "11" and valorSensor[1].strip() == "010101010101010101010101":
                    if self.myAgent.banMsg:
                        print "hola movimiento"
			aux = datetime.datetime.now()
                        seg = int(self.movimiento.strftime("%S")) - int(aux.strftime("%S"))
                        if abs(seg) > 4:
                            self.movimiento = datetime.datetime.now()
                            fecha = self.movimiento.strftime("%d/%m/%Y-%H:%M:%S")
                            print "Movimiento el: " + fecha + "\n"
                            receiver = self.myAgent.msgR.getSender()
                            self.msgS = spade.ACLMessage.ACLMessage()
                            self.msgS.setPerformative("inform")
                            self.msgS.setOntology(self.myAgent.msgR.getOntology())
                            self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
                            self.msgS.addReceiver(receiver)
                            self.msgS.setContent(fecha)
                            #self.myAgent.send(self.msgS)
                        
                elif puertoSensor[1] == "11" and valorSensor[1].strip() == "010111010100010100110000":
                    print "boton " + str(datetime.datetime.now())
                    if self.myAgent.banMsg:
                        self.movimiento = datetime.datetime.now()
                        fecha = self.movimiento.strftime("%d/%m/%Y-%H:%M:%S")
                        print "boton el: " + fecha + "\n"
                        receiver = self.myAgent.msgR.getSender()
                        self.msgS = spade.ACLMessage.ACLMessage()
                        self.msgS.setPerformative("inform")
                        self.msgS.setOntology(self.myAgent.msgR.getOntology())
                        self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
                        self.msgS.addReceiver(receiver)
                        self.msgS.setContent(fecha)
                        self.myAgent.send(self.msgS)
                    
#            self.myAgent.msgR = self._receive(True, 10)
        
#            if self.myAgent.msgR:
#                print "Mensaje recibido!"
#                print self.myAgent.msgR
#                mensaje = self.myAgent.msgR.split("<body>")
#                print mensaje[0]
#                print mensaje[1]
                #if self.myAgent.msgR.getType() == "chat":
                #    print "Mensaje de OpenHab"
#                self.myAgent.msgR = None
                   
   
    class recibeSubscripcion(spade.Behaviour.EventBehaviour):

      def _process(self):
        self.myAgent.msgR = self._receive(False)
        
        if self.myAgent.msgR:
            print "Mensaje de subscripcion recibido!"
            print "Enviando respuesta"
            receiver = self.myAgent.msgR.getSender()
            self.msgS = spade.ACLMessage.ACLMessage()
            self.msgS.setPerformative("accept")
            self.msgS.setOntology(self.myAgent.msgR.getOntology())
            self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
            self.msgS.addReceiver(receiver)
            self.msgS.setContent("Recibira notificaciones de %s" % self.myAgent.msgR.getContent())
            self.myAgent.send(self.msgS)
            print "Mensaje de subscripcion enviado"
            self.myAgent.banMsg = True
        else:
                print "No hay mensajes"    
       

    class recibeSolicitud(spade.Behaviour.EventBehaviour):

      def _process(self):
        self.msgR = self._receive(False)
        
        if self.msgR:
            if self.msgR.getOntology() == "vote":
                print "Mensaje de solicitud recibido!"
                print "Enviando respuesta"
                receiver = self.msgR.getSender()
                self.msgS = spade.ACLMessage.ACLMessage()
                self.msgS.setPerformative("inform")
                self.msgS.setOntology(self.msgR.getOntology())
                self.msgS.setLanguage(self.msgR.getLanguage())
                self.msgS.addReceiver(receiver)
                a = float(self.myAgent.temperatura)
                print a
                if a > 22:
                    self.msgS.setContent("si")
                    print "yo voto que si y la temperatura es: " + self.myAgent.temperatura
                else:
                    self.msgS.setContent("no")
                    print "yo voto que no y la temperatura es: " + self.myAgent.temperatura
                self.myAgent.send(self.msgS)
            elif self.msgR.getOntology() == "switch":
                if self.msgR.getContent() == "prende":
                    print "prende dispositivo"
                    self.myAgent.puerto.write("{\"DEVICE\":[{\"G\":\"0\",\"V\":0,\"D\":11,\"DA\":\"001100101001000001111111\"}]}\r\n")
            else:
                print "apaga dispositivo"
                self.myAgent.puerto.write("{\"DEVICE\":[{\"G\":\"0\",\"V\":0,\"D\":11,\"DA\":\"001100101001000001110111\"}]}\r\n")
                print "se apago"
        else:
            print "No hay mensajes"    

            
    class mensajeOpenHab(spade.Behaviour.EventBehaviour):

      def _process(self):
        print "Mensaje detectado"
        self.myAgent.msgR = self._receive(False)
         
        if self.myAgent.msgR:
            print "Mensaje de subscripcion recibido!"
            print "Enviando respuesta"
            receiver = self.myAgent.msgR.getSender()
            self.msgS = spade.ACLMessage.ACLMessage()
            self.msgS.setPerformative("accept")
            self.msgS.setOntology(self.myAgent.msgR.getOntology())
            self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
            self.msgS.addReceiver(receiver)
            self.msgS.setContent("Recibira notificaciones de %s" % self.myAgent.msgR.getContent())
            self.myAgent.send(self.msgS)
            print "Mensaje de subscripcion enviado"
            self.myAgent.banMsg = True
        else:
                print "No hay mensajes"    

    def _setup(self):
        self.banMsg = False
        self.msgR = None
        self.temperatura = "0"
        self.puerto = None

        self.setDefaultBehaviour(self.leeSensoresNinja())

        tem = spade.Behaviour.ACLTemplate()
        tem.setPerformative("subscribe")
        mt = spade.Behaviour.MessageTemplate(tem)
        self.addBehaviour(self.recibeSubscripcion(),mt)

        tem = spade.Behaviour.ACLTemplate()
        tem.setPerformative("request")
        mt = spade.Behaviour.MessageTemplate(tem)
        self.addBehaviour(self.recibeSolicitud(),mt)

        tem = spade.Behaviour.ACLTemplate()
        sender = spade.AID.aid(name="openhab@lujan.mx/Smack", 
            addresses=["xmpp://openhab@lujan.mx/Smack"])
        tem.setSender(sender)
        #tem.setPerformative("")
        mt = spade.Behaviour.MessageTemplate(tem)
        self.addBehaviour(self.mensajeOpenHab())

if __name__ == "__main__":
   objAgente = agente("agentehw@lujan.mx", "agentehw")
#   objAgente = agente("danielAgente1@jabberes.org", "agente1")
#   objAgente = agente("danielAgente1@ubuntu-jabber.net", "agente1")
   objAgente.start()

