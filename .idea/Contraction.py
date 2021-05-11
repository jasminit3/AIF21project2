import Dictionary
import Resolution


class Contraction:
# Examples:

    #                       KB          dict        new_entry       new_KB              change / comment
    #lit - lit:             [A]         [A]         [~A]            [~A]                conflict with dict -> replace lit

    #statement - lit        [A, A|B]    [A]         [~A]            [~A, B]             conflict with dict -> replace lit, make sence out of statement*  (check bothsides of statement with new_entry)
    #statement - lit        [A,A|~B]    [A]         [~A]            [~A,~B]             conflict with dict -> replace lit, make sence out of statement*
    #statement - lit        [A,A|~B]    [A,B]       [~A]            [~A]                conflict with dict -> replace lit, make sence out of statement*
    #statement - lit        [A,~A|B]*** [A,B]       [~A]            [~A, B]

    #lit - statement        [A,B]       [A,B]       [-A|-B]         [-A|-B]             conflict on both sides w/ dict -> replace both (check bothsides of new_entry with dict)
    #lit - statement        [A,B]       [A,B]       [-A|B]          [A,B] or [A,-A|B]   conflict on one side -> not part of contraction**

    #statement - statement  [A,~A|B]    [A,~B]      [~A|~B]         [A,~B]              no contraction **
    #statement - statement  [A,~A|B]    [A, B]      [~A|~B]         [A,~B],[~A,B]       conflict on both sides w/ dict -> conflict with KB correction -> as for prio
    #statement - statement  [A,A|B]     [A, B]      [~A|~B]         [A,~B],[~A,B]       conflict on both sides w/ dict -> conflict with KB correction -> as for prio
    #statement - statement  [A,~A|B]    [A,B]       [A|~B]          [A,B]               no contraction **
    #statement - statement  [A,~A|B]    [A,~B]      [A|~B]          []                  no contraction **
    #statement - statement  [A,~A|B]    [A,B]       [A|B]           []                  no contraction **

    #* make sence out of statement:
        # check left and right side seperatly
            # add side w/o conflict as new lit
            # if both sides -> remove entire statement

    # ** check if part of resolution?
    # *** shouldn't be a valid KB


    def contract(self, new_entry):
        # information:
        # new contraction method, hopefully better and shorter than contr()
        # implemented for statements containing not more than two literals

        co = Contraction
        re = Resolution
        KB = Dictionary.Dictionary.KB

        # contraction with one literal
        if len(new_entry) < 3:
            # negate new_entry
            old_entry = '~' + new_entry
            old_entry = old_entry.replace('~~','')
            # check if new_entry has conflickt with dictionary
            if co.isIssue(self, new_entry):
                print("Contraction: single literal in KB: ", KB, " gets updated with singe literal a: ", new_entry)
                KB = co.replaceLiteral(self, new_entry, KB)

            # in addition, check if old_entry is part of OR-statement in KB
            for k in KB:
                if old_entry in k and '|' in k:
                    old_entry_a = k.partition('|')[0]   # everything on the left
                    old_entry_b = k.partition('|')[-1]  # everything on the right

                    # check for left and right halfs if conflict with dict
                    aIssue = co.isIssue(self, old_entry_a)
                    bIssue = co.isIssue(self, old_entry_b)
                    print("Contraction: OR-statement in KB: ", KB, " gets updated with singe literal a: ", new_entry)

                    if aIssue and bIssue:
                        # if conflict on both sides -> remove entire OR-statement
                        KB.remove(k)
                    elif aIssue:
                        # if conflict on left side -> remove entire OR-statement, append right side
                        KB.remove(k)
                        KB.append(old_entry_b)
                        co.updateDict(self, old_entry_b)
                    elif bIssue:
                        # if conflict on right side -> remove entire OR-statement, append left side
                        KB.remove(k)
                        KB.append(old_entry_a)
                        co.updateDict(self, old_entry_a)
                    # else:
                        # do nothing

        # literal contraction with OR-statement
        #statement - statement  [A,~A|B]    [A, B]      [~A|~B]         [A,~B],[~A,B]       conflict on both sides w/ dict -> conflict with KB correction -> as for prio, remove Or-Statement
        #statement - statement  [A,A|B]     [A, B]      [~A|~B]         [A,~B],[~A,B]       conflict on both sides w/ dict -> conflict with KB correction -> as for prio

        if '|' in new_entry:
            new_entry_a = new_entry.partition('|')[0]   # everything on the left
            new_entry_b = new_entry.partition('|')[-1]  # everything on the right
            # negate new_entrys
            old_entry_a = '~' + new_entry_a
            old_entry_a = old_entry_a.replace('~~','')
            old_entry_b = '~' + new_entry_b
            old_entry_b = old_entry_b.replace('~~','')
            # check for left half if conflict with dict
            aIssue = co.isIssue(self, new_entry_a)
            bIssue = co.isIssue(self, new_entry_b)

            if aIssue and bIssue:
                # conflict on both sides w/ dict -> ask user for prio input
                # solution wih least changes would also be nice
                print("Please specify literal that should be replaced: ", old_entry_a,"or", old_entry_b,": ")
                low_prio = input()
                print(low_prio)
                # check input
                while low_prio != old_entry_a and low_prio != old_entry_b:
                    print("Please check spelling of literal that should be replaced: ", old_entry_a,"or", old_entry_b,": ")
                    low_prio = input()

                for k in KB:
                    if k == low_prio:
                        # if low_prio is found in KB -> remove it and update Dict
                        KB.remove(k)
                        # negate low_prio
                        low_prio_neg = '~' + low_prio
                        low_prio_neg = low_prio_neg.replace('~~','')
                        co.updateDict(self, new_entry_a)

                    elif k == old_entry_a + '|' + old_entry_b or k == new_entry_a + '|' + old_entry_b or k == new_entry_a + '|' + new_entry_b:
                        # if OR-statement is found in KB (with conflict on one or two sides) -> remove it
                        ('This should be removed from KB', k)
                        KB.remove(k)

         #check if KB has three entries
        KB = co.checkKB(self, KB)
        # return updated KB in the end
        print('Contraction: updated KB is: ', KB)
        return (KB)

    def checkKB(self, KB):
        if len(KB) < 3:
            # removed literals imply that the opposite is true
            dict = Dictionary.Dictionary
            if 'A' not in KB and '~A' not in KB:
                if dict.getTruelogic(self, 'A'):  # gets bool value of literal
                    KB.append('A')
                else:
                    KB.append('~A')
            if 'B' not in KB and '~B' not in KB:
                if dict.getTruelogic(self, 'B'):  # gets bool value of literal
                    KB.append('B')
                else:
                    KB.append('~B')
            if 'C' not in KB and '~C' not in KB:
                if dict.getTruelogic(self, 'C'):  # gets bool value of literal
                    KB.append('C')
                else:
                    KB.append('~C')
        return KB


    def replaceLiteral(self, new_entry, KB):
        # replaces a single literal with another single literal (both can be negated)
        # negate new_entry
        old_entry = '~' + new_entry
        old_entry = old_entry.replace('~~','')
        # delete old entry in KB
        Dictionary.Dictionary.KB.remove(old_entry)
        # add new entry
        Dictionary.Dictionary.KB.append(new_entry)
        # update Dicionary
        Contraction.updateDict(self, new_entry)
        KB=Dictionary.Dictionary.KB
        return (KB)


    def isIssue(self, str):
        # checks if there is an conflict between the literal in str and current belief (saved in dict)
        # returns True if conflict, False if no conflict
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


    def updateDict(self, new_entry):
        if new_entry[0].isalpha():
            Dictionary.Dictionary.newBelief(self, new_entry[0], True)
        elif new_entry[0].isalpha() == False:
            Dictionary.Dictionary.newBelief(self, new_entry[-1], False)


    # def contr(self, new_entry):
    #     # function contracts KB in a way that p can be appended to KB without conflicts
    #     co = Contraction
    #     #di = Dictionary.Dictionary
    #     re = Resolution
    #     KB = Dictionary.Dictionary.KB
    #     if len(new_entry) < 3:  # if only one (negated) literal
    #         # checks if issue with dictonary -> obsolete bc resolution?
    #         if co.isIssue(self, new_entry):
    #             print("Contraction: KB: ", KB, " gets updated with singe literal a: ", new_entry)
    #             co.replaceKB(self, new_entry, KB)
    #             print('Contraction: updated KB is: ', KB)
    #         # remove all dublicates in KB
    #         #KB = list(dict.fromkeys(KB))
    #         return (KB)
    #     if '|' in new_entry:
    #         # replacement with input with OR operator
    #         a = new_entry.partition('|')[0]  # everything on the left
    #         b = new_entry.partition('|')[-1]  # everything on the right
    #         old_a = '~' + a
    #         old_a.replace('~~', '')
    #         old_b = '~' + b
    #         old_b.replace('~~', '')
    #         # check if issue with respective part (save as var to save calc time) -> obsolete bc resolution?
    #         is_Issue_a = co.isIssue(self, a)
    #         is_Issue_b = co.isIssue(self, b)
    #         # replace the corresponding part of KB
    #         print('isisue a', is_Issue_a,'isisue b', is_Issue_b)
    #         if is_Issue_a and is_Issue_b :
    #             # check which one is better to replace
    #             # KB = replaceKB( lowerPrio(a,b),KB) # needs function to determine variable with lower priority
    #             print('Contraction: KB: ', KB, ' gets contracted with b: ', b)
    #             co.replaceKB(self, b, KB)
    #             print('Contraction: updated KB is: ', KB)
    #         if is_Issue_a == False and is_Issue_b==False: # if both literals are true and already in KB, replaced with A|B
    #                 KB.remove(a)
    #                 KB.remove(b)
    #                 KB.append(new_entry)
    #                 print('KB:', KB,'new entry', new_entry)
    #         else:
    #             # simplyfy KB accordingly
    #             print('Contraction: KB: ', KB, ' gets simplified with b: ', b)
    #             # negations of a and b
    #             # old_a = '~' + a
    #             # old_a.replace('~~', '')
    #             # old_b = '~' + b
    #             # old_b.replace('~~', '')
    #             for k in KB:
    #                 x = KB.index(k)
    #                 if is_Issue_a and old_a in KB[x]:
    #                     # if left issue -> replace left statement in KB
    #                     KB.remove(KB[x])
    #                     KB.append(new_entry)
    #                 if is_Issue_b and old_b in KB[x]:
    #                     # if right issue -> replace right statement in KB
    #                     KB.remove(KB[x])
    #                     KB.append(new_entry)
    #         print('Contraction: updated KB is: ', KB)
    #         return KB



    # def replaceKB(self, new_entry, KB):
    #     K = Dictionary.Dictionary.KB
    #     co = Contraction
    #     re = Resolution
    #     # replaces ~str in KB with str, returns updated KB
    #     if len(new_entry) > 3:
    #         new_entry_a = new_entry.partition('|')[0]  # everything on the left
    #         new_entry_b = new_entry.partition('|')[-1]
    #         old_entry_a = '~' + new_entry_a
    #         old_entry_a.replace('~~', '')
    #         old_entry_b = '~' + new_entry_b
    #         old_entry_b.replace('~~', '')
    #         for k in len(K):
    #             if old_entry_a in K[k] or old_entry_b in K[k]:
    #                 K.remove(K[k])
    #                 K.append(new_entry)
    #
    #     if len(new_entry) < 3:  # if only one (negated) literal
    #         # creates negation of input p
    #         old_entry = '~' + new_entry
    #         old_entry =old_entry.replace('~~', '')
    #         print('Replace kb: new entry ', new_entry, 'old entry',old_entry)
    #         for k in K:
    #             x = K.index(k)
    #             # ............... if KB[k] is OR statement ...............
    #             if old_entry in K[x] and '|' in K[x]:  # KB = [A|B] new_entry : [~A]
    #                 a = k.partition('|')[0]  # everything on the left
    #                 b = k.partition('|')[-1]  # everything on the right
    #                 print('replace a: ',a,'b: ',b)
    #                 # check if issue with respective part (save as var to save calc time)
    #                 is_Issue_a = not bool(re.resolve(new_entry, a))  # ???
    #                 is_Issue_b = not bool(re.resolve(new_entry, b))  # ???
    #                 if is_Issue_a and is_Issue_b:
    #                     # if two issus -> remove entire or statement, keep new_entry
    #                     K.remove(K[x])
    #                     K.append(new_entry)
    #                     co.updateDict(self, new_entry)
    #                 if is_Issue_a and is_Issue_b == False:
    #                     # if left issue -> keep right statement and new_entry
    #                     K.remove(K[x])
    #                     K.append(b)
    #                     co.updateDict(self, b)
    #                     K.append(new_entry)
    #                     co.updateDict(self, new_entry)
    #                 if is_Issue_a == False and is_Issue_b:
    #                     # if right issue -> keep left statement and new_entry
    #                     K.remove(K[x])
    #                     K.append(a)
    #                     co.updateDict(self, a)
    #                     K.append(new_entry)
    #                     co.updateDict(self, new_entry)
    #
    #             # ..... if KB[k] is only (negated) literal ...............
    #             elif old_entry in K[x]:
    #                 K.remove(k)
    #                 print('Remove old string', k)
    #                 K.append(new_entry)
    #                 print('New literal: ',new_entry,'new KB is:', Dictionary.Dictionary.KB)
    #                 co.updateDict(self, new_entry)