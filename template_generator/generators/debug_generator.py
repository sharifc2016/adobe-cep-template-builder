def generate(config):
    ExtensionId = config["Extension"]["Id"]
    HostName = config["Host"]["Name"]
    HostDebug = config["Host"]["Debug"]
    f = open('templates/debug.text').read()
    return f.format(ExtensionId=ExtensionId,
                    HostName=HostName,
                    HostDebug=HostDebug,
                    )
