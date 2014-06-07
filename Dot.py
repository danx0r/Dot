import operator, types

class Dot(dict):
    def __init__(self, *args, **kw):
        dict.__init__(self, *args, **kw)
        dict.__setattr__(self, 'GE', DotCompareMethod(self, operator.ge))      #our __setattr__ is overloaded! use base class method
        dict.__setattr__(self, 'EQ', DotCompareMethod(self, operator.eq))

    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val

    def AND(self, *args):
#         print "DEBUG AND args:", args
        result = []
        for key in self:
#             print "AND COMPARE:", key, args
            do = True
            for op, test, val in args:
                try:
                    if not op(self[key][test], val):
                        do = False
                except:
                    do = False
            if do:
                result.append(key)
        return result
        
    def __repr__(self):
        temp = dict(self)
        return repr(temp)

def isDictType(d):
    try:
        d.has_key
    except:
        return False
    return True

class DotCompareMethod(object):
    def __init__(self, super, op, attr=None):
        self.super = super
        self.op = op
        self.attr = attr

    def __getitem__(self, attribute):
        return DotCompareMethod(self.super, self.op, attribute)

    def __getattr__(self, attribute):
        return DotCompareMethod(self.super, self.op, attribute)

    def __call__(self, val):
        result = []
        for key in self.super:
#             print "COMPARE:", self.super[key], ">=", val
            if self.attr:
                try:
                    if self.attr in self.super[key] and self.op(self.super[key][self.attr], val):
                        a = self.super[key][self.attr]
                        if isDictType(a) == isDictType(val):
                            result.append(key)
                except:
                    pass
            else:
                a = self.super[key]
#                 print "DEBUG", a, val, isDictType(a), isDictType(val), isDictType(a) == isDictType(val)
                if isDictType(a) == isDictType(val):
                    if self.op(a, val):
                        result.append(key)
        return result

class DotCompareFunction(object):
    def __init__(self, op, attr=None):
        self.super = super
        self.op = op
        self.attr = attr

    def __getitem__(self, attribute):
        return DotCompareFunction(self.op, attribute)

    def __getattr__(self, attribute):
#         print "DEBUG DotCompare attr:", attribute
        return DotCompareFunction(self.op, attribute)

    def __call__(self, val):
#         print "DEBUG DotCompare Call:", self, val
        return (self.op, self.attr, val)

GT = DotCompareFunction(operator.gt)
LT = DotCompareFunction(operator.lt)

if __name__ == "__main__":
    foo = Dot()
    foo['xyz'] = 456
    print foo.xyz
    foo.abc = 123
    print foo['abc']
    foo = Dot()
    foo.dee = Dot(bar = 11111)
    foo['def'] = Dot({'bar': 11112})         #foo.def errors due to keyword
    print foo
    print "> 200:", [e for e in foo if foo[e] > 200]
    print "> 100:", [e for e in foo if foo[e] > 100]
    print "nested:",[e for e in foo if foo[e].bar > 11112]#foo.GE.bar(11112)
    x = [e for e in foo if foo[e].bar == 11111][0]
    print x, foo[x].bar
#     print "AND:", foo.AND(GT.bar(11110), LT.bar(11112))
    print "pony style:", [e for e in foo if foo[e].bar > 11110 and foo[e].bar < 11112]
    