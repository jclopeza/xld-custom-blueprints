# Configuration/Policies
def createPoliciesDirectories():
    policiesDirectory = factory.configurationItem('Configuration/Policies', 'core.Directory')
    # To save the CI in the repository, execute:
    repository.create(policiesDirectory)

def createTutorialPackageRetentionPolicy():
    # Ahora tenemos que añadir estas politicas de retencion de packages.
    # Regular expression that matches the full IDs of packages to which the policy should be applied.
    # For example: '^Applications/.*/\d{1,8}(?:\.\d{1,6})?(?:\.\d{1,6})?(?:-\d+)?$'. (Property: pattern)
    # Specify the daily crontab schedule to execute this policy.
    # The pattern is a list of six fields separated by a single space.
    # The fields represent the second, minute, hour, day, month, and weekday.
    # Example patterns: '0 0 * * * *' = the top of every hour of every day
    # '0 0 14 * * SAT,SUN' = 14 o'clock on each weekend day
    # '0 0 9-17 * * MON-FRI' = on the hour nine-to-five weekdays
    # '0 0 0 1 * *' = every 1st of month at midnight
    policyProperties = {'pattern': '^Applications/Calculator/tutorial/\d{1,3}\.\d{1,3}\.\d{1,3}-B\d{1,3}$', 'packageRetention': '5', 'enabled': 'true', 'schedule': '0 * * * * *', 'dryRun': 'false'}
    tutorialPackageRetentionPolicy = factory.configurationItem('Configuration/Policies/TutorialPackageRetentionPolicy', 'policy.PackageRetentionPolicy', policyProperties)
    repository.create(tutorialPackageRetentionPolicy)
