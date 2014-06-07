class Dot(dict):
    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val

class DotComparator(object):
    def __getattr__(self, attribute):
        print "GE attrib:", attribute
        return DotComparator()

    def __call__(self, *args):
        print "GE call():", args

# def GE(self, val):
#     result = []
#     for key in self:
#         if self[key] >= val:
#             result.append(key)
#     return result

Dot.GE = DotComparator()

if __name__ == "__main__":
    foo = Dot()
    foo['xyz'] = 456
    print foo.xyz
    foo.abc = 123
    print foo['abc']
    foo['def'] = Dot({'bar': 11111})         #foo.def errors due to keyword
    print foo
#     print "> 200:", foo.GE(200)
#     print "> 100:", foo.GE(100)
    print "nested:", foo.GE.bar(11111)