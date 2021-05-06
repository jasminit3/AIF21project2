
# KB = [A|B, ~A, B]   dict = [~A, B, ~C]      input = ~B
# resolution -> false, do contraction
# contraction -> replace either A|B or B

# OR
# KB = [A|B]      input ~A     -->  KB = [~A, B]


# resolution returns false -> there needs to be a change
# contraction
# simplify KB


def contr(p, KB):
    # plan:
    # seperate brackets:
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
    #
    #without brackets (max two literals)
    if len(p) < 3:       #if only one (negated) literal
        a=p
        is_Issue_a = isIssue(a) # checks if issue with dictonary -> obsolete bc resolution?
        if is_Issue_a:
            print("contraction: KB: " ,KB, " gets updated with a: ", a)
            KB = replaceKB(a, KB)
            print('contraction: updated KB is: '%KB)
        return (KB)
    if '|' in p:
        # OR needs replacement if both of its sides return an issue with KB
        # split sentence p at opartor
        a=p.partition('|')[0]       # everything on the left
        b=p.partition('|')[-1]      # everything on the right
        # check if issue with respective part (save as var to save calc time) -> obsolete bc resolution?
        is_Issue_a = isIssue(a)
        is_Issue_b = isIssue(b)
        # replace the corresponding part of KB
        if is_Issue_a and is_Issue_b:
            # check which one is better to replace
#            KB = replaceKB( lowerPrio(a,b),KB) # needs function to determine variable with lower priority
            print('contraction: KB: ', KB, ' gets updated with b: ', b)
            KB = replaceKB(b,KB)
            print('contraction: updated KB is: ', KB)
        else:
            KB.append(p)
            print('Contranction added something to WB, why???')
        # similar with singel literals
        return (KB)


    def isIssue(str):
    # checks if there i an issue between literal in str and current belief (saved in dict)
        dict = Dictionary()
        literal =  str[-1]                  # seperates negation from literal (if there is a negation)
        val = dict.getTruelogic(literal)    # gets bool value of literal
        if '~' in str and val == False:     # if str=~A and A in dict is False: -> False
            return False
        elif '~' in str and val == True:    # if str=~A and A in dict is True:  -> True
            return True
        elif val == False:                  # if str= A and A in dict is False: -> False
            return False
        elif val == True:                   # if str= A and A in dict is True:  -> True
            return True


    def replaceKB(str,KB):
    # replaces str in KB with ~str, returns updated KB
        if '~' in str:                                                                  # if replace ~A
            old_entry = str                # old entry that gets replaxed               # old = ~A
            new_entry = str[-1]            # new entry that gets added                  # new = A
        else:                                                                           # if replace A
            old_entry =  str                # old entry that gets replaxed              # old = A
            new_entry = '~' + str           # new entry that gets added                 # new = ~A
        for k in KB:
            if old_entry in KB[k] and '|' in KB[k]:
                # if both sides have an issu
                a=str.partition('|')[0]       # everything on the left
                b=str.partition('|')[-1]      # everything on the right
                # check if issue with respective part (save as var to save calc time)
                is_Issue_a = isIssue(a)
                is_Issue_b = isIssue(b)
                if is_Issue_a and is_Issue_b:
                    KB.remove(KB[k])
                    KB.append(new_entry)
            elif old_entry in KB[k]:
                KB.remove(KB[k])
                KB.append(new_entry)
                if new_entry == str[-1]  :       # if replace ~A
                    newBelief(new_entry, True)
                elif new_entry == '~' + str:    # if replace A
                    newBelief(old_entry, False)
