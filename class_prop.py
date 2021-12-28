class ExamplePlain:
    def __init__(self, inp):
        self.inp = inp
    def brackets(self):
        return '<' + self.inp + '>'
    def braces(self):
        return '(' + self.brackets() + ')'

class ExampleProp:
    def __init__(self, inp):
        self.inp = inp
    @property
    def brackets(self):
        return '<' + self.inp + '>'
    @property
    def braces(self):
        return '(' + self.brackets + ')'

e1 = ExamplePlain('this')
print(e1.braces())
e2 = ExampleProp('that')
print(e2.braces)