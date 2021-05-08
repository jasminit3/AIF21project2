import Dictionary
import Resolution


class Contraction:


    # Contraction plan:
    # seperate brackets
    # negate input
    # seperate string at operator
    # for single literal
    # replace KB
    # check logical outcome
    # for OR
    # leftside: remove ~, look for issues with directory
    # rightside:    - "" -
    # change KB accordingly
    # return KB
    #

    def contr(self, new_entry):
        # function contracts KB in a way that p can be appended to KB without conflicts
        co = Contraction
        #di = Dictionary.Dictionary
        re = Resolution
        KB = Dictionary.Dictionary.KB
        if len(new_entry) < 3:  # if only one (negated) literal
            # checks if issue with dictonary -> obsolete bc resolution?
            if co.isIssue(self, new_entry):
                print("Contraction: KB: ", KB, " gets updated with singe literal a: ", new_entry)
                co.replaceKB(self, new_entry, KB)
                print('Contraction: updated KB is: ', KB)
            # remove all dublicates in KB
            #KB = list(dict.fromkeys(KB))
            return (KB)
        if '|' in new_entry:
            # replacement with input with OR operator
            a = new_entry.partition('|')[0]  # everything on the left
            b = new_entry.partition('|')[-1]  # everything on the right
            old_a = '~' + a
            old_a.replace('~~', '')
            old_b = '~' + b
            old_b.replace('~~', '')
            # check if issue with respective part (save as var to save calc time) -> obsolete bc resolution?
            is_Issue_a = co.isIssue(self, a)
            is_Issue_b = co.isIssue(self, b)
            # replace the corresponding part of KB
            print('isisue a', is_Issue_a,'isisue b', is_Issue_b)
            if is_Issue_a and is_Issue_b :
                # check which one is better to replace
                # KB = replaceKB( lowerPrio(a,b),KB) # needs function to determine variable with lower priority
                print('Contraction: KB: ', KB, ' gets contracted with b: ', b)
                co.replaceKB(self, b, KB)
                print('Contraction: updated KB is: ', KB)
            if is_Issue_a == False and is_Issue_b==False: # if both literals are true and already in KB, replaced with A|B
                    KB.remove(a)
                    KB.remove(b)
                    KB.append(new_entry)
                    print('KB:', KB,'new entry', new_entry)
            else:
                # simplyfy KB accordingly
                print('Contraction: KB: ', KB, ' gets simplified with b: ', b)
                # negations of a and b
                # old_a = '~' + a
                # old_a.replace('~~', '')
                # old_b = '~' + b
                # old_b.replace('~~', '')
                for k in KB:
                    x = KB.index(k)
                    if is_Issue_a and old_a in KB[x]:
                        # if left issue -> replace left statement in KB
                        KB.remove(KB[x])
                        KB.append(new_entry)
                    if is_Issue_b and old_b in KB[x]:
                        # if right issue -> replace right statement in KB
                        KB.remove(KB[x])
                        KB.append(new_entry)

            # remove all dublicates in KB
            #KB = list(dict.fromkeys(KB))
            print('Contraction: updated KB is: ', KB)
            return KB


    def isIssue(self, str):
        # checks if there is an issue between literal in str and current belief (saved in dict)
        dict = Dictionary.Dictionary
        literal = str[-1]  # seperates negation from literal (if there is a negation)
        val = dict.getTruelogic(self, literal)  # gets bool value of literal
        if '~' in str and val == False:  # if str=~A and A in dict is False: -> False
            return False
        elif '~' in str and val == True:  # if str=~A and A in dict is True:  -> True
            return True
        elif val == False:  # if str= A and A in dict is False: -> True
            return True
        elif val == True:  # if str= A and A in dict is True:  -> False
            return False

    def replaceKB(self, new_entry, KB):
        K = Dictionary.Dictionary.KB
        co = Contraction
        re = Resolution
        # replaces ~str in KB with str, returns updated KB
        if len(new_entry) > 3:
            new_entry_a = new_entry.partition('|')[0]  # everything on the left
            new_entry_b = new_entry.partition('|')[-1]
            old_entry_a = '~' + new_entry_a
            old_entry_a.replace('~~', '')
            old_entry_b = '~' + new_entry_b
            old_entry_b.replace('~~', '')
            for k in len(K):
                if old_entry_a in K[k] or old_entry_b in K[k]:
                    K.remove(K[k])
                    K.append(new_entry)

        if len(new_entry) < 3:  # if only one (negated) literal
            # creates negation of input p                                                 # Example
            old_entry = '~' + new_entry
            old_entry =old_entry.replace('~~', '')
            print('Replace kb: new entry ', new_entry, 'old entry',old_entry)
            for k in K:
                x = K.index(k)
                # ............... if KB[k] is OR statement ...............
                if old_entry in K[x] and '|' in K[x]:  # KB = [A|B] new_entry : [~A]
                    a = k.partition('|')[0]  # everything on the left
                    b = k.partition('|')[-1]  # everything on the right
                    print('replace a: ',a,'b: ',b)
                    # check if issue with respective part (save as var to save calc time)
                    is_Issue_a = not bool(re.resolve(new_entry, a))  # ???
                    is_Issue_b = not bool(re.resolve(new_entry, b))  # ???
                    if is_Issue_a and is_Issue_b:
                        # if two issus -> remove entire or statement, keep new_entry
                        K.remove(K[x])
                        K.append(new_entry)
                        co.updateDict(self, new_entry)
                    if is_Issue_a and is_Issue_b == False:
                        # if left issue -> keep right statement and new_entry
                        K.remove(K[x])
                        K.append(b)
                        co.updateDict(self, b)
                        K.append(new_entry)
                        co.updateDict(self, new_entry)
                    if is_Issue_a == False and is_Issue_b:
                        # if right issue -> keep left statement and new_entry
                        K.remove(K[x])
                        K.append(a)
                        co.updateDict(self, a)
                        K.append(new_entry)
                        co.updateDict(self, new_entry)

                # ..... if KB[k] is only (negated) literal ...............
                elif old_entry in K[x]:
                    K.remove(k)
                    print('Remove old string', k)
                    K.append(new_entry)
                    print('New literal: ',new_entry,'new KB is:', Dictionary.Dictionary.KB)
                    co.updateDict(self, new_entry)


    def updateDict(self, new_entry):
        if new_entry[0].isalpha():
            Dictionary.Dictionary.newBelief(self, new_entry[0], True)
        elif new_entry[0].isalpha() == False:
            Dictionary.Dictionary.newBelief(self, new_entry[-1], False)