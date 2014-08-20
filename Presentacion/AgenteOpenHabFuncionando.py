import spade

class MyAgent(spade.Agent.Agent):
	class ReceivePresence(spade.Behaviour.EventBehaviour):
		def _process(self):
			print "msg presencia"
			self.msg = self._receive(False)
			print self.msg
			if self.msg:
				print "hay mensaje de presencia"

        class ReceiveBehav(spade.Behaviour.Behaviour):
                """This behaviour will receive all kind of messages"""

                def _process(self):
                        print "process"
                        self.msg = self._receive(True,10)
                        print "mensaje recibido"
                        print self.msg
                        #print self.msg   
                        # Blocking receive for 10 seconds
                        # Check wether the message arrived
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


        def _setup(self):
                # Add the "ReceiveBehav" as the default behaviour
                print "setup iniciado"
	#                rb = self.ReceiveBehav()
#                self.setDefaultBehaviour(rb)

		template = spade.Behaviour.BehaviourTemplate("from=\"jorge@lujan.mx\"")

		mt = spade.Behaviour.MessageTemplate(template)
		self.addBehaviour(self.ReceivePresence(),mt)


if __name__ == "__main__":
        a = MyAgent("juanpablo@lujan.mx", "juanpablo")
        a.start()
                
