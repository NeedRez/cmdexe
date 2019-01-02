import cmdexe
choicelist = (('Check > ', ['Ali', 'Brandon', 'Chris', 'Kelly', 'Quinn']),
    ('Approve > ', ['Brad', 'Kelly', 'Quinn']),
    ('Release > ', ['JeRae', 'Richie']))

print cmdexe.nav_userchoices(choicelist)
