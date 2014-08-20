# -*- coding: utf-8 -*-
import spade
import time

class agente(spade.Agent.Agent):
    class Votacion(spade.Behaviour.PeriodicBehaviour):
        def _onTick(self):
            receiver = spade.AID.aid(name="danielagente1@jabberes.org/spade/",
             addresses=["xmpp://danielagente1@jabberes.org/spade/"])

            receiver2 = spade.AID.aid(name="jolishagent1@jabberes.org/spade/",
             addresses=["xmpp://jolishagent1@jabberes.org/spade/"])
            
            self.msg = spade.ACLMessage.ACLMessage() 
            self.msg.setPerformative("request")
            self.msg.setOntology("vote")
            self.msg.setLanguage("English")         
            self.msg.addReceiver(receiver)
            self.msg.addReceiver(receiver2)           
            self.msg.setContent("Solicitud de voto")
            print "Solicitando votos"
            self.myAgent.send(self.msg)
            
            self.msgR = self._receive(True, 10)

            if self.msgR:
                print "Voto1 recibido, dice: %s" % self.msgR.getContent()
                vote1 = self.msgR.getContent()
            else:
                print "No hay mensajes"

            self.msgR = self._receive(True, 10)

            if self.msgR:
                print "Voto2 recibido, dice: %s" % self.msgR.getContent()
                vote2 = self.msgR.getContent()
            else:
                print "No hay mensajes"

            if (vote1 == "si" and vote2 == "si"):
                print "prende"
                self.myAgent.enciendeVentilador()            
            elif (vote1 == "si" or vote2 == "si"):
                vote3 = raw_input("Usted tiene calor? si/no\n")
                print "Su respuesta fue: %s" % vote3
                if (vote1 == "si" and vote3 == "si") or (vote2 == "si" and vote3 == "si"):
                    print "prende"
                    self.myAgent.enciendeVentilador()
                else:
                    self.myAgent.apagaVentilador()
            else:
                self.myAgent.apagaVentilador()

    def enciendeVentilador(self):
            print "Requesting switch ON to NinjaBlock Hardware Agent..."
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
            self.msg.setContent("prende")        # Set the message content
            self.send(self.msg)
            print "Se envió el mensaje"


    def apagaVentilador(self):
            print "Requesting switch OFF to NinjaBlock Hardware Agent..."
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
            
        

    def _setup(self):
        print "Inicializando..."
        tem = spade.Behaviour.ACLTemplate()
        tem.setPerformative("inform")
        tem.setOntology("vote")
        mt = spade.Behaviour.MessageTemplate(tem)
        
        self.addBehaviour(self.Votacion(60),mt)
        print "iniciado"

if __name__ == "__main__":
    objAgente = agente("danielAgente2@jabberes.org", "agente2")
    objAgente.start()
    
