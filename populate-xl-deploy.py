# Configuration/pipeline-calculator
def createPipeline():
    pipelineCalculator = factory.configurationItem('Configuration/pipeline-calculator', 'release.DeploymentPipeline', { 'pipeline': ['Environments/Development/calculator-dev', 'Environments/Preproduction/calculator-pre', 'Environments/Production/calculator-pro'] })
    # To save the CI in the repository, execute:
    repository.create(pipelineCalculator)

def associatePipelines():
    # Ahora tenemos que añadir estos pipelines
    ci = repository.read("Applications/Calculator/front")
    ci.pipeline = 'Configuration/pipeline-calculator'
    repository.update(ci)

def createSMTPServer():
    # SMTP Server
    smtpServer = factory.configurationItem('Configuration/smtp-server', 'mail.SmtpServer', {'host': 'localhost', 'port': '1025', 'fromAddress': 'xldeploy@xebialabs.com', 'testAddress': 'josecarlos.lopezayala@gmail.com'})
    repository.create(smtpServer)

def createDirectories():
    # Creación de estructura de directorios para notificaciones
    # Environments
    environmentsDir = factory.configurationItem('Configuration/Environments', 'core.Directory')
    environmentsDevDir = factory.configurationItem('Configuration/Environments/Development', 'core.Directory')
    environmentsDevDirEmailNotifications = factory.configurationItem('Configuration/Environments/Development/EmailNotifications', 'core.Directory')
    environmentsDevDirTriggers = factory.configurationItem('Configuration/Environments/Development/Triggers', 'core.Directory')
    environmentsPreDir = factory.configurationItem('Configuration/Environments/Preproduction', 'core.Directory')
    environmentsPreDirEmailNotifications = factory.configurationItem('Configuration/Environments/Preproduction/EmailNotifications', 'core.Directory')
    environmentsPreDirTriggers = factory.configurationItem('Configuration/Environments/Preproduction/Triggers', 'core.Directory')
    environmentsProDir = factory.configurationItem('Configuration/Environments/Production', 'core.Directory')
    environmentsProDirEmailNotifications = factory.configurationItem('Configuration/Environments/Production/EmailNotifications', 'core.Directory')
    environmentsProDirTriggers = factory.configurationItem('Configuration/Environments/Production/Triggers', 'core.Directory')
    listCIs = [environmentsDir, environmentsDevDir, environmentsPreDir, environmentsProDir, environmentsDevDirEmailNotifications, environmentsDevDirTriggers, environmentsPreDirEmailNotifications, environmentsPreDirTriggers, environmentsProDirEmailNotifications, environmentsProDirTriggers]
    repository.create(listCIs)

def createEmailNotifications():
    # Configuramos las notificaciones por Email
    emailFailedDeploymentDev = factory.configurationItem('Configuration/Environments/Development/EmailNotifications/Email failed deployment', 'trigger.EmailNotification', {'toAddresses': ['devteam@xebialabs.com'], 'subject': 'FAILED! - Application ${deployedApplication.version.application.name} deployment to ${deployedApplication.environment.name} failed', 'sendContentAsHtml': 'true', 'bodyTemplatePath': '/opt/xebialabs/mail-templates/emailFailedDeploymentDev.html', 'mailServer': 'Configuration/smtp-server'})
    emailSuccessfulDeploymentDev = factory.configurationItem('Configuration/Environments/Development/EmailNotifications/Email successful deployment', 'trigger.EmailNotification', {'toAddresses': ['devteam@xebialabs.com'], 'subject': 'SUCCESSFUL! - Application ${deployedApplication.version.application.name} deployment to ${deployedApplication.environment.name} successful', 'sendContentAsHtml': 'true', 'bodyTemplatePath': '/opt/xebialabs/mail-templates/emailSuccessfulDeploymentDev.html', 'mailServer': 'Configuration/smtp-server'})
    repository.create([emailFailedDeploymentDev, emailSuccessfulDeploymentDev])

def createTriggers():
    # Configuramos los triggers
    triggerFailedDeploymentDev = factory.configurationItem('Configuration/Environments/Development/Triggers/Failed deployment trigger', 'trigger.TaskTrigger', {'actions': ['Configuration/Environments/Development/EmailNotifications/Email failed deployment'], 'fromState': 'ANY', 'toState': 'FAILED'})
    triggerSuccessfulDeploymentDev = factory.configurationItem('Configuration/Environments/Development/Triggers/Successful deployment trigger', 'trigger.TaskTrigger', {'actions': ['Configuration/Environments/Development/EmailNotifications/Email successful deployment'], 'fromState': 'ANY', 'toState': 'EXECUTED'})
    repository.create([triggerFailedDeploymentDev, triggerSuccessfulDeploymentDev])

def associateTriggers():
    # Ahora tenemos que añadir estos triggers a los distintos environments
    ci = repository.read("Environments/Development/calculator-dev")
    ci.triggers = ['Configuration/Environments/Development/Triggers/Failed deployment trigger', 'Configuration/Environments/Development/Triggers/Successful deployment trigger']
    repository.update(ci)
    ci = repository.read("Environments/Preproduction/calculator-pre")
    ci.triggers = ['Configuration/Environments/Development/Triggers/Failed deployment trigger', 'Configuration/Environments/Development/Triggers/Successful deployment trigger']
    repository.update(ci)
    ci = repository.read("Environments/Production/calculator-pro")
    ci.triggers = ['Configuration/Environments/Development/Triggers/Failed deployment trigger', 'Configuration/Environments/Development/Triggers/Successful deployment trigger']
    repository.update(ci)

