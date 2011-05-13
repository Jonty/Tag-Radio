#!/usr/bin/python

#  readtag.py - read all sectors from a standard tag
# 
#  Adam Laurie <adam@algroup.co.uk>
#  http://rfidiot.org/
# 
#  This code is copyright (c) Adam Laurie, 2006, All rights reserved.
#  For non-commercial use only, the following terms apply - for all other
#  uses, please contact the author:
#
#    This code is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#


import RFIDIOtconfig
import sys
import os

try:
        card= RFIDIOtconfig.card
except:
        os._exit(True)

card.info('readtag v0.1d')
card.select()
print '\nID: ' + card.uid
print '  Data:'

card.select()
for x in range(255):
	print '    Block %02x:' % x,
	if card.readblock(x):
		print card.data,
		print card.ReadablePrint(card.ToBinary(card.data))
	else:
		print 'read error: %s' % card.errorcode

print '\n    Total blocks: ',
print x
if x > 0:
	os._exit(False)
else:
	os._exit(True)
