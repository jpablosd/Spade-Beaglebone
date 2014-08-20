import spade

class MyAgent(spade.Agent.Agent):
        class ReceiveBehav(spade.Behaviour.Behaviour):
                """This behaviour will receive all kind of messages"""

                def _process(self):
                        print "process"
                        self.msg = self._receive(True,10)
                        print self.msg
                        #print self.msg   
                        # Blocking receive for 10 seconds
                        # Check wether the message arrived
                        if self.msg:
                                print "I got a message!"
                                try:
                                        if self.msg.getOntology() != "Presence":
                                                print "No presencia msg"
                                                print self.msg
                                except:
                                        print "except"
                                        print self.msg
                                        linea = str(self.msg)
                                        if len(linea)>3:
                                            print linea
                                            #expreReg = re.compile('<|>|=|"|:|/| ')
                                            #linea = expreReg.sub("",linea)
                                            linea = linea.split('<body>')
                                            print linea
                                            mesaje = linea[1].split('</body>')
                                            print mesaje
                                            print "mensaje: "
                                            print mesaje[0]

                                            '''
                                            if mesaje[0] == "luz prendida":
                                                print "entro al if"

                                                
                                                receiver = spade.AID.aid(name="openhab@lujan.mx", addresses=["xmpp://openhab@lujan.mx"])
                                                print "receiver"
                                                self.msg = spade.ACLMessage.ACLMessage()
                                                print "aclmensaje"
                                                self.msg.setPerformative("inform")
                                                print "inform"
                                                #self.msg.setOntology("hola")
                                                #print "ontology"
                                                selg.msg.setLanguage("English")
                                                print "languaje"
                                                self.msg.addReceiver(receiver)
                                                print "add receiver"
                                                self.msg.setContent("help")
                                                print "contenido"
                                                self.MyAgent.send(self.msg)
                                                print "enviando mensaje"
                                            '''  
                        else:
                                print "I waited but got no message"
                        self.msg = None

        '''
        class SendMsgBehav(spade.Behaviour.OneShotBehaviour):
                """
                This behaviour sends a message to this same agent to trigger an EventBehaviour
                """
                def _process(self):
                    msg = spade.ACLMessage.ACLMessage()
                    msg.setPerformative("inform")
                    msg.addReceiver(spade.AID.aid("qwerty@suchat.org",["xmpp://qwerty@suchat.org"]))
                    msg.setContent("testSendMsg")
                    print "Sending message in 3 . . ."
                    time.sleep(1)
                    print "Sending message in 2 . . ."
                    time.sleep(1)
                    print "Sending message in 1 . . ."
                    time.sleep(1)

                    self.myAgent.send(msg)
                    
                    print "I sent a message"
                    #print str(msg)
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

        def _setup(self):
                # Add the "ReceiveBehav" as the default behaviour
                print "setup iniciado"
                rb = self.ReceiveBehav()
                self.setDefaultBehaviour(rb)

                '''
                # Prepare template for "AnotherBehav"
                cooking_template = spade.Behaviour.ACLTemplate()

                cooking_template.setOntology("cooking")
                mt = spade.Behaviour.MessageTemplate(cooking_template)

                # Add the behaviour WITH the template
                self.addBehaviour(AnotherBehav, mt)                               
                '''

if __name__ == "__main__":
        a = MyAgent("juanpablo@lujan.mx", "juanpablo")
        a.start()
                