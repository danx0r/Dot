import operator, types

class Dot(dict):
    def __init__(self, *args):
        dict.__init__(self, *args)
        self.GE = DotComparator(self, operator.ge)

    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val
        
    def __repr__(self):
        temp = dict(self)
        del temp['GE']
        return repr(temp)

class DotComparator(object):
    def __init__(self, super, op):
        self.super = super
        self.op = op

    def __getattr__(self, attribute):
#         print "GE attrib:", attribute
        return DotComparator(self.super, self.op)

    def __call__(self, val):
#         print "GE call():", args
        result = []
        for key in self.super:
            if key != 'GE':
                if self.super[key] >= val:
                    result.append(key)
        return result

# Dot.GE = DotComparator(operator.ge)

if __name__ == "__main__":
    foo = Dot()
    foo['xyz'] = 456
    print foo.xyz
    foo.abc = 123
    print foo['abc']
    foo['def'] = Dot({'bar': 11111})         #foo.def errors due to keyword
    print foo
    print "> 200:", foo.GE(200)
    print "> 100:", foo.GE(100)
    print "nested:", foo.GE.bar(11112)