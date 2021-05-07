
class Dictionary:

    # KB=['r'];
    # KB is a list
    # can be extended by extend('clause')
    # can be retracted by remove('clause')
    KB = ['~A', '~B', '~C', '~A|~B']

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
        'A': False,
        'B': False,
        'C': False
    }

    def newBelief(self, NB, bool):
        if bool== False:
            Dictionary.logicDict[NB] = False
        else:
            Dictionary.logicDict[NB] = True
        print('dict: updated dict: ',Dictionary.logicDict)

    def getTruelogic(self, nb):
        #beliefs= []
        print('dict: received nb in gettruelogic', nb)
        x = Dictionary.logicDict[nb]
        #for nb in Dictionary.logicDict:
            #if Dictionary.logicDict[x]==True:
                #beliefs.append(x)
        print('dict: True formulas', x)
        return x

#D = Dictionary()
#D.newBelief('A')
#x= D.getTruelogic()
#print('x returned', x)