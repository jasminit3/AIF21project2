import copy
from itertools import chain

class Resolution:
    """Resolution class used to perform the resolution algorithm by internally using a resolution graph"""

    def _negate(self, Formula):
        """This function is used to negate the formula that is to be checked using resolution"""
        
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
        """Takes the entire knowledge base and the formula in CNF form for the logical entailment check"""
        # Note : Assumes the formula is always a clause.(i.e in cnf format without spaces)
        # Here, the function operates on multiple literals and multiple sentences.
        re= Resolution
        KB = copy.deepcopy(KnB)
        formula = copy.deepcopy(Formula)
        formula = formula.replace(' ', '')
        if '&' in formula:
            formula = formula.split(sep = '&')

        logical_entailment = []
        for alpha in formula:
            negated_alpha = re._negate(self, alpha)
            clauses = KB
            clauses_set = set(KB)
            [clauses.append(item) for item in negated_alpha]
            new = []
            new_set = set()
            entails = False
            iteration = 0

            while True:

                #print(clauses)
                for Ci_ind in range(len(clauses)):
                    for Cj_ind in range(Ci_ind + 1, len(clauses)):
                        #print(Ci_ind, Cj_ind)
                        Ci, Cj = clauses[Ci_ind], clauses[Cj_ind]
                        #print(Ci, Cj)
                        resolvents = re._resolve(self, Ci, Cj)
                        #print(resolvents)
                        if str() == resolvents:
                            entails = True
                        if resolvents not in new_set: 
                            new.append(resolvents)
                            new_set.add(resolvents)
                if entails:
                    break
                if new_set.issubset(clauses_set):
                    entails = False
                    break
                [clauses.append(item) for item in new if item not in clauses_set]
                [clauses_set.add(item) for item in new]
                iteration += 1
            
            logical_entailment.append(entails)

        # print(logical_entailment)
        if all(logical_entailment):
            return True
        else:
            return False 
    
    def _resolve(self, A,B):
        """This function takes two clauses as input and returns the resolved clause if resolution can be applied."""
        # Note: This function fuses the clauses using logical OR if they cannot be resolved. This is because the function never sees a logical AND
        # as per this implementation.

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

    def _resolvepossibilities(self, A,B):
        """Used as a test function, it return all the possibilities for resolving clauses A and B."""
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
    # Write the code to test the working of this module of the belief revision agent, a template has been provided below.
    resolution = Resolution()
    statement1 = 'p|q'
    statement2 = '~q|p'
    resolved = resolution._resolve(statement1, statement2) # Do not use this function outside this module as it may not give preferable results
    print("statement 1 = {}\tstatement 2 = {}\tresolved = {}".format(statement1, statement2, resolved))
    KB = ['p|q', '~q|p', '~p|r', '~p|s']
    alpha = 'p & r|q|e & s'
    result = resolution.resolveKB(KB, alpha)
    print('\nKB = ', KB)
    print("Formula = ",alpha, "\nLogically entails the KB?\n", result)
