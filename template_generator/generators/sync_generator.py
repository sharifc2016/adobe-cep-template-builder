from os import path


def generate(config):
    ExtensionBundleId = config["ExtensionBundle"]["Id"]
    CepExtensionPath = config["CepExtensionPath"]
    f = open('templates/sync.text').read()
    return f.format(ExtensionBundleId=ExtensionBundleId,
                    CepExtensionPath=path.join(CepExtensionPath, ExtensionBundleId),
                    )
