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

templatesResponse = dispatcher['listtemplates'](key, login)
while templatesResponse.status_code != 200:
	templatesResponse = dispatcher['listtemplates'](key, login)

templates = json.loads(templatesResponse.text)['data']

templateID = ''
templateName = ''

for template in templates:
	if 'ubuntu' in template['name'].lower():
		templateID = str(template['ce_id'])
		templateName = str(template['name'])
		break

if templateID == '':
	print "Unable to retrieve Ubuntu template..."
	exit(1)

response = dispatcher['listresources'](key, login)
while response.status_code != 200:
	response = dispatcher['listresources'](key, login)

response = json.loads(response.text)
dataSet = response['data']

for key in dataSet["used"].keys():
	try:
		dataSet["used"][key] = int(dataSet["used"][key])

	except:
		dataSet["used"][key] = 0

for key in dataSet["total"].keys():
	try:
		dataSet["total"][key] = int(dataSet["total"][key])

	except:
		dataSet["total"][key] = 0
cpus = dataSet['total']['cpu_total'] - dataSet['used']['cpu_used']
rams = dataSet['total']['ram_total'] - dataSet['used']['ram_used']
storages = dataSet['total']['storage_total'] - dataSet['used']['storage_used']

print "cpu:", cpus
print "ram:", rams
print "storage:",storages

cpu = 1
ram = rams/cpus
storage = storages/cpus

print cpu
print ram
print storage

