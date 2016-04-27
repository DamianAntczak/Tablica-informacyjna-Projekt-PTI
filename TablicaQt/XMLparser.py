#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from xml.dom import minidom

class XMLparser:
	DOMTree = minidom.parse('test.xml')
	s = '';
	widgetList = []
	
	cNodes = DOMTree.childNodes
	for i in cNodes[0].getElementsByTagName("widget"):
		# nazwa taga
		#print i.getElementsByTagName("WeathercastWidget")[0].nodeName
		# wartosc taga
		#print i.getElementsByTagName("imie")[0].childNodes[0].toxml()
		# dostep do atrybutu
		#print i.getElementsByTagName("WeathercastWidget")[0].getAttribute("x")
		#print i.getElementsByTagName("WeathercastWidget")[0].getAttribute("y")
		
		if not i.getAttribute("extra"):
			s = i.getAttribute("name")+'(self,'+i.getAttribute("x")+','+i.getAttribute("y")+')'
		else:
			s = i.getAttribute("name")+'(self,'+i.getAttribute("x")+','+i.getAttribute("y")+','+i.getAttribute("extra")+')'
			print s
		widgetList.append(s)
