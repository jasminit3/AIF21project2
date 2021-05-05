
class Dictionary:


    logicDict = {
        'A': None,
        'B': None,
        'C': None,
        '~A': None,
        '~B': None,
        '~C': None,
        'A|B' : None,
        'A|C': None,
        'B|C':True,
        '~A|B':None,
    }

    def newBelief(self, NB):
        Dictionary.logicDict[NB] = True

    def getTruelogic(self):
        beliefs= []
        for x in Dictionary.logicDict:
            if Dictionary.logicDict[x]==True:
                beliefs.append(x)
                print('True formulas', x)
        return beliefs

D = Dictionary()
D.newBelief('A')
x= D.getTruelogic()
print('x returned', x)