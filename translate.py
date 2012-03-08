#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import re
import urllib
import urllib2
import argparse

parser = argparse.ArgumentParser(description = 'Translate text using google translate service.')
parser.add_argument('text')
parser.add_argument('-t', '--html', action='store_true', dest='html', help='display translation in html')
parser.add_argument('-j', '--json', action='store_true', dest='json', help='display translation in raw json')
args = parser.parse_args()

url = "http://translate.google.com/translate_a/t"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.2) Gecko/20100101 Firefox/10.0.2"}
params = urllib.urlencode({
	"client": "t",
	"hl": "en",
	"multires": 1,
	"text": args.text,
	"sl": "en",
	"tl": "ru"
	})
	
request = urllib2.Request(url + "?" + params,None,headers)
response = urllib2.urlopen(request)
js = re.sub(r",\s*(?=,|])",',""',response.read())
data = json.loads(js)
translated = data[0][0][0];

if args.json:
	print data
	sys.exit(0)
elif args.html:
	# generate html
	if len(data) > 1:
		alternatives = data[1]
		translated += '<style>td {padding: 0px 4px !important;}</style>'
		translated += '<br><br><table cellpadding="3" align="center"><tr>'
		for i in range(0,len(alternatives)):
			translated += '<td' + (' style="border-left: 1px solid;"' if i > 0 else '') + '>'
			translated += '<b>' + (alternatives[i][0] or 'Dictionary') +'</b>'
			partOfSpeechAlternatives = alternatives[i][1]
			for j in range(0,len(partOfSpeechAlternatives)):
				translated += '<br>' + partOfSpeechAlternatives[j]
			translated += '</td>'
		translated += '</tr></table>'

print translated.encode('utf-8')
