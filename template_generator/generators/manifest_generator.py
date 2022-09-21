def generate(config):
    ExtensionBundleId = config["ExtensionBundle"]["Id"]
    ExtensionBundleVersion = config["ExtensionBundle"]["Version"]
    ExtensionId = config["Extension"]["Id"]
    ExtensionVersion = config["Extension"]["Version"]
    ExtensionMenu = config["Extension"]["Menu"]
    HostName = config["Host"]["Name"]
    HostVersion = config["Host"]["Version"]
    f = open('templates/manifest.text').read()
    return f.format(ExtensionBundleId=ExtensionBundleId,
                    ExtensionBundleVersion=ExtensionBundleVersion,
                    ExtensionId=ExtensionId,
                    ExtensionVersion=ExtensionVersion,
                    ExtensionMenu=ExtensionMenu,
                    HostName=HostName,
                    HostVersion=HostVersion,
                    )
