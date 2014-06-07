####Dot

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

makes some complicated expressions shorter and easier to read:

	if foo[e]['bar']['far'] == foo[e]['bar']['fat']:
	
becomes

	if foo[e].bar.far == foo[e].bar.fat:
