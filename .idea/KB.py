import sympy
class KB:

    KB=['P'];

    def get_sentence(self):
        b = input('Input new Belief : ')
        print('this is your input: ', b)
        #i = []
        #i = b.split(',')
        print('input is', b)
        return b

    def operators_check(self,input):
         if input.find('-->')==True:
             print('-->')
             imply=input.find('-->') # index of operator
             a=input.partition('-->')[0]
             b=input.partition('-->')[-1]
             print('first atomic : ', a, 'Operator is --> with index: ',imply,'last atomic is : ',b )
         if input.find('<->')==True:
             bi_di=input.find('<->') # index of operator
             a=input[0]
             b=input[-1]
             print('first atomic : ', a, 'Operator is: <-> with index',bi_di,'last atomic is : ',b )
         if input.find('&')==True:
             bi_di=input.find('&') # index of operator
             a=input[0]
             b=input[-1]
             print('first atomic : ', a, 'Operator is: & with index',bi_di,'last atomic is : ',b )



    def ask(self):
        kb= KB()
        p= kb.tell() #Run tell method and get input from user
        print('List of statements ',p)
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
        print(knowledgebase.remove(index))
        print(knowledgebase.append(newbelief))



B=KB()
s= B.get_sentence()
B.operators_check(s)