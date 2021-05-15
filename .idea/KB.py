import Dictionary
import Contraction
import Resolution
import Dictionary
import numpy
class KB:


    def get_sentence(self):
        b = input('Input new Belief : ')
        b= b.upper()
        # transform input to CNS
        kb=KB()
        #print('input is', b)
        newbelief=kb.to_CNS(b)
        print('get_sentence: newbelief in CNS-Format is: ',newbelief)
        # if input includes AND -> more than one new belief
        if '&' in newbelief:
            splitted_newbeliefs = kb.seperate_ANDs(newbelief)
            for i in range(len(splitted_newbeliefs)):
                newbelief1 = splitted_newbeliefs[i]
                kb.ask(newbelief1)
                #kb.ask(newbelief)
        else:
            kb.ask(newbelief)


    def ask(self, new_belief):
        kb= KB()
        new_belief
        k = Dictionary.Dictionary.KB #knowledgebase attribute
        i=0
        if new_belief in k:
                print('Ask_func: Belief: ',new_belief, 'is already in KB, do nothing')
        elif Resolution.Resolution.resolveKB(self, k, new_belief)==False:
            # do resolution:
            # if true -> issue with new belief -> call contraction
            k= Contraction.Contraction.contract(self, new_belief)

            # if no problem append new_belief to KB
            Dictionary.Dictionary.KB = list(dict.fromkeys(Dictionary.Dictionary.KB))
            print('Ask_function: belief added to KB: ',new_belief, 'New updated KB', Dictionary.Dictionary.KB)
        else :#Resolution.Resolution.resolveKB(self, k, new_belief)==False:
            #Some isues we have to check what is actually
            Dictionary.Dictionary.KB.append(new_belief)
            if new_belief[0].isalpha():
                Dictionary.Dictionary.newBelief(self, new_belief[0], True)
            elif new_belief[0].isalpha() == False:
                Dictionary.Dictionary.newBelief(self, new_belief[-1], False)
            Dictionary.Dictionary.KB = list(dict.fromkeys(Dictionary.Dictionary.KB))
            print('Ask_function: updated KB is : ', Dictionary.Dictionary.KB)


    def to_CNS(self, input):
        # translates input to CNF format
        # missing:
            # solve bracket negation
            # distribute ANDs

        input = input.replace(' ','')                                                       # removes all spaces in input
        input = input.replace('~~','')                                                      # removes all double negations

        input = input.replace(' ','')                                                       # removes all spaces in input
        translation = ''
        # seperates input in single () terms to translate, creates 'bracket_translation'
        k=KB()
        if translation == '':
                translation = '%s' %k.replace_operator(input)
                #print('t', translation) # saves first part of CNS translation (with brackets)
        return(translation)



    def replace_operator(self, str):
        # Basic variable translation:
        if 'NOT' in str:
            # translate negation
            # translates to ~R
            str= str.replace('NOT','~')
            #print('String has',b)

        if '^' in str or 'AND' in str:
            # translate conjunction (AND)
            str= str.replace('^','&')
            str = str.replace('AND','&')

        if 'V' in str or 'OR' in str:
            # translate disjunction (OR)
            str= str.replace('V','|')
            str= str.replace('OR','|')
            #print('String has an OR :',str)

        if '<==>' in str or '<-->' in str:
            # eliminate equalance
            # R <==> P
            # translates to (R ==> P) & (P ==> R)
            # translates to (~R | P) & (~P | R)
            if '<==>' in str:
                a=str.partition('<==>')[0]       # everything on the left
                b=str.partition('<==>')[-1]      # everything on the right
            elif '<-->' in str:
                a=str.partition('<-->')[0]       # everything on the left
                b=str.partition('<-->')[-1]      # everything on the right
            #str = '(' + str[0:len(a)-1] + '~' + a[-1] + '|' + b + ')&(' + '~' + b[0] + b[1:len(b)] + '|' + a + ')'
            str = str[0:len(a)-1] + '~' + a[-1] + '|' + b + '&' + '~' + b[0] + b[1:len(b)] + '|' + a
            # this is wrong, but it workes bc of seperate_ANDs

        if '==>' in str or '-->' in str:
            # translate implication
            # R ==> P
            # translates to ~R | P
            if '==>' in str:
                a=str.partition('==>')[0]       # everything on the left
                b=str.partition('==>')[-1]
            elif '-->' in str:
                a=str.partition('-->')[0]       # everything on the left
                b=str.partition('-->')[-1]# everything on the right
            str = str[0:len(a)-1] + '~' + a[-1] + '|' + b
        str = str.replace('~~','')
        return(str)

    def seperate_ANDs(self, str):
        # seperates string at AND to produce more than one new belief
        # works only without brakets at the moment
        statements = []
        while '&' in str:
            statements.append(str.partition('&')[0])        # everything on the left of & -> first statement
            str = str.partition('&')[-1]                    # everything on the right -> look for additional '&'
        statements.append(str)                              # rest of the original statement -> last statement
        return (statements)
    def makeMethod(self, k):
        print('I dont do anything',k)

while True:
    B=KB()
    B.get_sentence()

