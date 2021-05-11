import copy
from itertools import product, chain
from time import sleep

class Resolution:
    def negate(self, Formula):
        formula = Formula.split(sep = '|')
        negated_formula = []
        for literal in formula:
            if len(literal) == 2:
                literal = literal[1]
            else:
                literal = '~' + literal
            negated_formula.append(literal)

        return negated_formula

    def resolveKB(self, KnB, Formula):
        re= Resolution
        KB = copy.deepcopy(KnB)
        alpha = copy.deepcopy(Formula)
        
        negated_alpha = re.negate(self, alpha)
        clauses = KB
        clauses_set = set(KB)
        [clauses.append(item) for item in negated_alpha]
        new = []
        new_set = set()
        iteration = 0

        while True:

            #print(clauses)
            for Ci_ind in range(len(clauses)):
                for Cj_ind in range(Ci_ind + 1, len(clauses)):
                    #print(Ci_ind, Cj_ind)
                    Ci, Cj = clauses[Ci_ind], clauses[Cj_ind]
                    #print(Ci, Cj)
                    resolvents = re.resolve(self, Ci, Cj)
                    #print(resolvents)
                    if str() == resolvents:
                        return True
                    if resolvents not in new_set: 
                        new.append(resolvents)
                        new_set.add(resolvents)
            if new_set.issubset(clauses_set):
                return False
            [clauses.append(item) for item in new if item not in clauses_set]
            [clauses_set.add(item) for item in new]
            iteration += 1 
    
    def resolve(self, A,B):

        statements = sorted([A.split(sep = '|'), B.split(sep = '|')], key = lambda x: len(x))

        resolved = copy.deepcopy(statements)
        for literal in statements[0]:
            if len(literal) == 2:
                neg_literal = literal[1]
            else:
                neg_literal = '~' + literal             
            if neg_literal in statements[1]:
                try:
                    resolved[0].remove(literal)
                    resolved[1].remove(neg_literal)
                except ValueError:
                    pass
        
        resolved = list(chain(*resolved))
        resolved = set(resolved)
        resolved = '|'.join(resolved)
        return resolved

    def resolvepossibilities(self, A,B):

        statements = sorted([A.split(sep = '|'), B.split(sep = '|')], key = lambda x: len(x))

        possibilities = []
        for literal in statements[0]:
            resolved = copy.deepcopy(statements)
            if len(literal) == 2:
                neg_literal = literal[1]
            else:
                neg_literal = '~' + literal             
            if neg_literal in statements[1]:
                resolved[0].remove(literal)
                resolved[1].remove(neg_literal)
                sentence = resolved[0]
                for item in resolved[1]:
                    sentence.append(item)
                possibilities.append(sentence)

        possibilities = [set(item) for item in possibilities]
        possibilities = ['|'.join(item) for item in possibilities]
                    
        return possibilities

if __name__ == "__main__":
    statement1 = 'p|q'
    statement2 = '~q|p'
    resolution = Resolution()
    resolved = resolution.resolve(statement1, statement2)
    print(str() == resolved)
    KB = ['p|q', '~q|p', '~p|r', '~p|s']
    alpha = 's'
    result = resolution.resolveKB(KB, alpha)
    print(result)
