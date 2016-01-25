__author__ = 'tongshan'


a= """b = %(value)s"""

c = 10
a%dict(value=c)
