
class KB:

    KB=['r'];
 # hi
    def KBAgent(kb):
        kb

    def tell(self):
        b = input('Input new Belief : ')
        print('this is your input: ', b)
        i = []
        i = b.split(',')
        print('input array is', i)
        return i

    def ask(self):
        kb= KB()
        p= kb.tell() #Run tell method and get input from user
        k = KB.KB #knowledgebase attribute
        i=0
        for i in p:
            if i in k:
                k.index(i)
                print('Belief: ',i, 'is already in KB, do nothing')
            else:
                k.append(i)
                print('belief added to KB: ',i, 'New updated KB', k)


    def contraction(self,newbelief,index, knowledgebase):
        knowledgebase.remove(index)
        knowledgebase.append(newbelief)



B=KB()
B.ask()