import copy

def resolve(A,B):

    operations = {'&', '|'}
    literals_of_A = [i for i in A if i not in operations]
    literals_of_B = [i for i in B if i not in operations]
    
    literals = set()
    found_not = False
    for literal in literals_of_A:
        if found_not:
            literals.add("~" + str(literal))
        if literal == "~":
            found_not = True
            continue
        else:
            if found_not:
                found_not = False
            else:
                literals.add(literal)
    
    found_not = False
    for literal in literals_of_B:
        if found_not:
            literals.add("~" + str(literal))
        if literal == "~":
            found_not = True
            continue
        else:
            if found_not:
                found_not = False
            else:
                literals.add(literal)


    resolved = copy.deepcopy(literals)
    for literal in literals:
        if len(literal) == 2:
            literal = literal[1]
        else:
            literal = '~' + literal
        if literal in literals:
            try:
                resolved.remove(literal)
                if len(literal) == 2:
                    resolved.remove(literal[1])
                else:
                    resolved.remove('~' + literal)
            except KeyError:
                pass
    return resolved

if __name__ == "__main__":
    statement1 = 'p|q'
    statement2 = '~p|~q'
    resolved = resolve(statement1, statement2)
    print(resolved)
