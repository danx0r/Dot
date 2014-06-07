import operator, types

class Dot(dict):
    def __init__(self, *args):
        dict.__init__(self, *args)
        dict.__setattr__(self, 'GE', DotComparator(self, operator.ge))      #our __setattr__ is overloaded! use base class method
        dict.__setattr__(self, 'EQ', DotComparator(self, operator.eq))

    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val
        
    def __repr__(self):
        temp = dict(self)
        return repr(temp)

class DotComparator(object):
    def __init__(self, super, op, attr=None):
        self.super = super
        self.op = op
        self.attr = attr

    def __getitem__(self, attribute):
        return DotComparator(self.super, self.op, attribute)

    def __getattr__(self, attribute):
        return DotComparator(self.super, self.op, attribute)

    def __call__(self, val):
        result = []
        for key in self.super:
#             print "COMPARE:", self.super[key], ">=", val
            if self.attr:
                try:
                    if self.attr in self.super[key] and self.op(self.super[key][self.attr], val):
                        result.append(key)
                except:
                    pass
            else:
                if self.op(self.super[key], val):
                    result.append(key)
        return result

if __name__ == "__main__":
    foo = Dot()
    foo['xyz'] = 456
    print foo.xyz
    foo.abc = 123
    print foo['abc']
    foo.dee = Dot({'bar': 11111})
    foo['def'] = Dot({'bar': 11112})         #foo.def errors due to keyword
    print foo
    print "> 200:", foo.GE(200)
    print "> 100:", foo.GE(100)
    print "nested:", foo.GE.bar(11112)
    x = foo.EQ['bar'](11111)[0]
    print foo[x].bar
