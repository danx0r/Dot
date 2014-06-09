#
# dict with js-like dot access
#
class Dot(dict):
    convert = True
    def __init__(self, *args, **kw):
        if len(args) and args[0] == False:
            dict.__setattr__(self, 'convert', False)
            args = args[1:]
        dict.__init__(self, *args, **kw)

    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val

    def __setitem__(self, key, val):
        if self.convert and type(val) == dict:
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
#     foo = Dot(False)                            #no dict-->Dot conversion; foo.car.bay will error
    d = {'bay': 1}
    foo.car = d
    d['bay'] += 1
    print foo.car.bay
    d = Dot({'bay': 1})
    foo.car = d
    d['bay'] += 1
    print foo.car.bay
