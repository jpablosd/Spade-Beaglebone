import spade

#     NOTIFICADOR 3

class MyAgent(spade.Agent.Agent):
	
	class Suscribir(spade.Behaviour.OneShotBehaviour):
        	def _process(self):
            		print "Requesting subscription to Movimiento 1 Agent..."
            		receiver = spade.AID.aid(name="amovimiento@lujan.mx/spade/", addresses=["xmpp://amovimiento@lujan.mx/spade/"])

                	# Second, build the message
            		self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            		self.msg.setPerformative("subscribe")        # Set the "inform" FIPA performative
            		self.msg.setOntology("AMITec")        # Set the ontology of the message content
            		self.msg.setLanguage("English")           # Set the language of the message content
            		self.msg.addReceiver(receiver)            # Add the message receiver
            		self.msg.setContent("movimiento")       # Set the message content

            		# Third, send the message with the "send" method of the agent
            		self.myAgent.send(self.msg)
			print "Subscription sent"
			
				
			print "Requesting subscription to Movimiento 2 Agent..."
            		receiver = spade.AID.aid(name="amovimiento2@lujan.mx/spade/", addresses=["xmpp://amovimiento2@lujan.mx/spade/"])

                	# Second, build the message
            		self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            		self.msg.setPerformative("subscribe")        # Set the "inform" FIPA performative
            		self.msg.setOntology("AMITec")        # Set the ontology of the message content
            		self.msg.setLanguage("English")           # Set the language of the message content
            		self.msg.addReceiver(receiver)            # Add the message receiver
            		self.msg.setContent("movimiento2")       # Set the message content

            		# Third, send the message with the "send" method of the agent
            		self.myAgent.send(self.msg)
			print "Subscription sent 2"

		
        class ReceiveBehav(spade.Behaviour.Behaviour):
                """This behaviour will receive all kind of messages"""
                def _process(self):
		      		
			#   RECIBIR MENSAJES DE OPENHAB
                        self.msg = self._receive(True,10)
                        #print "mensaje recibido"
                        #print self.msg
                        #print self.msg   
                        # Blocking receive for 10 seconds
                        # Check wether the message arrived
                        if self.msg:
                                #print "I got a message!"
                                try:
                                        if self.msg.getOntology() != "Presence":
                                                print "presencia msg"
                                                print self.msg
                                except:
                                        #print "except"
                                        #print self.msg
                                        linea = str(self.msg)
                                        if len(linea)>3:
                                            #print linea
                                            #expreReg = re.compile('<|>|=|"|:|/| ')
                                            #linea = expreReg.sub("",linea)
                                            linea = linea.split('<body>')
                                            #print linea
                                            mesaje = linea[1].split('</body>')
                                            #print mesaje
                                            print "mensaje: "
                                            print mesaje[0]

                                            if mesaje[0] == "luz apagada":
                                                print "envio mensaje de apagar luz a agenteSwitch"
						self.myAgent.enviarMensajeSwitchOFF()                                                

                                            else:
                                                print "mensaje diferente"
                        else:
                                print "I waited but got no message"
                        self.msg = None
			#   RECIBIR MENSAJES DE OPENHAB
 			
        class AnotherBehav(spade.Behaviour.Behaviour):
                """This behaviour will receive only messages of the 'cooking' ontology"""
                def _process(self):
                        self.msg = None
                        # Blocking receive indefinitely
                        self.msg = self._receive(True)
                        # Check wether the message arrived
                        if self.msg:
                                print "I got a cooking message!"
                        else:
                                print "I waited but got no cooking message"                             
	
		
	class recibeMovimiento(spade.Behaviour.EventBehaviour):
		def _process(self):
        		self.msgR = self._receive(False)
        
        		if self.msgR:
                		print "Mensaje de movimiento recibido!"
				#print self.msgR 
				receiver = self.msgR.getSender()
				#print receiver
				print ""
				#print "presencia"
				presence = self.msgR.getContent()
				#print presence
				print ""
				#              MOVIMIENTO 1
				if presence == "Movimiento1ON":
					print "hay Movimiento 1"
					self.myAgent.banMovimiento1 = True
					#print self.myAgent.banMovimiento1
					print ""
				if presence == "Movimiento1OFF":
					print "No hay movimiento 1"
					self.myAgent.banMovimiento1 = False
				
				#if ((presence != "Movimiento1ON") and (presence != "Movimiento1OFF")):
				#	print "mensaje de otro agente"
				#               MOVIMIENTO  2
				if presence == "Movimiento2ON":
					print "hay movimiento2"
					self.myAgent.banMovimiento2 = True
					print ""
				if presence == "Movimiento2OFF":
					print "No hay movimiento 2"
					self.myAgent.banMovimiento2 = False
				#if ((presence != "Movimiento2ON") and (presence != "Movimiento2OFF")):
				#	print "mensaje de otro agente"
			else:
				print "no hay mensajes"
	
	class recibeNotificacion(spade.Behaviour.EventBehaviour):
		def _process(self):
			self.msgR = self._receive(False)
			if self.msgR:
				print "peticion de notificacion recibida"
				receiver = self.msgR.getSender()
				notificacion = self.msgR.getContent()
				self.myAgent.notificacion = notificacion
				self.myAgent.banNotificacion = True
				#print receiver
				#print self.myAgent.banNotificacion
				print ""
				
				
				if self.myAgent.banNotificacion:
					#print "1"
					if self.myAgent.banMovimiento1:
						print "notificacion 1"
						self.myAgent.enviarMensajeSwitch()
						#self.myAgent.banMovimiento1 = False
					
					
					if self.myAgent.banMovimiento2:
						print "notificacion 2"
						#self.myAgent.banMovimiento2 = False
										 	
						receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                    				self.msgS = spade.ACLMessage.ACLMessage()
                    				self.msgS.setPerformative("help")
                    				self.msgS.addReceiver(receiver)
                    				self.msgS.setContent("say tocan el tiimbre")
                    				#print self.msgS.getContent()
                    				self.myAgent.send(self.msgS)
                    				print "aviso enviado a computador openhab"
	

					if ((self.myAgent.banMovimiento1 != True) and (self.myAgent.banMovimiento2 != True)):
						print "notificar al celular" 
				 	
						receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                    				self.msgS = spade.ACLMessage.ACLMessage()
                    				self.msgS.setPerformative("help")
                    				self.msgS.addReceiver(receiver)
                    				self.msgS.setContent("send boton ON")
                    				#print self.msgS.getContent()
                    				self.myAgent.send(self.msgS)
                    				print "boton ENCENDIDO enviado a openhab"
	
					
					self.myAgent.banNotificacion = False
	

	def enviarMensajeSwitch(self):
		receiver = spade.AID.aid(name="aswitch@lujan.mx/spade/", addresses=["xmpp://aswitch@lujan.mx/spade/"])
                # Second, build the message
            	self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            	self.msg.setPerformative("request")        # Set the "inform" FIPA performative
            	self.msg.setLanguage("English")           # Set the language of the message content
            	self.msg.addReceiver(receiver)            # Add the message receiver
            	self.msg.setContent("ON")        # Set the message content
            	self.send(self.msg)
            	print "Se envio el mensaje ON al switch"

	def enviarMensajeSwitchOFF(self):
		
		receiver = spade.AID.aid(name="aswitch@lujan.mx/spade/", addresses=["xmpp://aswitch@lujan.mx/spade/"])
                # Second, build the message
            	self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            	self.msg.setPerformative("request")        # Set the "inform" FIPA performative
            	self.msg.setLanguage("English")           # Set the language of the message content
            	self.msg.addReceiver(receiver)            # Add the message receiver
            	self.msg.setContent("apaga")        # Set the message content
            	self.send(self.msg)
            	print "Se envio el mensaje OFF al switch"


	
        def _setup(self):
                # Add the "ReceiveBehav" as the default behaviour
                print "setup iniciado"
		
		b = self.Suscribir()
        	self.addBehaviour(b, None)		

		self.notificacion = None
		self.banNotificacion = False

		self.banMovimiento1 = False
		self.banMovimiento2 = False
		        		
                rb = self.ReceiveBehav()
                self.setDefaultBehaviour(rb)
	
				
	
		tem = spade.Behaviour.ACLTemplate()
        	tem.setPerformative("inform")
		tem.setOntology("demo3")
        	mt = spade.Behaviour.MessageTemplate(tem)
        	self.addBehaviour(self.recibeMovimiento(),mt)
		
		tem = spade.Behaviour.ACLTemplate()
                tem.setPerformative("request")
                mt = spade.Behaviour.MessageTemplate(tem)
                self.addBehaviour(self.recibeNotificacion(),mt)

if __name__ == "__main__":
        a = MyAgent("anotificador@lujan.mx", "anotificador")
        a.start()
                
