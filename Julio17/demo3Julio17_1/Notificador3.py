import spade

#     NOTIFICADOR 3

class MyAgent(spade.Agent.Agent):
	
	class Suscribir(spade.Behaviour.OneShotBehaviour):
        	def _process(self):
            		print "Requesting subscription to Movimiento Agent..."
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

		
        class ReceiveBehav(spade.Behaviour.Behaviour):
                """This behaviour will receive all kind of messages"""
                def _process(self):
			if self.myAgent.banNotificacion:
				#print "1"
				if self.myAgent.banMovimiento1:
					print "notificacion 1"
					self.myAgent.enviarMensajeSwitch()
					#self.myAgent.banMovimiento1 = False
				if self.myAgent.banMovimiento2:
					print "notificacion 2"
					#self.myAgent.banMovimiento2 = False

				if ((self.myAgent.banMovimiento1 != True) and (self.myAgent.banMovimiento2 != True)):
					print "notificar al celular" 
				 
				self.myAgent.banNotificacion = False
	      
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
				print "presencia"
				presence = self.msgR.getContent()
				#print presence
				print ""
				if presence == "Movimiento1ON":
					print "hay Movimiento 1"
					self.myAgent.banMovimiento1 = True
					#print self.myAgent.banMovimiento1
					print ""
				if presence == "Movimiento1OFF":
					print "No hay movimiento 1"
					self.myAgent.banMovimiento1 = False
				#agregar movimiento 2

				if ((presence != "Movimiento1ON") and (presence != "Movimiento1OFF")):
					print "mensaje de otro agente"
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
                
