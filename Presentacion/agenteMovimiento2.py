# -*- coding: utf-8 -*-
import spade
import time
import datetime

#       AGENTE MOVIMIENTO 2

class MyAgent(spade.Agent.Agent):
	
    def enviarMensaje(self):
	if (self.banSubscriptor):
	
		print "enviando mensaje"
		if (self.presence):
			receiver = self.sender
			self.msgS = spade.ACLMessage.ACLMessage()
			self.msgS.setPerformative("inform")
			self.msgS.setOntology("demo3")
			self.msgS.addReceiver(receiver)
			self.msgS.setContent("Movimiento2ON")
			self.send(self.msgS)
			print "envie mensaje ON a notificador"
		else:
			receiver = self.sender
			self.msgS = spade.ACLMessage.ACLMessage()
			self.msgS.setPerformative("inform")
			self.msgS.setOntology("demo3")
			self.msgS.addReceiver(receiver)
			self.msgS.setContent("Movimiento2OFF")
			self.send(self.msgS)
			print "envie mensaje OFF a notificador"
	else:
		print "no hay suscriptor"
    
    class Suscribir(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            print "Requesting subscription to NinjaBlock Hardware Agent..."
            receiver = spade.AID.aid(name="agentehw@lujan.mx/spade/", 
                addresses=["xmpp://agentehw@lujan.mx/spade/"])
            self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            self.msg.setPerformative("subscribe")        # Set the "inform" FIPA performative
            self.msg.setOntology("AMITec")        # Set the ontology of the message content
            self.msg.setLanguage("English")           # Set the language of the message content
            self.msg.addReceiver(receiver)            # Add the message receiver
            self.msg.setContent("movimiento2")       # Set the message content

            self.myAgent.send(self.msg)

    class Accepted(spade.Behaviour.EventBehaviour):
        """
        This EventBehaviour gets launched when a message that matches its template arrives at the agent
        """
        def _process(self):            
            print "Aceptación de la suscripción"
            self.msg = None
            self.msg = self._receive(False)
            # Check wether the message arrived
            if self.msg:
                print "La respuesta recibida: '%s'!" % self.msg.content
            else:
                print "No se recibió mensaje"

   

    class RcvMotion(spade.Behaviour.EventBehaviour):

        def _process(self):                        
            self.motionMsg = None
            self.motionMsg = self._receive(False)
            # Check wether the message arrived
            if self.motionMsg:
		print "Mensaje recibido: '%s'!" % self.motionMsg.getContent()
                self.myAgent.LastMov = datetime.datetime(*(time.strptime(self.motionMsg.getContent(), "%d/%m/%Y-%H:%M:%S"))[:6])
                
                if(self.myAgent.presence == False):
                    self.myAgent.presence = True
		    self.myAgent.enviarMensaje()
            else:
                print "No se recibió mensaje"
                
    class ActualizaOH(spade.Behaviour.PeriodicBehaviour):
        def _onTick(self):
            if(self.myAgent.presence):
		receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                self.msgS = spade.ACLMessage.ACLMessage()
                self.msgS.setPerformative("help")
                self.msgS.addReceiver(receiver)
                self.msgS.setContent("update movimiento2 ON")
                self.myAgent.send(self.msgS)
                print "estado nuevo ENCENDIDO enviado a openHab"
		
		
              
            else:
                #print "."
		receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                self.msgS = spade.ACLMessage.ACLMessage()
                self.msgS.setPerformative("help")
                self.msgS.addReceiver(receiver)
                self.msgS.setContent("update movimiento2 OFF")
                self.myAgent.send(self.msgS)
                print "estado nuevo APAGADO enviado"
		
    class recibeSubscribe(spade.Behaviour.EventBehaviour):
	def _process(self):
		self.msgR = self._receive(False)
		if self.msgR:
			print "suscripcion de movimiento recibido"
			self.myAgent.banSubscriptor = True
			self.myAgent.sender = self.msgR.getSender()
			
		else:	
			print "No hay mensajes"

    class MainBhv(spade.Behaviour.Behaviour):
        def _process(self):
            
            if(self.myAgent.presence):
                now = datetime.datetime.now()
                #print "%s" %(now - self.myAgent.LastMov)
                if((now - self.myAgent.LastMov).total_seconds() > 5):
                    self.myAgent.presence = False
		    self.myAgent.enviarMensaje()

                                
    def _setup(self):
        print "Inicializando. . . ."
        time.sleep(2)
        self.LastMov = datetime.datetime.now()
        self.presence = False
	
	self.banSubscriptor = False
	self.sender = None	

        b = self.MainBhv()
        self.setDefaultBehaviour(b)
        
        b = self.Suscribir()
        self.addBehaviour(b, None)
        
        b= self.ActualizaOH(5)
        self.addBehaviour(b, None)

        #Se aceptó la suscripción
        template = spade.Behaviour.ACLTemplate()
        template.setPerformative("accept")
        t = spade.Behaviour.MessageTemplate(template)        
        self.addBehaviour(self.Accepted(),t)

        #Se reciben los mensajes de movimiento
        template = spade.Behaviour.ACLTemplate()
        template.setPerformative("inform")
        template.setOntology("AMITec")
        t = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.RcvMotion(),t)

	tem = spade.Behaviour.ACLTemplate()
	tem.setPerformative("subscribe")
	mt = spade.Behaviour.MessageTemplate(tem)
	self.addBehaviour(self.recibeSubscribe(),mt)		
	
        

if __name__ == "__main__":
#    a = MyAgent("jolishagent1@ubuntu-jabber.net", "agent1")
#    a = MyAgent("jolishagent1@jabberes.org", "agent1")
    a = MyAgent("amovimiento2@lujan.mx", "amovimiento2")
    a.start()

    #time.sleep(20)
    #print "Execution time limit reached"
    #a.stop()
