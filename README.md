it started simply enough... I wanted to combine the features of Python classes and dicts. Javascript objects allow you to mix dot and subscript syntax, like so:

    foo = {}
    foo.abc = 123
    foo['abc']
    > 123

so I created a class called Dot, that does the same:

    foo = Dot()
    foo.abc = 123
    foo['abc']
    >>> 123

then I thought, wouldn't it be cool to add compare operators to return keys whose items met some condition?

    foo = Dot()
    foo.a = 123
    foo.b = 234
    foo.c = 345
    foo.GT(200)
    >>> ['a', 'b']

and wouldn't it also be cool to nest this behavior, so we can search within nested Dots?

    foo = Dot()
    foo.a = Dot(x=1)
    foo.b = Dot(x=2)
    foo.c = Dot(x=3)
    foo
    {'a': {'x': 1}, 'b': {'x': 2}, 'c': {'x': 3}}
    foo.GE.x(2)
    >>> ['b', 'c']

yes, that would be cool!

    foo.OR(LT.x(2), EQ.x(3))
    >>> ['a', 'c']
