# Create users
def createUsers():
    security.createUser('mallory', 'mallory')
    security.createUser('carol', 'carol')
    security.createUser('dave', 'dave')
    security.createUser('bob', 'bob')
    security.createUser('alice', 'alice')
    security.createUser('azucena', 'azucena')

def asignRoles():
    security.assignRole('administrators', ['alice'])
    security.assignRole('calculator-deployers', ['carol', 'dave'])
    security.assignRole('senior-deployers', ['bob'])
    security.assignRole('developers', ['mallory'])
    security.assignRole('testing', ['azucena'])

def grantPermissions():
    security.grant('login', 'developers')
    security.grant('login', 'calculator-deployers')
    security.grant('login', 'senior-deployers')
    security.grant('login', 'administrators')
    security.grant('login', 'testing')
    # administrators
    security.grant('read', 'administrators', ['Infrastructure', 'Environments', 'Applications'])
    security.grant('repo#edit', 'administrators', ['Infrastructure', 'Environments', 'Applications'])
    # senior-deployers
    security.grant("import#initial", 'senior-deployers', ['Applications'])
    security.grant("import#upgrade", 'senior-deployers', ['Applications'])
    security.grant("import#remove", 'senior-deployers', ['Applications'])
    security.grant("deploy#initial", 'senior-deployers', ['Environments'])
    security.grant("deploy#upgrade", 'senior-deployers', ['Environments'])
    security.grant("deploy#undeploy", 'senior-deployers', ['Environments'])
    # calculator-deployers
    security.grant("import#initial", 'calculator-deployers', ['Applications'])
    security.grant("import#upgrade", 'calculator-deployers', ['Applications/Calculator'])
    security.grant("import#remove", 'calculator-deployers', ['Applications/Calculator'])
    security.grant("deploy#initial", 'calculator-deployers', ['Environments/Development', 'Environments/Preproduction'])
    security.grant("deploy#upgrade", 'calculator-deployers', ['Environments/Development', 'Environments/Preproduction'])
    security.grant("deploy#undeploy", 'calculator-deployers', ['Environments/Development', 'Environments/Preproduction'])
    # developers
    security.grant('read', 'developers', ['Applications/Calculator'])
    security.grant("import#upgrade", 'developers', ['Applications/Calculator'])
    security.grant("deploy#upgrade", 'developers', ['Environments/Development'])
    # testing
    security.grant('read', 'testing', ['Applications/Calculator'])
    security.grant("deploy#upgrade", 'testing', ['Environments/Preproduction'])

def loadData():
    createUsers()
    asignRoles()
    grantPermissions()
