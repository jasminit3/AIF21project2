
class KB:

    # KB=['r'];
    # KB is a list
    # can be extended by extend('clause')
    # can be retracted by remove('clause')
    KB = []


    def get_sentence(self):
        b = input('Input new Belief : ')
        b= b.upper()
        # transform input to CNS
        kb=KB()
        #print('input is', b)
        newbelief=kb.to_CNS(b)
        print('newbelief in CNS-Format is: ',newbelief)
        # if input includes AND -> more than one new belief
        if '&' in newbelief:
            splitted_newbeliefs = kb.seperate_ANDs(newbelief)
            for i in range(len(splitted_newbeliefs)):
                newbelief = splitted_newbeliefs[i]
                kb.ask(newbelief)
        else:
            kb.ask(newbelief)


    def ask(self, new_belief):
        kb= KB()
        new_belief
        k = kb.KB #knowledgebase attribute
        i=0
        if new_belief in k:
                print('Belief: ',new_belief, 'is already in KB, do nothing')
        else:
            kb.contraction(new_belief,k)
         # should check for change-method before append
             #k.append(new_belief)
            print('belief added to KB: ',new_belief, 'New updated KB', k)


    def contraction(self, newbelief, knowledgebase):
        print('knowledgebase before contraction ',knowledgebase, 'newbelief before contraction', newbelief)
        negated = '~'+ newbelief
        not_negated = newbelief[1:]
        #print('not negated input',not_negated)
        if newbelief and negated in knowledgebase:
            knowledgebase.remove(negated)
            knowledgebase.append(newbelief)
        elif newbelief and not_negated in knowledgebase :
             knowledgebase.remove(not_negated)
             knowledgebase.append(newbelief)
        else:
            knowledgebase.append(newbelief)
        print('updated Knowledgebase ', KB.KB)


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
        # if str.isalpha() and len(str) == 1:
        #     # single Letter needs no translation
        #     print('String is one literal :',str)
        #     return str
        #
        # if '~' in str and len(str)==2:
        #     return str
        # Basic variable translation:
        if 'NOT' in str:
            # translate negation
            # translates to ~R
            b= b.replace('NOT','~')
            #print('String has',b)

        if '^' in str or 'AND' in str:
            # translate conjunction (AND)
            str= str.replace('^','&')
            str = str.replace('AND','&')

        if 'v' in str or 'OR' in str:
            # translate disjunction (OR)
            str= str.replace('v','|')
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
            # this is momuntaritly wrong (bc of missing brackets), but it gets transformet correctly in seperate_ANDs

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


while True:
    B=KB()
    B.get_sentence()


#     kb = KB()                       # KB as class handle
#     conti = true
#     while conti == true
#     p = kb.tell()                   # Run tell method and get input from user
#     chanMeth = kb.ask()             # Run ask method to determen change_methode
#     if chanMeth == 'contraction':   # Run specified change method to update KB
#         KB = contraction(KB, p)
#     elif chanMeth == 'revision':
#         KB = revision(KB, p)
#     elif chanMeth == 'expansion':
#         KB = expansion(KB, p)
#     print('updated Knowledgebase is: ',kb.KB)
#
#     # ask if user wants to end
#     convar = input('Do you want to continue y/n : ')
#     if con convar == 'n':
#         conti = false


# def to_CNS(self, input):
#     # translates input to CNF format
#     # missing:
#         # what if more than one braket term
#         # distribute ANDs
#
#     input = input.replace(' ','')                                                       # removes all spaces in input
#     translation = ''
#     # seperates input in single () terms to translate, creates 'bracket_translation'
#     k=KB()
#     if '(' in input:
#         I='I'
#         end_idx = input.find(')')                                                       # finds end of 'bracket_term' that should get translated
#         start_idx = input.rfind('(', 0, end_idx)                                        # finds start of 'bracket_term'
#         bracket_term = input[start_idx+1:end_idx-1]                                     # saves 'bracket_term' (without brakets) as string
#         input = '%s%s%s' %(input[0:start_idx-1], I, input[end_idx+1:])                  # replaces '(bracket_term)' with placeholder 'I', gets rid of brakets
#         if translation == '':
#             translation = '(%s)' %k.replace_operator(bracket_term)                        # saves first part of CNS translation (with brackets)
#         else:
#             outer_translation = '(%s)' %k.replace_operator(bracket_term)                  # saves additional CNS translation with placeholder 'I'
#             translation = outer_translation.replace('I', '%s' %translation)             # replaces I with former translation
#     bracket_translation = k.replace_operator(input)
#     if 'I' in bracket_translation:                                                      # if 'I' was introduced as a placeholder
#         bracket_translation = bracket_translation.replace('I', '%s' %translation)       # replace 'I'
#
#     # translates negation over brackets ~(...)
#     #bracket_translation = k.bracket_negation(bracket_translation)
#
#     final_translation = bracket_translation
#     return(final_translation)
#def bracket_negation(self, bracket_translation):
#     bracket_translation = bracket_translation.replace('~~', '')                         # replaces douple negation
#     while '~(' in bracket_translation:
#         start_idx = bracket_translation.find('~(')                                       # finds start of 'bracket_term' that should get translated
#         next_bracket_end = bracket_translation.find(')', start_idx)                                    # finds start of 'bracket_term' that should get translated
#         while bracket_translation.count('(',start_idx, next_bracket_end) > 0:
#             next_bracket_end = bracket_translation.find(')', next_bracket_end)            # finds start of 'bracket_term' that should get translated
#         end_idx = next_bracket_end
#
#         if '(' in bracket_translation[start_idx+2, end_idx-1]:                          # +2 bc of two indexes '~('
#             inside_start_idx = bracket_translation[start_idx+2, end_idx-1].find('(')                                                       # finds end of 'bracket_term' that should get translated
#             inside_end_idx = bracket_translation[start_idx+2, end_idx-1].rfind(')')
#             bracket_term = bracket_translation[inside_start_idx:inside_end_idx]        # saves '(bracket_term)' (with brakets) as string
#             bracket_translation = '%s%s%s' %(bracket_translation[0:inside_start_idx-1], I, bracket_translation[inside_end_idx+1:])    # replaces '(bracket_term)' with placeholder 'I', gets rid of brakets
#
#         for c in bracket_translation:
#             if bracket_translation[c].isalpha():
#                 bracket_translation = bracket_translation[:c] + '~' + bracket_translation[c:]
#                 c=c+1
#         bracket_translation = bracket_translation.replace('|', '+')
#         bracket_translation = bracket_translation.replace('&', '|')
#         bracket_translation = bracket_translation.replace('+', '&')
#         bracket_translation = bracket_translation.replace('I', bracket_term)
#         bracket_translation = bracket_translation.replace('~~', '')                         # replaces douple negation