table = {
    'Python':'Guido van Rossum',
    'Perl':'Larry Wall',
    'Tcl':'John Ous'
}
language = 'Python'
creator = table[language]
print(creator)

for c in table:
    print(c, '\t',table[c])
print()