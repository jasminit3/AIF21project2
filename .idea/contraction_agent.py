import Resolution


class MI_contraction:
    def __init__(self, KB):
        self.KB = KB
    
    def ContractionMI(self, contraction_statement):
        """Performs contraction on a given KB"""
        # This method takes only CNF input for all its operations, uses a list of sets to represent the KB internally amd perform operations.
        # Uses Entrenchment for cases where the random decision are to be made.
        # The entrenchment used is the position of the given letter in the alphabet.
        # Z has more priority over A.
        KB_rep = [set(string.split(sep = '|')) for string in self.KB]
        res = Resolution.Resolution()
        contraction_statement_raw = contraction_statement.upper()
        contraction_statement_raw = contraction_statement_raw.replace(' ', '')
        and_count = contraction_statement_raw.count('&')
        or_count = contraction_statement_raw.count('|')
        if '&' in contraction_statement_raw:
            contraction_statement = contraction_statement_raw.split(sep = '&')
            contraction_statement_rep = [string.split(sep = '|') for string in contraction_statement if string != '~']
        else:
            contraction_statement_rep = contraction_statement_raw.split(sep = '|')
        

        solo, statement_check = False, False

        if len(contraction_statement_raw) == 2:
            contraction_statement_rep = [contraction_statement_rep]

        
        if and_count == 0 and or_count != 0:
            contraction_statement_rep = [contraction_statement_rep]
        
        
        if res.resolveKB(self.KB, contraction_statement_raw):           # Performs contraction only if the entire CNF contraction statement is true.
            for index in range(len(contraction_statement_rep)):
                statement = contraction_statement_rep[index]
                statement = sorted(statement, key = lambda x: ord(x) if len(x) < 2 else len(x))
                KB_statement = '|'.join(statement)
                truth_value = res.resolveKB(self.KB, KB_statement)
                single_literal = False
                if truth_value:
                    if solo:
                            single_literal = True
                    else:
                        try:
                            [statement] = statement
                            single_literal = True
                        except ValueError:
                            single_literal = False
                
                    if single_literal:
                        for location, sentence in enumerate(KB_rep):
                            literal = statement
                            if literal in sentence:
                                KB_rep[location].remove(literal)
                                break
                    else:
                        truth = [res.resolveKB(self.KB, literal) for literal in statement]
                        pos = [i for i, x in enumerate(truth) if not x]
                        for position in pos:
                            literal = statement[position]
                            for location, sentence in enumerate(KB_rep):
                                if literal in sentence:
                                    KB_rep[location].remove(literal)
                                    break
                            break
            
                while True:
                    try:
                        KB_rep.remove(set())
                    except ValueError:
                        break

                self.KB = ['|'.join(sentence) for sentence in KB_rep]
            
            if len(self.KB) == 0:
                print(self.KB)
                return False
            else:
                print(self.KB)
                return True

        else:
            # new belief follows KB therefore can directly be added into the KB if performing revision.
            print(self.KB)
            return True

if __name__ == "__main__":
    while True:
        user_input = input('Enter Knowledge base? (1 for preexisting 2 for new q to quit)\t')
        if user_input == '1':
            KB = ['~A', 'B|F', '~C', 'D']
            print(KB)
        elif user_input == '2':
            KB = input('Enter the entire KB in CNF format without brackets:    ')
            KB = KB.replace(' ', '')
            if '&' in KB:
                KB = KB.split(sep = '&')
            print(KB)
        elif user_input == 'q':
            quit()
        
        agent = MI_contraction(KB)
        ret = True
        while ret:
            contraction_statement = input("statement to be contracted from KB in CNF format(q to quit): ")
            if contraction_statement == 'q':
                quit()
            else:
                ret = agent.ContractionMI(contraction_statement)
