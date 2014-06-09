#
# dict with js-like dot access
#
class Dot(dict):
    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val

    def __setitem__(self, key, val):
        if type(val) == dict:
            val = Dot(val)
        dict.__setitem__(self, key, val)

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
    foo.abc = Dot(bar = Dot(far = 3), bat = 5)
    foo['def'] = Dot(bar = Dot(far = 7), bat = 8)          #.def reserved; foo.def = syntax error
    print foo
    print [e for e in foo if foo[e]['bar']['far'] == 3]
    print [e for e in foo if foo[e].bar.far == 7]
    foo.car = {'bay': 789}
    print foo.car.bay