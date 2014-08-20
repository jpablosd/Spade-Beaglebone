# -*- coding: utf-8 -*-
import spade
import time
import datetime

class MyAgent(spade.Agent.Agent):
    
    class Suscribir(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            print "Requesting subscription to NinjaBlock Hardware Agent..."
            receiver = spade.AID.aid(name="agentehw@lujan.mx/spade/", addresses=["xmpp://agentehw@lujan.mx/spade/"])
                # Second, build the message
            self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            self.msg.setPerformative("subscribe")        # Set the "inform" FIPA performative
            self.msg.setOntology("AMITec")        # Set the ontology of the message content
            self.msg.setLanguage("English")           # Set the language of the message content
            self.msg.addReceiver(receiver)            # Add the message receiver
            self.msg.setContent("PuertaAbierta")       # Set the message content

            # Third, send the message with the "send" method of the agent
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
                print "No se recibió mensa"

    class RcvMotion(spade.Behaviour.EventBehaviour):

        def _process(self):                        
            self.motionMsg = None
            self.motionMsg = self._receive(False)
            # Check wether the message arrived
            if self.motionMsg:
		print "Mensaje recibido: %s" % self.motionMsg.getContent()
		#mensaje = self.msgR.getContet()
		#print "mensaje"
		if(self.motionMsg.getContent() == "PuertaAbierta"):
		   	receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
			self.msgS = spade.ACLMessage.ACLMessage()
			self.msgS.setPerformative("help")
			self.msgS.addReceiver(receiver)
			self.msgS.setContent("update puerta ON")
			self.myAgent.send(self.msgS)
			print "mensaje enviado (puerta abierta) a openhab"
			self.myAgent.presence = True
	
		else:
			print "entro al else"
			#self.myAgent.presence = False
                
            else:
                print "No se recibió mensaje"
                



    class MainBhv(spade.Behaviour.Behaviour):
        def _process(self):
            
            if(self.myAgent.presence):
                now = datetime.datetime.now()
                #print "%s" %(now - self.myAgent.LastMov)
                if((now - self.myAgent.LastMov).total_seconds() > 30):
                    receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                    self.msgS = spade.ACLMessage.ACLMessage()
                    self.msgS.setPerformative("help")
                    self.msgS.addReceiver(receiver)
                    self.msgS.setContent("update puerta OFF")
                    self.myAgent.send(self.msgS)
                    print "mensaje enviado (puerta cerrada) a openhab"
		    self.myAgent.presence = False
		 

    def _setup(self):
        print "Inicializando. . . ."
        time.sleep(2)
        self.LastMov = datetime.datetime.now()
        self.presence = False

        b = self.MainBhv()
        self.setDefaultBehaviour(b)
        
        b = self.Suscribir()
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

if __name__ == "__main__":
#    a = MyAgent("jolishagent1@ubuntu-jabber.net", "agent1")
#    a = MyAgent("jolishagent1@jabberes.org", "agent1")
    a = MyAgent("apuerta@lujan.mx", "apuerta")
    a.start()

    #time.sleep(20)
    #print "Execution time limit reached"
    #a.stop()
