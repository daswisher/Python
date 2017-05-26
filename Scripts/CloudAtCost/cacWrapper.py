'''
Refer to:
https://github.com/cloudatcost/api
'''

import json
import requests

baseURL = "https://panel.cloudatcost.com"

def listServers(apiKey, apiLogin):
	url = baseURL + "/api/v1/listservers.php?key=%s&login=%s" % (apiKey, apiLogin)
	response = requests.get(url)
	return response
	
def listTemplates(apiKey, apiLogin):
	url = baseURL + "/api/v1/listtemplates.php?key=%s&login=%s" % (apiKey, apiLogin)
	response = requests.get(url)
	return response

def listTasks(apiKey, apiLogin):
        url = baseURL + "/api/v1/listtasks.php?key=%s&login=%s" % (apiKey, apiLogin)
        response = requests.get(url)
        return response

def powerOp(apiKey, apiLogin, sid, action):
	action = action.lower()
	actions = ["poweron","poweroff","reset"]
	if action in actions:
		url = baseURL + "/api/v1/powerop.php" 
		data = {
			'key': apiKey,
			'login': apiLogin,
			'sid': sid,
			'action': action
		}
		response = requests.post(url,data=data)
		return response

def runMode(apiKey, apiLogin, sid, mode):
        mode = mode.lower()
        modes = ["normal", "safe"]
        if mode in modes:
                url = baseURL + "/api/v1/runmode.php"
		data = {
			'key': apiKey,
			'login': apiLogin,
			'sid': sid,
			'mode': mode
		}
		response = requests.post(url,data=data)
                return response

def renameServer(apiKey, apiLogin, sid, name):
	url = baseURL + "/api/v1/renameserver.php"
	data = {
		'key': apiKey,
		'login': apiLogin,
		'sid': sid,
		'name': name
	}
	response = requests.post(url,data=data)
	return response

def modifyDns(apiKey, apiLogin, sid, hostname):
        url = baseURL + "/api/v1/rdns.php"
        data = {
                'key': apiKey,
                'login': apiLogin,
                'sid': sid,
                'hostname': hostname
        }
        response = requests.post(url,data=data)
        return response

def serverConsole(apiKey, apiLogin, sid):
        url = baseURL + "/api/v1/console.php"
        data = {
                'key': apiKey,
                'login': apiLogin,
                'sid': sid,
        }
        response = requests.post(url,data=data)
        return response

def buildServer(apiKey, apiLogin, cpu, ram, storage, os):
	#TODO:
	#input validation

	#cpu must be between 1-16
	#ram must be between 1024 and 32768 and a multiple of 4
	#storage must be between 10 and 1000
	#os mus be a value from listtemplates.php

	url = baseURL + "/api/v1/cloudpro/build.php"
	data = {
		'key': apiKey,
		'login': apiLogin,
		'cpu': cpu,
		'ram': ram,
		'storage': storage,
		'os': os
	}
	response = requests.post(url,data=data)
	return response

def deleteServer(apiKey, apiLogin, sid):
        url = baseURL + "/api/v1/cloudpro/delete.php"
        data = {
                'key': apiKey,
                'login': apiLogin,
                'sid': sid,
        }
        response = requests.post(url,data=data)
        return response

def listResources(apiKey, apiLogin):
        url = baseURL + "/api/v1/cloudpro/resources.php?key=%s&login=%s" % (apiKey, apiLogin)
        response = requests.get(url)
        return response

