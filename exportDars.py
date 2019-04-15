def exportDars(versions):
    for v in versions:
        print("Exportando la aplicacion " + str(v))
        repository.exportDar('/home/jcla/Projects/xld-custom-blueprints/dars', v)

exportDars(repository.search('udm.DeploymentPackage', 'Applications/Calculator/front'))
exportDars(repository.search('udm.DeploymentPackage', 'Applications/Calculator/webservices'))
exportDars(repository.search('udm.DeploymentPackage', 'Applications/Calculator/tutorial'))
