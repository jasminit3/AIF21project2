
class Dictionary:

    # KB=['r'];
    # KB is a list
    # can be extended by extend('clause')
    # can be retracted by remove('clause')
    KB = ['~A', '~B', '~C']

    logicDict = {
        'A': False,
        'B': False,
        'C': False
    }

    def update_KB(self, new_believ,leaving_belief ):
        Dictionary.KB.remove(leaving_belief)
        Dictionary.KB.append(new_believ)

    def newBelief(self, NB, bool):
        if bool== False:
            Dictionary.logicDict[NB] = False
        else:
            Dictionary.logicDict[NB] = True
        #print('Updated Literal dict: ',Dictionary.logicDict)

    def getTruelogic(self, nb):
        #beliefs= []
        #print('dict: received nb in gettruelogic', nb)
        x = Dictionary.logicDict[nb]
        #for nb in Dictionary.logicDict:
            #if Dictionary.logicDict[x]==True:
                #beliefs.append(x)
        #print('dict: True formulas', x)
        return x