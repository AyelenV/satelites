
""" Lee los datos descargados"""
#Busca archivos de URL y depsita en directorio source

#Descomprime archivos .gz

import gzip
import glob
import os.path
import shutil

source_dir = "./dumps/server1"
dest_dir = "./dedupmount"
tmpfile = "/tmp/delete.me"

for src_name in glob.glob(os.path.join(source_dir, '*.gz')):
    base = os.path.basename(src_name)
    dest_name = os.path.join(dest_dir, base[:-3])
    shutil.copyfile(src_name, tmpfile)
    with gzip.open(tmpfile, 'rb') as infile:
        with open(dest_name, 'w') as outfile:
            for line in infile:
                outfile.write(line)


#Creo objeto netCDF a partir del archivo unzip
import netCDF4 as nc
from netCDF4 import Dataset

f=Dataset("./Downloads/ascat_20160101_003000_metopa_47740_eps_o_250_2300_ovw.l2.nc","r")

#Extraigo las variables de locacion y tiempo
lat=f.variables['lat'][:]
lon=f.variables['lon'][:]
time=f.variables['time'][:]

#Extraigo variable a plotear
wspeed=f.variables['wind_speed'][:]

