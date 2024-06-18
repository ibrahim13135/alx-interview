# from string import Template

# s = Template('Hello , $name')

# print(s.substitute(name='hima'))


# # name1 = 'hima'
# # name2 = 'sondos'

# print('{name2} and {name1}'.format(name1='hima', name2='sondos'))


# ob = {'hima': 43, 'sondos': 134}

# print('hima have {hima:d}, sondos have {sondos:d}'.format(**ob))



for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
