# -*- coding: utf-8 -*-
import spade
import time
import datetime

class MyAgent(spade.Agent.Agent):
    
    class SuscribirON(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            print "Requesting subscription to NinjaBlock Hardware Agent..."
            # First, form the receiver AID
#            receiver = spade.AID.aid(name="jolishagent2@ubuntu-jabber.net/spade/", 
#                addresses=["xmpp://jolishagent2@ubuntu-jabber.net/spade/"])
#            receiver = spade.AID.aid(name="danielagente1@ubuntu-jabber.net/spade/", 
#                addresses=["xmpp://danielagente1@ubuntu-jabber.net/spade/"])
#            receiver = spade.AID.aid(name="danielAgente1@jabberes.org/spade/", 
#                addresses=["xmpp://danielAgente1@jabberes.org/spade/"])
            receiver = spade.AID.aid(name="agentehw@lujan.mx/spade/", 
                addresses=["xmpp://agentehw@lujan.mx/spade/"])

                 
                # Second, build the message
            self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            self.msg.setPerformative("subscribe")        # Set the "inform" FIPA performative
            self.msg.setOntology("AMITec")        # Set the ontology of the message content
            self.msg.setLanguage("English")           # Set the language of the message content
            self.msg.addReceiver(receiver)            # Add the message receiver
            self.msg.setContent("SwitchOn")       # Set the message content

            # Third, send the message with the "send" method of the agent
            self.myAgent.send(self.msg)

    class SuscribirOFF(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            print "Requesting subscription to NinjaBlock Hardware Agent..."
            # First, form the receiver AID
#            receiver = spade.AID.aid(name="jolishagent2@ubuntu-jabber.net/spade/", 
#                addresses=["xmpp://jolishagent2@ubuntu-jabber.net/spade/"])
#            receiver = spade.AID.aid(name="danielagente1@ubuntu-jabber.net/spade/", 
#                addresses=["xmpp://danielagente1@ubuntu-jabber.net/spade/"])
#            receiver = spade.AID.aid(name="danielAgente1@jabberes.org/spade/", 
#                addresses=["xmpp://danielAgente1@jabberes.org/spade/"])
            receiver = spade.AID.aid(name="agentehw@lujan.mx/spade/", 
                addresses=["xmpp://agentehw@lujan.mx/spade/"])

                 
                # Second, build the message
            self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            self.msg.setPerformative("subscribe")        # Set the "inform" FIPA performative
            self.msg.setOntology("AMITec")        # Set the ontology of the message content
            self.msg.setLanguage("English")           # Set the language of the message content
            self.msg.addReceiver(receiver)            # Add the message receiver
            self.msg.setContent("SwitchOff")       # Set the message content

            # Third, send the message with the "send" method of the agent
            self.myAgent.send(self.msg)
    def enciendeVentilador(self):
            print "Solicitando encender al agente de Hardware NinjaBlock"
            # First, form the receiver AID
#            receiver = spade.AID.aid(name="jolishagent2@ubuntu-jabber.net/spade/", 
#                addresses=["xmpp://jolishagent2@ubuntu-jabber.net/spade/"])
#            receiver = spade.AID.aid(name="danielagente1@ubuntu-jabber.net/spade/", 
#                addresses=["xmpp://danielagente1@ubuntu-jabber.net/spade/"])
#            receiver = spade.AID.aid(name="danielAgente1@jabberes.org/spade/", 
#                addresses=["xmpp://danielAgente1@jabberes.org/spade/"])
            receiver = spade.AID.aid(name="agentehw@lujan.mx/spade/", 
                addresses=["xmpp://agentehw@lujan.mx/spade/"])

                 
                # Second, build the message
            self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            self.msg.setPerformative("request")        # Set the "inform" FIPA performative
            self.msg.setOntology("switch")        # Set the ontology of the message content
            self.msg.setLanguage("English")           # Set the language of the message content
            self.msg.addReceiver(receiver)            # Add the message receiver
            self.msg.setContent("prende")        # Set the message content
            self.send(self.msg)
            print "Se envió el mensaje"

    def apagaVentilador(self):
            print "Solicitando apagar al agente de Hardware NinjaBlock.."
            # First, form the receiver AID
#            receiver = spade.AID.aid(name="jolishagent2@ubuntu-jabber.net/spade/", 
#                addresses=["xmpp://jolishagent2@ubuntu-jabber.net/spade/"])
#            receiver = spade.AID.aid(name="danielagente1@ubuntu-jabber.net/spade/", 
#                addresses=["xmpp://danielagente1@ubuntu-jabber.net/spade/"])
            receiver = spade.AID.aid(name="danielAgente1@jabberes.org/spade/", 
                addresses=["xmpp://danielAgente1@jabberes.org/spade/"])
                 
                # Second, build the message
            self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            self.msg.setPerformative("request")        # Set the "inform" FIPA performative
            self.msg.setOntology("switch")        # Set the ontology of the message content
            self.msg.setLanguage("English")           # Set the language of the message content
            self.msg.addReceiver(receiver)            # Add the message receiver
            self.msg.setContent("apaga")        # Set the message content            

            # Third, send the message with the "send" method of the agent
            self.send(self.msg)        

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

    class recibeRequest(spade.Behaviour.EventBehaviour):
        def _process(self):            
            self.msgR = None
            self.msgR = self._receive(False)
            if self.msgR:
                print "El mensaje es: '%s'!" % self.msgR.content
                receiver = spade.AID.aid(name="agentehw@lujan.mx/spade/", addresses=["xmpp://agentehw@lujan.mx/spade/"])

                self.msgS = spade.ACLMessage.ACLMessage()
                self.msgS.setPerformative("request")
                self.msgS.setOntology("switch")
                self.msgS.setLanguage("English")
                self.msgS.addReceiver(receiver)
                if(self.msgR.getContent() == "ON"):
                    self.msgS.setContent("prende")
                else:
                    self.msgS.setContent("apaga")
                self.myAgent.send(self.msgS)
            else:
                print "No se recibió mensaje"


    class RcvMotion(spade.Behaviour.EventBehaviour):

        def _process(self):                        
            self.motionMsg = None
            self.motionMsg = self._receive(False)
            # Check wether the message arrived
            if self.motionMsg:
		print "Mensaje recibido: '%s'!" % self.motionMsg.getContent()
                
                if (self.motionMsg.getContent() == "ON"):
			receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                    	self.msgS = spade.ACLMessage.ACLMessage()
                   	self.msgS.setPerformative("help")
                    	self.msgS.addReceiver(receiver)
                    	self.msgS.setContent("update corriente ON")
                    	self.myAgent.send(self.msgS)
                    	print "mensaje enviado switch ON  a openhab"
                	self.myAgent.presence = True
                    #print "Hay alguien"

                    #Iniciar agente usuario
#                    objAgente = agente("danielAgente2@jabberes.org", "agente2")
#                    objAgente.start()
            	elif (self.motionMsg.getContent() == "OFF"):
			receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                    	self.msgS = spade.ACLMessage.ACLMessage()
                    	self.msgS.setPerformative("help")
                    	self.msgS.addReceiver(receiver)
                    	self.msgS.setContent("update corriente OFF")
                    	self.myAgent.send(self.msgS)
                    	print "mensaje enviado switch OFF a openhab"

                	self.myAgent.presence = False

    class MainBhv(spade.Behaviour.Behaviour):
        def _process(self):
            
            if(self.myAgent.presence):
                now = datetime.datetime.now()
                #print "%s" %(now - self.myAgent.LastMov)
                if((now - self.myAgent.LastMov).total_seconds() > 60):
                    self.myAgent.presence = False
#                    print "No hay nadie"
#self.myAgent.apagaVentilador()
                    #Enviar mensaje para apagar ventilador
                                
    def _setup(self):
        print "Inicializando. . . ."
        time.sleep(2)
        self.LastMov = datetime.datetime.now()
        self.presence = False

        b = self.MainBhv()
        self.setDefaultBehaviour(b)
        
        b = self.SuscribirON()
        self.addBehaviour(b, None)
	
	b = self.SuscribirOFF()
	self.addBehaviour(b,None)
        
       
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
        self.addBehaviour(self.RcvMotion(), t)

        #Se recibe el mensaje de votación
        template = spade.Behaviour.ACLTemplate()
        template.setPerformative("request")
        t = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.recibeRequest(), t)
        

if __name__ == "__main__":
#    a = MyAgent("jolishagent1@ubuntu-jabber.net", "agent1")
#    a = MyAgent("jolishagent1@jabberes.org", "agent1")
    a = MyAgent("aswitch@lujan.mx", "aswitch")
    a.start()

    #time.sleep(20)
    #print "Execution time limit reached"
    #a.stop()
