import operator, types

class Dot(dict):
    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val

if __name__ == "__main__":
    foo = Dot()
    foo['xyz'] = 456
    print foo.xyz
    foo.abc = 123
    print foo['abc']
    print "> 200:", [e for e in foo if foo[e] > 200]
    print "> 100:", [e for e in foo if foo[e] > 100]
    foo = Dot()
    foo.dee = Dot(bar = 11111)
    foo['def'] = Dot({'bar': 11112})         #foo.def errors due to keyword
    print foo
    print "nested:",[e for e in foo if foo[e].bar > 11112]#foo.GE.bar(11112)
    x = [e for e in foo if foo[e].bar == 11111][0]
    print x, foo[x].bar
    print "pony style:", [e for e in foo if foo[e].bar > 11110 and foo[e].bar < 11112]
    