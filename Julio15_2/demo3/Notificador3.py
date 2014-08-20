import spade

class MyAgent(spade.Agent.Agent):
        class ReceiveBehav(spade.Behaviour.Behaviour):
                """This behaviour will receive all kind of messages"""
                def _process(self):
			print "MEnsaje"
			self.msg = self._receive(True,10)
			if self.msg:
				print "MENSAJE"
				if self.msg.getOntology() != "Presence":
					self.MyAgent.banMsg = True
					print self.msg.getContent()
   					self.MyAgent.mensaje = self.msg.getContent()
#				print self.MyAgent.mensaje

	class recibeRespuesta(spade.Behaviour.EventBehaviour):
		def _process(self):
			self.msgR = self.receive(False)
			if self.msgR.getOntology() == "mov1":
				self.MyAgent.banMov1 = True
			else:
				self.MyAgent.banMov2 = True

	class mainBHV(spade.Behaviour.Behaviour):
		def _process(self):
			print "MAIN"
			if self.MyAgent.banMsg:
				if self.MyAgent.banMov1:
					if self.MyAgent.banMov2:
						receiver = spade.AID.aid(name="openhab@lujan.mx", addresses=["xmpp://openhab@lujan.mx"])
					else:
						receiver = spade.AID.aid(name="juanpablo@lujan.mx", addresses=["xmpp://juanpablo@lujan.mx"])
				else:
					receiver = spade.AID.aid(name="andres@lujan.mx", addresses=["xmpp://andres@lujan.mx"])
				self.msg = spade.ACLMessage.ACLMessage()
				self.msg.setPerformative("Notificador")
				self.msg.addReceiver(receiver)
				self.msg.setContent(self.MyAgent.mensaje)
				self.MyAgent.send(self.msg)
			
        def _setup(self):
                # Add the "ReceiveBehav" as the default behaviour
                print "setup iniciado"

		self.banMsg = False
		self.banMov1 = False
		self.banMov2 = False
		self.mensaje = None

                rb = self.ReceiveBehav()
                self.setDefaultBehaviour(rb)

		b = self.mainBHV()
		self.addBehaviour(b, None)

		template = spade.Behaviour.ACLTemplate()
		template.setPerformative("response")
		mt = spade.Behaviour.MessageTemplate(template)
		self.addBehaviour(self.recibeRespuesta(), mt)

		



if __name__ == "__main__":
        a = MyAgent("anotificador@lujan.mx", "anotificador")
        a.start()
                

