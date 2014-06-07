import operator, types

class Dot(dict):
    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val

    def select(self, gen):
        return list(gen)

if __name__ == "__main__":
    foo = Dot()
    foo['xyz'] = 456
    print foo.xyz
    foo.abc = 123
    print foo['abc']
    print "> 200:", foo.select(e for e in foo if foo[e] > 200)
    print "> 100:", foo.select(e for e in foo if foo[e] > 100)
    foo = Dot()
    foo.dee = Dot(bar = 11111)
    foo['def'] = Dot({'bar': 11112})         #foo.def errors due to keyword
    print foo
    print foo.select(e for e in foo if foo[e].bar > 11110 and foo[e].bar < 11112)
    