#from utils import expr
import sympy


class CNF:
#page 253 and 254 in book (chapter 7)

#1. Make method that: checks if input is from alphabet and has operator (
#2. Make method that: eliminate <=> and <=/=>(implications into equivalent form, replacing them with "&" (AND), "|"(OR) and "~" (NOT))
#3. Make method that: "move NOT inwards" with double-negation elimination or De Morgan (depends) so that it only appears in literals
#4. Make method that: Apply distributivity law, distributing OR over AND wherever possible
#5. Make method that takes input and puts it through method 2., 3. and 4. and returns the original sentence/belief into CNF


        #characters = "P, C, H, L"

        def convert_to_cnf(s):
            s = expr(s)

          #  if isinstance(s, str) #returns True, if "s" is of the type string, else False


        def eliminations(s):

            s = expr(s)
            operators = s.op #&|<=~
            character_first = isinstance(s, str) and s[:1].isalpha(operators)

            if not s.args or character_first:
                return s

            print("Halli Hallo")

CNF=CNF()
CNF.eliminations()

           # elements_from_input = list(map(eliminations, s.args))
            #
            #P, C, H, L = args[0], args [1], args[2], args[3]
            #if (s == '==>'):
            #    return P | ~













