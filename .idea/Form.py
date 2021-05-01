class Form:

    def __invert__(self):
        return Not(self)
    def __and__(self, other):
        return And(self, other)
    def __or__(self, other):
        return Or(self, other)
    def __rshift__(self, other):
        return Implies(self, other)
    def __lshift__(self, other):
        return Iff(self, other)