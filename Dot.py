class Dot(dict):
    def __getattr__(self, attribute):
        return self[attribute]
     
    def __setattr__(self, key, val):
        self[key] = val

    def GE(self, val):
        result = []
        for key in self:
            if self[key] >= val:
                result.append(key)
        return result

if __name__ == "__main__":
    foo = Dot()
    foo['xyz'] = 456
    print foo.xyz
    foo.abc = 123
    print foo['abc']
    print foo
    print "> 200:", foo.GE(200)
    print "> 100:", foo.GE(100)
