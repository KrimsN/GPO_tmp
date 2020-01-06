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

import h5py, os, sys, tarfile

from classes import Point
	
DEBUG = True


def Check():
    pass

def Download(wgetlist: str):
	os.system("wget -i " + wgetlist + " -P gosat/tmp/archives/ --http-user=tarangok@yandex.ru --http-passwd=GPOtusur19 ")

def FromTar(path_to_archives, path_to_extract):
	
	archives_list = os.listdir(path_to_archives)
	
	for archive in archives_list:
		archive = path_to_archives + archive
		tar = tarfile.open(archive, "r")
		tar.extractall(path=path_to_extract)
		tar.close()

		if not DEBUG:
			os.remove(archive)
	return archives_list

def Convert():
	if not os.path.exists("gosat/data"):
		os.makedirs("gosat/data")

	hdf5_l = os.listdir('gosat/tmp/HDF/SWIRL2CO2/')


	for hdf5 in hdf5_l:

		with h5py.File('gosat/tmp/HDF/SWIRL2CO2/' + hdf5, 'r') as f:
			Data = f['Data']
			geolocation = Data['geolocation']
			longitude = geolocation['longitude']
			latitude = geolocation['latitude']
			scanAttribute = f['scanAttribute']
			mixingRatio = Data['mixingRatio']

			timeList = list(scanAttribute['time'])
			# Значение 
			co2_l = list(mixingRatio['XCO2'])
			lon_l = list( longitude )									
			lat_l = list( latitude )
		
		with open(f'gosat/data/{timeList[0].decode("utf-8")[:10]}.json', 'w') as f:
			f.write('[\n')
			for i in range(len(co2_l)):
				f.write(str(Point(lat_l[i], lon_l[i], timeList[i], co2_l[i])))
				if i != len(co2_l)-1:
					f.write(',\n')
			f.write(']')