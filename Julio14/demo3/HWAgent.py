import re, serial
import datetime, time
import spade

class agente(spade.Agent.Agent):

    class leeSensoresNinja(spade.Behaviour.Behaviour):
        def onStart(self):
            self.movimiento = datetime.datetime.now()
	    self.movimiento2 = datetime.datetime.now()
	
            self.myAgent.puerto = serial.Serial('/dev/ttyO1', 9600, timeout=1)
            print "Inicia proceso de lectura..."

        def _process(self):
            linea = self.myAgent.puerto.readline()
#            if linea != "":
#                print "Linea: " + linea
            print linea            
            	    
            if len(linea) > 3:
		#self.myAgent.banMsg = True
                expreReg = re.compile('({|}|\[|\]|\")')
                linea = expreReg.sub("",linea)
		#print "linea: ", linea
                linea = linea.split(',')
		#print "linea: ", linea
                puertoSensor =  linea[2].split(':')
		print "puerto sensor: ",puertoSensor	
                valorSensor = linea[3].split(':')
		#print "valor sensor: ", valorSensor
                print "valor strip: ", valorSensor[1].strip()

                if puertoSensor[1] == "31":
                	temp = valorSensor[1]
                    	print "La temperatura es: " +  temp + "\n"
		    	if self.myAgent.banMsgTemperatura:
		    		
				receiver = self.myAgent.senderTemperatura
				self.msgS = spade.ACLMessage.ACLMessage()
				self.msgS.setPerformative("inform")
				self.msgS.setOntology(self.myAgent.msgR.getOntology())
				self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
				self.msgS.addReceiver(receiver)
				self.msgS.setContent(temp)
				self.myAgent.send(self.msgS)	
		#lectura movimiento 1
                elif puertoSensor[1] == "11" and valorSensor[1].strip() == "110101010101010101010101":
                	print "movimiento 1"
			if self.myAgent.banMsgMovimiento:
				aux = datetime.datetime.now()
                        	seg = int(self.movimiento.strftime("%S")) - int(aux.strftime("%S"))
                        	if abs(seg) > 4:
                            		self.movimiento = datetime.datetime.now()
                            		fecha = self.movimiento.strftime("%d/%m/%Y-%H:%M:%S")
                            		print "Movimiento el: " + fecha + "\n"
 			   
                            		receiver = self.myAgent.senderMovimiento
                            		self.msgS = spade.ACLMessage.ACLMessage()
                            		self.msgS.setPerformative("inform")
                            		self.msgS.setOntology(self.myAgent.msgR.getOntology())
                            		self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
                            		self.msgS.addReceiver(receiver)
                            		self.msgS.setContent(fecha)
                            		self.myAgent.send(self.msgS)
			

		# lectura movimiento 2
		elif puertoSensor[1] == "11" and valorSensor[1].strip() == "010101010101110101010101":
			print "movimiento 2"
			if self.myAgent.banMsgMovimiento2:
				print "1"
				aux = datetime.datetime.now()
				seg = int(self.movimiento2.strftime("%S")) - int(aux.strftime("%S"))
				print "2"
				if abs(seg) > 4:
					print "3"
					self.movimiento2 = datetime.datetime.now()
					print "4"
					fecha = self.movimiento2.strftime("%d/%m/%Y-%H:%M:%S")
					print "movimiento el: " + fecha + "\n"
					print "5"	
					receiver = self.myAgent.senderMovimiento2
					print "6"
					self.msgS = spade.ACLMessage.ACLMessage()
					print "7"
					self.msgS.setPerformative("inform")
					print "8"
					self.msgS.setOntology(self.myAgent.msgR.getOntology())
					print "9"
					self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
					print "10"
					self.msgS.addReceiver(receiver)
					print "11"
					self.msgS.setContent(fecha)
					print "12"
					self.myAgent.send(self.msgS)
					print "13"
			    
            	# lectura boton	    		                
                elif puertoSensor[1] == "11" and valorSensor[1].strip() == "010111010100010100110000":
                    	print "boton " + str(datetime.datetime.now())
                    	if self.myAgent.banMsgBoton:
				print "boton"
                        
                        	self.movimiento = datetime.datetime.now()
                        	fecha = self.movimiento.strftime("%d/%m/%Y-%H:%M:%S")
                        	print "boton el: " + fecha + "\n"
                        	receiver = self.myAgent.senderBoton
                        	self.msgS = spade.ACLMessage.ACLMessage()
                        	self.msgS.setPerformative("inform")
                        	self.msgS.setOntology(self.myAgent.msgR.getOntology())
                        	self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
                        	self.msgS.addReceiver(receiver)
                        	self.msgS.setContent(fecha)
                        	self.myAgent.send(self.msgS)
               

		#lectura de switch 1 ON
		elif puertoSensor[1] == "11" and valorSensor[1].strip() == "001100101001000001111111":
			print "switch 1 On"
			if self.myAgent.banMsgSwitchOn:
				
				
				receiver = self.myAgent.senderSwitchOn
				#print "1"
				self.msgS = spade.ACLMessage.ACLMessage()
				#print "2"
				self.msgS.setPerformative("inform")
				#print "3"
				self.msgS.setOntology(self.myAgent.msgR.getOntology())
				#print "4"
				self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
				#print "5"
				self.msgS.addReceiver(receiver)
				#print "6"
				self.msgS.setContent("ON")
				#print "7"
				self.myAgent.send(self.msgS)
		
		#lectura de switch 1 OFF
		elif puertoSensor[1] == "11" and valorSensor[1].strip() == "001100101001000001110111":
			print "switch 1 OFF"
			if self.myAgent.banMsgSwitchOff:
				receiver = self.myAgent.senderSwitchOff
				self.msgS = spade.ACLMessage.ACLMessage()
				self.msgS.setPerformative("inform")
				self.msgS.setOntology(self.myAgent.msgR.getOntology())
				self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
				self.msgS.addReceiver(receiver)
				self.msgS.setContent("OFF")
				self.myAgent.send(self.msgS)
			             
		# lectura de Puerta Abierta
		elif puertoSensor[1] == "11" and valorSensor[1].strip() == "010011000111000101010000":
			print "puerta abierta"
			if self.myAgent.banMsgPuerta:
				receiver = self.myAgent.senderPuerta
				self.msgS = spade.ACLMessage.ACLMessage()
				self.msgS.setPerformative("inform")
				self.msgS.setOntology(self.myAgent.msgR.getOntology())
				self.msgS.setLanguage(self.myAgent.msgR.getLanguage())
				self.msgS.addReceiver(receiver)
				self.msgS.setContent("Puerta Abierta")
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
          #      self.myAgent.msgR = None
                   
   
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
	    
	    sensor = self.myAgent.msgR.getContent()
	    #sensor Movimiento
	    if (sensor == "movimiento"):
		self.myAgent.banMsgMovimiento = True
		self.myAgent.senderMovimiento = self.myAgent.msgR.getSender()
	    #sensor Boton
	    elif (sensor == "boton"):
		self.myAgent.banMsgBoton = True
		self.myAgent.senderBoton = self.myAgent.msgR.getSender()
	    #sensor temperatura
	    elif (sensor == "temperatura"):
		self.myAgent.banMsgTemperatura = True
		self.myAgent.senderTemperatura = self.myAgent.msgR.getSender()
	    #sensor switchOn
  	    elif (sensor == "SwitchOn"):
		self.myAgent.banMsgSwitchOn = True
		self.myAgent.senderSwitchOn = self.myAgent.msgR.getSender()
	    #sensor SwitchOff
	    elif (sensor == "SwitchOff"):
		self.myAgent.banMsgSwitchOff = True
		self.myAgent.senderSwitchOff = self.myAgent.msgR.getSender()
	    #sensor Puerta	
	    elif (sensor == "PuertaAbierta"):
		self.myAgent.banMsgPuerta = True
		self.myAgent.senderPuerta = self.myAgent.msgR.getSender()
	    #sensor Movimiento 2
	    elif (sensor == "movimiento2"):
		self.myAgent.banMsgMovimiento2 = True
		self.myAgent.senderMovimiento2 = self.myAgent.msgR.getSender()		
        else:
                print "No hay suscriptores"    
       

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

    '''        
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
    '''
    def _setup(self):
        self.banMsgMovimiento = False
	self.banMsgBoton = False
	self.banMsgSwitchOn = False
	self.banMsgSwitchOff = False
	self.banMsgTemperatura = False
	self.banMsgPuerta = False
	self.banMsgMovimiento2 = False	
	
	self.sendeTemperatura = None
	self.senderMovimiento = None
	self.senderBoton = None
	self.senderSwitchOn = None
	self.senderSwitchOff = None
	self.senderPuerta = None
	self.senderMovimiento2 = None	

        self.msgR = None
        self.temperatura1 = 0
	self.temperatura2 = 0 
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
        '''
        tem = spade.Behaviour.ACLTemplate()
        sender = spade.AID.aid(name="openhab@lujan.mx/Smack", 
            addresses=["xmpp://openhab@lujan.mx/Smack"])
        tem.setSender(sender)
        #tem.setPerformative("")
        mt = spade.Behaviour.MessageTemplate(tem)
        self.addBehaviour(self.mensajeOpenHab())
        '''
if __name__ == "__main__":
   objAgente = agente("agentehw@lujan.mx", "agentehw")
#   objAgente = agente("danielAgente1@jabberes.org", "agente1")
#   objAgente = agente("danielAgente1@ubuntu-jabber.net", "agente1")
   objAgente.start()

