'''
Refer to:
https://github.com/cloudatcost/api
'''

import json
import requests

credentialsDict = eval(open('credentials.txt', 'r').read())
key = credentialsDict['apiKey']
login = credentialsDict['login']

baseURL = "https://panel.cloudatcost.com"

def listServers(apiKey=key, apiLogin=login):
	url = baseURL + "/api/v1/listservers.php?key=%s&login=%s" % (apiKey, apiLogin)
	response = requests.get(url)
	return response
	
def listTemplates(apiKey=key, apiLogin=login):
	url = baseURL + "/api/v1/listtemplates.php?key=%s&login=%s" % (apiKey, apiLogin)
	response = requests.get(url)
	return response

def listTasks(apiKey=key, apiLogin=login):
        url = baseURL + "/api/v1/listtasks.php?key=%s&login=%s" % (apiKey, apiLogin)
        response = requests.get(url)
        return response

def powerOp(apiKey=key, apiLogin=login, sid, action):
	action = action.lower()
	actions = ["poweron","poweroff","reset"]
	if action in actions:
		url = baseURL + "/api/v1/powerop.php?key=%s&login=%s&sid=%s&action=%s" % (apiKey, apiLogin, sid, action)
		response = requests.get(url)
		return response

def runMode(apiKey=key, apiLogin=login, sid, mode):
        mode = mode.lower()
        modes = ["normal", "safe"]
        if mode in modes:
                url = baseURL + "/api/v1/runmode.php?key=%s&login=%s&sid=%s&mode=%s" % (apiKey, apiLogin, sid, mode)
                response = requests.get(url)
                return response

def renameServer(apiKey=key, apiLogin=login, sid, name):
	url = baseURL + "/api/v1/renameserver.php?key=%s&login=%s&sid=%s&name=%s" % (apiKey, apiLogin, sid, name)
	response = requests.get(url)
	return response

def modifyDns(apiKey=key, apiLogin=login, sid, hostname):
        url = baseURL + "/api/v1/rdns.php?key=%s&login=%s&sid=%s&hostname=%s" % (apiKey, apiLogin, sid, hostname)
        response = requests.get(url)
        return response

def serverConsole(apiKey=key, apiLogin=login, sid):
        url = baseURL + "/api/v1/renameserver.php?key=%s&login=%s&sid=%s" % (apiKey, apiLogin, sid)
        response = requests.get(url)
        return response

def buildServer(apiKey=key, apiLogin=login, cpu, ram, storage, os):
	#TODO:
	#input validation

	#cpu must be between 1-16
	#ram must be between 1024 and 32768 and a multiple of 4
	#storage must be between 10 and 1000
	#os mus be a value from listtemplates.php

	url = baseURL + "/api/v1/cloudpro/build.php?key=%s&login=%s&cpu=%s&ram=%s&storage=%s&os=%s" % (apiKey, apiLogin, cpu, ram, storage, os)
	response = requests.get(url)
	return response

def deleteServer(apiKey=key, apiLogin=login, sid):
        url = baseURL + "/api/v1/cloudpro/delete.php?key=%s&login=%s&sid=%s" % (apiKey, apiLogin, sid)
        response = requests.get(url)
        return response

def listResources(apiKey=key, apiLogin=login):
        url = baseURL + "/api/v1/cloudpro/resources.php?key=%s&login=%s" % (apiKey, apiLogin)
        response = requests.get(url)
        return response

