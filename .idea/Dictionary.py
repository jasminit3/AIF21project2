
class Dictionary:


    # logicDict = {
    #     'A': None,
    #     'B': None,
    #     'C': None,
    #     '~A': None,
    #     '~B': None,
    #     '~C': None,
    #     'A|B' : None,
    #     'A|C': None,
    #     'B|C':True,
    #     '~A|B':None,
    # }
    logicDict = {
        'A': None,
        'B': None,
        'C': None
    }

    def newBelief(self, NB, bool):
        if bool== False:
            Dictionary.logicDict[NB] = False
        else:
            Dictionary.logicDict[NB] = True
        print('updated dict: ',Dictionary.logicDict)

    def getTruelogic(self, nb):
        #beliefs= []
        x = Dictionary.logicDict[nb]
        #for nb in Dictionary.logicDict:
            #if Dictionary.logicDict[x]==True:
                #beliefs.append(x)
        print('True formulas', x)
        return x

#D = Dictionary()
#D.newBelief('A')
#x= D.getTruelogic()
#print('x returned', x)