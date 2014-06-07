class Dot(dict):
    pass
    def __getattribute__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        print "set", key, val
        self[key] = val
#     def __getitem__(self, item):
#         return self.__dict__[item]

if __name__ == "__main__":
    foo = Dot()
    foo['xyz'] = 456
    print foo.xyz
    foo.abc = 123
    print foo['abc']
    print foo