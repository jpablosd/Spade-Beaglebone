# -*- coding: utf-8 -*-
import spade
import time
import datetime

class MyAgent(spade.Agent.Agent):
    
    class Suscribir(spade.Behaviour.OneShotBehaviour):
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
            self.msg.setContent("temperatura")       # Set the message content

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

    class Vote(spade.Behaviour.EventBehaviour):
        """
        This EventBehaviour gets launched when a message that matches its template arrives at the agent
        """
        def _process(self):            
            print "Solicitud de voto entrante"
            self.msgR = None
            self.msgR = self._receive(False)
            # Check wether the message arrived
            if self.msgR:
                print "El mensaje es: '%s'!" % self.msgR.content
                receiver = self.msgR.getSender()

                self.msgS = spade.ACLMessage.ACLMessage()
                self.msgS.setPerformative("inform")
                self.msgS.setOntology(self.msgR.getOntology())
                self.msgS.setLanguage(self.msgR.getLanguage())
                self.msgS.addReceiver(receiver)
                if(self.myAgent.presence):
                    self.msgS.setContent("si")
                else:
                    self.msgS.setContent("no")
                self.myAgent.send(self.msgS)
                print "Yo voto que %s" % self.msgS.getContent()                   
            else:
                print "No se recibió mensaje"


    class RcvMotion(spade.Behaviour.EventBehaviour):

        def _process(self):                        
            self.motionMsg = None
            self.motionMsg = self._receive(False)
            # Check wether the message arrived
            if self.motionMsg:
		print "Mensaje recibido: %s" % self.motionMsg.getContent()
		self.myAgent.temperatura = self.motionMsg.getContent()
                temp = self.myAgent.temperatura
		temp2 = str(temp)
                print "Hay alguien"
#	        receiver = spade.AID.aid(name="jorge@lujan.mx", addresses=["xmpp://jorge@lujan.mx"])
                receiver = spade.AID.aid(name="openhab@lujan.mx", addresses=["xmpp://openhab@lujan.mx"])
	        print "1"
	        self.msgS = spade.ACLMessage.ACLMessage()
	        #self.msgS.setPerformative("help")
                print "2"
	        self.msgS.addReceiver(receiver)
                print "3"
	        print temp
		if temp >= "20" and temp < "21":
			mensaje = "update Temperature_Setpoint 20"
		elif temp >= "21" and temp < "22":
			mensaje = "update Temperature_Setpoint 21"
		elif temp >= "22" and temp < "23":
			mensaje = "update Temperature_Setpoint 22"
		elif temp >= "23" and temp < "24":
			mensaje = "update Temperature_Setpoint 23"
		elif temp >= "24" and temp < "25":
			mensaje = "update Temperature_Setpoint 24"
		elif temp >= "25" and temp < "26":
			mensaje = "update Temperature_Setpoint 25"
		elif temp >= "26" and temp < "27":
			mensaje = "update Temperature_Setpoint 26"
		elif temp >= "27" and temp < "28":
			mensaje = "update Temperature_Setpoint 27"
		elif temp >= "28" and temp < "29":
			mensaje = "update Temperature_Setpoint 28"
		elif temp >= "29" and temp < "30":
			mensaje = "update Temperature_Setpoint 29"
		elif temp >= "30" and temp < "31":
			mensaje = "update Temperature_Setpoint 30"
		elif temp >= "31" and temp < "32":
			mensaje = "update Temperature_Setpoint 31"
		elif temp >= "32" and temp < "33":
			mensaje = "update Temperature_Setpoint 32"
		elif temp >= "33" and temp < "34":
			mensaje = "update Temperature_Setpoint 33"
		elif temp >= "34" and temp < "35":
			mensaje = "update Temperature_Setpoint 34"
		elif temp >= "35" and temp < "36":
			mensaje = "update Temperature_Setpoint 35"
		elif temp >= "36" and temp < "37":
			mensaje = "update Temperature_Setpoint 36"
		elif temp >= "37" and temp < "38":
			mensaje = "update Temperature_Setpoint 37"
		elif temp >= "38" and temp < "39":
			mensaje = "update Temperature_Setpoint 38"
		elif temp >= "39" and temp < "40":
			mensaje = "update Temperature_Setpoint 39"
		elif temp >= "40" and temp < "41":
			mensaje = "update Temperature_Setpoint 40"
		elif temp >= "41" and temp < "42":
			mensaje = "update Temperature_Setpoint 41"
		elif temp >= "42" and temp < "43":
			mensaje = "update Temperature_Setpoint 42"
		elif temp >= "43" and temp < "44":
			mensaje = "update Temperature_Setpoint 43"
		elif temp >= "44" and temp < "45":
			mensaje = "update Temperature_Setpoint 44"

       	        self.msgS.setContent("%s" % mensaje)
#     	        self.msgS.setContent("update Temperature_Setpoint %s" %  temp)
                print "4"
	        self.myAgent.send(self.msgS)
                print "5"
                    #Iniciar agente usuario
#                    objAgente = agente("danielAgente2@jabberes.org", "agente2")
#                    objAgente.start()
            else:
                print "No se recibió mensaje"
                
    class Twittear(spade.Behaviour.PeriodicBehaviour):
        def _onTick(self):
	    temp = self.myAgent.temperatura
	    print self.myAgent.presence	    
            if(self.myAgent.presence):
		receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                self.msgS = spade.ACLMessage.ACLMessage()
                self.msgS.addReceiver(receiver)
		print "1"
                self.msgS.setContent("update Temperature_Setpoint %d" % temp)
		print "2"
#                self.myAgent.send(self.msgS)
		print "Temp: %d" %temp
                print "estado nuevo ENCENDIDO enviado"
	



		
		'''
                print "tuiteando"
                receiver = spade.AID.aid(name="twitteragent@192.241.206.12/spade/", 
                    addresses=["xmpp://twitteragent@192.241.206.12/spade/"])             

                    # Second, build the message
                self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
                self.msg.setPerformative("request")        # Set the "inform" FIPA performative
                self.msg.setOntology("AMITEC")        # Set the ontology of the message content
                self.msg.setLanguage("English")           # Set the language of the message content
                self.msg.addReceiver(receiver)            # Add the message receiver
                self.msg.setContent("Felicidades por haber tomado su medicamento!")       # Set the message content

                # Third, send the message with the "send" method of the agent
                self.myAgent.send(self.msg)
		'''
		
            else:
                #print "."
		receiver = spade.AID.aid(name="openhab@lujan.mx/Smack", addresses=["xmpp://openhab@lujan.mx/Smack"])
                self.msgS = spade.ACLMessage.ACLMessage()
                self.msgS.setPerformative("help")
                self.msgS.addReceiver(receiver)
                self.msgS.setContent("wefq")
#                self.myAgent.send(self.msgS)
                print "estado nuevo APAGADO enviado"
		




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
        self.LastMov = datetime.datetime.now()
        self.presence = False
	self.temperatura = "0"

        b = self.MainBhv()
        self.setDefaultBehaviour(b)
        
        b = self.Suscribir()
        self.addBehaviour(b, None)
        
        b= self.Twittear(60)
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
        self.addBehaviour(self.RcvMotion(), t)

        #Se recibe el mensaje de votación
        template = spade.Behaviour.ACLTemplate()
        template.setPerformative("request")
        template.setOntology("vote")
        t = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.Vote(), t)
        

if __name__ == "__main__":
#    a = MyAgent("jolishagent1@ubuntu-jabber.net", "agent1")
#    a = MyAgent("jolishagent1@jabberes.org", "agent1")
    a = MyAgent("atemperatura@lujan.mx", "atemperatura")
    a.start()

    #time.sleep(20)
    #print "Execution time limit reached"
    #a.stop()
