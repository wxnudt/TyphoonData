#!/usr/bin/env python

import cdsapi
import data_temp

input_path = '/Users/cr/Research/2020/data/'
output_path = '/Users/cr/Research/2020/data/EC_data/'

BestTrack_data = data_temp.BTdata_processing(input_path + 'bwp262018.dat')

for i in range(0, len(BestTrack_data)):
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                '10m_u_component_of_wind', '10m_v_component_of_wind',
            ],
            'year': str(BestTrack_data['year'][i]),
            'month': str(BestTrack_data['month'][i]),
            'day': str(BestTrack_data['date'][i]),
            'time': str(BestTrack_data['hour'][i]),
            'area': [
                BestTrack_data['N'][i], BestTrack_data['W'][i],
                BestTrack_data['S'][i], BestTrack_data['E'][i],
            ],
        },
        output_path+'EC_Mangkhut_'+str(i+1) +'.nc')

