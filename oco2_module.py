"""
Copyright (c) 2018-2019, Pentagon Developments Cooperations
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import os, tarfile, netCDF4
from classes import Point
from pympler.asizeof import asizeof
import numpy as np
import os

DEBUG = False

def human_size(data):
	bytes_count = asizeof(data)
	return f'{bytes_count}b or {bytes_count/8}B or {bytes_count/1024/8:.3f}K or {(bytes_count/1024)/1024/8:.3f}M'


def Download(wgetlist):
	os.system("wget -i " + wgetlist + " -P oco2/tmp/NC4/")



def Convert():
	if not os.path.exists("oco2/data"):
		os.makedirs("oco2/data")

	nc4_l = os.listdir('oco2/tmp/NC4/')
	nc4_l.sort()
	if DEBUG:
		print(nc4_l[:10])


	for nc4 in nc4_l:
		_path = 'oco2/tmp/NC4/' + nc4
		try:
			with netCDF4.Dataset(_path) as f:
				
				lon_l = np.array(f.variables['longitude'] )
				lat_l = np.array(f.variables['latitude'])
				co2_l = np.array(f.variables['xco2'])
				date_l = np.array(f.variables['date'])
				if DEBUG:
					print(f'{type(date_l)}')
					print(f'{date_l[0]}')
					for i in date_l[0]:
						print(f'{i} = {human_size(i)}')
					print(f'size: date_l={human_size(date_l[0])}')
					print(f'size: co2_l={human_size(co2_l[0])}')
					print(f"oco2/data/{date_l[0][0]:4d}-{date_l[0][1]:02d}-{date_l[0][2]:02d}.json")
				

					print(f'file: {nc4}')
					print(f'points: {len(date_l)} {len(lat_l)} {len(lon_l)} {len(co2_l)}')
					print(f'size: lon_l={human_size(lon_l)}')
					print(f'size: lat_l={human_size(lat_l)}')
					print(f'size: co2_l={human_size(co2_l)}')
					print(f'size: date={human_size(date_l)}')

				
				with open(f"oco2/data/{date_l[0][0]:4d}-{date_l[0][1]:02d}-{date_l[0][2]:02d}.json", 'w') as f1:
					print(f"oco2/data/{date_l[0][0]:4d}-{date_l[0][1]:02d}-{date_l[0][2]:02d}.json")
					f1.write("[\n")
					for i in range(len(co2_l)):
						f1.write(str(Point(lat_l[i], lon_l[i], date_l[i][0], co2_l[i])))
						if i != len(co2_l)-1:
							f1.write(',\n')
					f1.write(']')
		except Exception as e:
			print(e)
		finally:
			if not DEBUG:
				print(f'remove {_path}')
				if os.path.isfile(_path):
					os.remove(_path)
				else:    ## Show an error ##
					print("Error: %s file not found" % _path)

		

		 

		
				

