import json

class CLMain():
    def __init__(self):
        self.path = '/usr/local/CyberCP/version.txt'
        #versionInfo = json.loads(open(self.path, 'r').read())
        self.version = '2.1'
        self.build = '1'

        ipFile = "/etc/cyberpanel/machineIP"
        f = open(ipFile)
        ipData = f.read()
        self.ipAddress = ipData.split('\n', 1)[0]

        self.initialMeta = {
            "result": "ok"
        }