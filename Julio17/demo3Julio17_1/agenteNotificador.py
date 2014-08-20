import spade

class MyAgent(spade.Agent.Agent):
        class ReceiveBehav(spade.Behaviour.Behaviour):
                """This behaviour will receive all kind of messages"""
                def _process(self):
                        print "process"
                        self.msg = self._receive(False)
                        print "mensaje recibido process"
                        print self.msg
				
			if self.myAgent.msgR:
	
	                    print "Mensaje recibido!"
         	            receiver = self.msg.getSender()
			    print receiver
                	    contenido = self.msg.setContent("self.myAgent.msgR.getContent()")
			    print contenido
                    	    ACLmessage = spade.ACLMessage.ACLMessage()
			    print "3"
                    	    performative = self.msg.setPerformative("inform")
			    print "4"
                    	    ontology = (self.msg.getOntology()) 
			    print "5"
                    	    language = (self.msg.getLanguage())
			    print "5"
			    print "mensaje recibido de: "
                  	    print receiver
		  	    print "contenido :"
                 	    print contenido
			
			    #self.msg = None

			
                        #print self.msg   
                        # Blocking receive for 10 seconds
                        # Check wether the message arrived
                        '''
                        if self.msg:
                                print "I got a message!"
                                try:
                                        if self.msg.getOntology() != "Presence":
                                                print "presencia msg"
                                                print self.msg
                                except:
                                        print "except"
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

                                            
                                            if mesaje[0] == "luz prendida":
                                                print "envio mensaje"
                                                #<message xmlns="jabber:client" to="juanpablo@lujan.mx" from="openhab@lujan.mx/Smack" id="0m7AJ-117" type="chat"><body>luz apagada</body><thread>lN9qH80</thread></message>
                                                receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                                                self.msgS = spade.ACLMessage.ACLMessage()
                                                self.msgS.setPerformative("help")
                                                self.msgS.addReceiver(receiver)
                                                self.msgS.setContent("say Se detecto un movimiento")
                                                self.myAgent.send(self.msgS)
                                                print "estado nuevo enviado"

                                            else:
                                                print "mensaje diferente"
                                                
                        else:
                                print "I waited but got no message"
                        self.msg = None
                        '''
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

        '''
        class recibeMensaje(spade.Behaviour.EventBehaviour):

              def _process(self):
                self.myAgent.msgR = self._receive(False)
                
                if self.myAgent.msgR:


                    
                    #self.myAgent.send(self.msgS)
                    #print "Mensaje de subscripcion enviado"
                
                                   
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
               
                    '''



        def _setup(self):
                # Add the "ReceiveBehav" as the default behaviour
                print "setup iniciado"
        		
                self.agenteBoton = None
                self.agenteMovimeinto1 = None
                self.agenteMovimiento2 = None
                self.agenteSwitch = None
                self.agenteTemperatura = None
                self.agentePuerta = None

                self.estadoBoton = False
                self.estadoMovimiento = False
                self.estadoMovimiento2 = False
                self.estadoSwitch = False
                self.agenteTemperatura = False
                self.agentePuerta = False


                rb = self.ReceiveBehav()
                self.setDefaultBehaviour(rb)
		
'''
		tem = spade.Behaviour.ACLTemplate()
        	tem.setPerformative("inform")
        	mt = spade.Behaviour.MessageTemplate(tem)
        	self.addBehaviour(self.recibeMensaje(),mt)


                
                # Prepare template for "AnotherBehav"
                cooking_template = spade.Behaviour.ACLTemplate()

                cooking_template.setOntology("cooking")
                mt = spade.Behaviour.MessageTemplate(cooking_template)

                # Add the behaviour WITH the template
                self.addBehaviour(AnotherBehav, mt)                               
'''                
 

if __name__ == "__main__":
        a = MyAgent("anotificador@lujan.mx", "anotificador")
        a.start()
                
