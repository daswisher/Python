import json

from cacWrapper import *
credentialsDict = eval(open('credentials.txt', 'r').read())
key = credentialsDict['apiKey']
login = credentialsDict['login']

baseURL = "https://panel.cloudatcost.com"

dispatcher = {
	'listservers': listServers,
	'listtemplates': listTemplates,
	'listtasks': listTasks,
	'powerop': powerOp,
	'runmode': runMode,
	'renameserver': renameServer,
	'modifydns': modifyDns,
	'serverconsole': serverConsole,
	'buildserver': buildServer,
	'deleteserver': deleteServer,
	'listresources': listResources
}

print dispatcher['listresources'](key, login)
