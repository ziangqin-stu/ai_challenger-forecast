from netCDF4 import Dataset

a = Dataset('.\\data\\ai_challenger_wf2018_trainingset_20150301-20180531.nc', 'r')

keys = a.variables.keys()

foretimes = a.variables['foretimes'][:]
station = a.variables['station'][:]
date = a.variables['date'][:]
psfc_M = a.variables['psfc_M'][:]


print(keys)
print(foretimes)
print(psfc_M.shape)
print(psfc_M[1][1][1])
