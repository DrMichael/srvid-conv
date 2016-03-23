# -*- coding: utf-8 -*-

for line in open("oscam.srvid"):
	
	if line[0] != "#":
		parts = line.split("|")
		# print str(len(parts)) + ' ' + repr(parts)
		if len(parts) > 1:
			caid, svrid = parts[0].strip().split(':')
			prov = parts[1].strip()
			name = parts[2].strip()
		if len(parts) == 5:
			tv = parts[3].strip()
			descr = parts[4].strip()
			print svrid + ':' + caid + '|' + name + '|' + tv + '|' + descr + '|' + prov
		elif len(parts) == 4:
			descr = parts[3].strip()
			print svrid + ':' + caid + '|' + name + '|' + 'TV' + '|' + descr + '|' + prov
		elif len(parts) == 3:
			print svrid + ':' + caid + '|' + name + '|' + 'TV' + '|' + '' + '|' + prov
		else:
			print line.strip()
	else:
		print line.strip()