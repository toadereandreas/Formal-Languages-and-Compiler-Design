class FiniteAutomata:

    def __init__(self, states, alphabet, q0, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.q0 = q0
        self.final_states = final_states
        self.transitions = transitions

    def getLine(line):
        return line.strip().split(' ')[2:]

    def readFromFile(fileName):
        with open(fileName) as file:
            states = FiniteAutomata.getLine(file.readline())
            alphabet = FiniteAutomata.getLine(file.readline())
            q0 = FiniteAutomata.getLine(file.readline())[0]
            final_states = FiniteAutomata.getLine(file.readline())
            file.readline()
            transitions = {}
            for line in file:
                source = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                weight = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1].strip()
                destination = line.strip().split('->')[1].strip()

                if (source, weight) in transitions.keys():
                    transitions[(source, weight)].append(destination)
                else:
                    transitions[(source, weight)] = [destination]

            return FiniteAutomata(states, alphabet, q0, final_states, transitions)

    def isDeterministic(self):
        for k in self.transitions.keys():
            if len(self.transitions[k]) > 1:
                return False
        return True

    def isSequenceAccepted(self, sequence):
        position = 0
        while(position < len(sequence[1])):
            next = sequence[1][position]
            # print("sequence[0]: " + str(sequence[0]))
            for k in self.transitions.keys():
                print("seqeuence[0]: " + str(sequence[0]) + ", next: " + str(next) + " in k: " + str(k))
                if( sequence[0] in k and next in k):
                    # print(self.transitions[k])
                    sequence[0] = self.transitions[k][0]
                    print("")
                    break
            print(next)
            print("current state: " + str(sequence[0]))
            position = position + 1
        print("final :" + str(sequence[0]))
        if(sequence[0] in self.final_states):
            return True
        return False

    def __str__(self):
        return "states = { " + ', '.join(self.states) + " }\n" + "alphabet = { " + ', '.join(self.alphabet) + " }\n" +\
               "q0 = { " + self.q0 + " }\n" + "final_states = { " + ', '.join(self.final_states) + " }\n" +"transitions = " + str(self.transitions) + " "
