"""
tz.py - Phenny Time/Zone Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib, simplejson

def tz(phenny, input):
	try:
		locinput = input.group(2)
		locinput1 = locinput.strip().lower()
		nickdict = dict(locu = 'NSW', bob = 'waterloo,on', munch = 'montreal,qc', vertigo = 'vancouver,wa', nenso = 'vancouver,bc', cetoole = 'redmond,wa', jewice = 'lulea,se', fungi = 'tokyo,jp', pf = 'montreal, qc')
		if locinput1 in nickdict:
			htmlinput = urllib.quote(nickdict[locinput1])
		else:
			htmlinput = urllib.quote(locinput1)
		url2 = 'http://nominatim.openstreetmap.org/search?q=' + htmlinput + '&format=json'
		jsonResponse = simplejson.load(urllib.urlopen(url2))
		lati = jsonResponse[0]['lat']
		longi = jsonResponse[0]['lon']
		loca = jsonResponse[0]['display_name']
		url3 = 'http://api.geonames.org/timezoneJSON?lat=' + lati + '&lng=' + longi + '&username=jinpark'
		jsonResponse1 = simplejson.load(urllib.urlopen(url3))
		if jsonResponse1['dstOffset'] == 0:
			timezone = ''
		elif jsonResponse1['dstOffset'] > 0:
			timezone = '+' + str(jsonResponse1['dstOffset'])
		else:
			timezone = str(jsonResponse1['dstOffset'])
		phennyout = loca + ": " + str(jsonResponse1['time']) + ' UTC' + timezone
		phenny.say(phennyout)
	except:
		phenny.say('Something went wrong')


tz.commands = ['tz']
tz.priority = 'low'