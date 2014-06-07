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
    foo.update = 'bar'
    print foo.update                            #doesn't work; still a method
    print foo['update']
    foo = Dot()
    foo.abc = Dot(bar = 4, bat = 5)
    foo['def'] = Dot(bar = 7, bat = 8)          #.def reserved; foo.def = syntax error
    print [e for e in foo if foo[e].bar == 7]