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

for dataKey in dataSet["used"].keys():
	try:
		dataSet["used"][dataKey] = int(dataSet["used"][dataKey])

	except:
		dataSet["used"][dataKey] = 0

for dataKey in dataSet["total"].keys():
	try:
		dataSet["total"][dataKey] = int(dataSet["total"][dataKey])

	except:
		dataSet["total"][dataKey] = 0

cpus = dataSet['total']['cpu_total'] - dataSet['used']['cpu_used']
rams = dataSet['total']['ram_total'] - dataSet['used']['ram_used']
storages = dataSet['total']['storage_total'] - dataSet['used']['storage_used']

print "cpu:", cpus
print "ram:", rams
print "storage:",storages

cpu = 1
ram = rams/cpus
while ram % 4 != 0:
	ram -= 1

storage = storages/cpus

print
print key
print login
print cpu
print ram
print storage
print templateID

#############################
'''
TODO:
Make the below section loop until all available resources have been consumed
'''
#############################
buildResponse = dispatcher['buildserver'](key, login, cpu, ram, storage, templateID)
while buildResponse.status_code != 200:
	buildResponse = dispatcher['buildserver'](key, login, cpu, ram, storage, templateID)

print buildResponse.url
print buildResponse.text

taskResponse = dispatcher['listtasks'](key, login)
print taskResponse.text
