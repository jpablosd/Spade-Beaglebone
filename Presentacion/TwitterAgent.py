# -*- coding: utf-8 -*-
import spade
import twitter

#Clase principal que hereda de Agent
class agente(spade.Agent.Agent):

    class ReqTwit(spade.Behaviour.EventBehaviour):

        def _process(self):                        
            self.myAgent.twitMsg = None
            self.myAgent.twitMsg = self._receive(False)
            # Check wether the message arrived
            if self.myAgent.twitMsg:
                print "Mensaje recibido: '%s'!" % self.myAgent.twitMsg.getContent()
                    
            else:
                print "No se recibió mensaje"

    class MainBhv(spade.Behaviour.Behaviour):
        def _process(self):
            if(self.myAgent.twitMsg != ""):
                print "Twitteando... '%s'" % self.myAgent.twitMsg.getContent()            
                self.my_auth = twitter.OAuth("22218718-H7S5pCM5ql3o5IbY3y3tKGRHPnZaNVKVkDyISHRC5","gFHKEOZ4SLvUZ9W5ZKoRbJ3T8QzRoNOKcXZh1KqdBLxog","xlROelufNxsqaBJhe2yd0w","z6e61FOffLaE2V3HV2OCbG745J9vBVfILe5LDaQBEQ")
                print "1... '%s'" % self.myAgent.twitMsg.getContent()
                self.twit = twitter.Twitter(auth=self.my_auth)
                print "2... '%s'" % self.myAgent.twitMsg.getContent()
                self.msg = "'%s'" % self.myAgent.twitMsg.getContent()
                print "3... '%s'" % self.myAgent.twitMsg.getContent()
                self.twit.statuses.update(status=self.msg)
                print "Listo... '%s'" % self.myAgent.twitMsg.getContent()
                self.myAgent.twitMsg = None

    #Metodo del comportamiento de la clase principal myAgent
    def _setup(self):
        print "Inicializando. . . ."
        
        self.twitMsg = ""
        print self.twitMsg
        
        b = self.MainBhv()
        self.setDefaultBehaviour(b)        

        #Se reciben los mensajes de movimiento
        template = spade.Behaviour.ACLTemplate()
        template.setPerformative("request")
        template.setOntology("AMITEC")
        t = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.ReqTwit(), t)        

if __name__ == "__main__":
    agent = agente("twitteragent@192.241.206.12","twitteragent")
    agent.start()


