class State(object):
    def __init__(self):
        pass

    def enter(self):
        #Initializes data that might not be initialized
        pass

    def exit(self):
        #Performs cleanups if State is finished
        pass

    def reason(self):
        #Checks if a state needs to end or start
        pass

    def act(self):
        #Controls frame behavior
        pass

class StateMachine(object):

    def __init__(self, host, first_state=None):
        self.host = host
        self.current_state = first_state

    def transition(self, new_state):
        #Changes to new state
        self.current_state.exit()
        self.current_state = new_state

        # provide state references to host object and fsm instance
        self.current_state.host = self.host
        self.current_state.fsm = self

        self.current_state.enter()

    def update(self):
		#Updates only when there is an existing state
        if self.current_state:
            new_state = self.current_state.reason()
            #Provides function for new states along with transition
            if new_state: 
                self.transition(new_state)
            else:
                #Has the game continue with existing state if a new one 
                #isn't created
                self.current_state.act()
