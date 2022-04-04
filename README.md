# TyphoonData: Reanalysis Datasets based on Typhoon Best Track data
If you are using this dataset, please cite

>Rui Chen, Xiang Wang, Weimin Zhang, Xiaoyu Zhu, Aiping Li, and Chao Yang. A hybrid CNN-LSTM model for typhoon formation forecasting[J]. Geoinformatica, 2019, 23(3): 375-396.

Download [here](https://www.researchgate.net/profile/Chen-Rui-21/publication/333008232_A_hybrid_CNN-LSTM_model_for_typhoon_formation_forecasting/links/5f16633592851c1eff23c8be/A-hybrid-CNN-LSTM-model-for-typhoon-formation-forecasting.pdf)

## Data Source
https://www.ecmwf.int/en/forecasts/datasets/browse-reanalysis-datasets

## Data Download
This dataset includes 12 RAR packages, and the folder name starts with WP_ means that this folder contains the typhoon data in West Pacific (EP_ are in East Pacific and NA_ are in North Atlantic). The numbers in each folder name represent the first and the last typhoon case in this folder.

[Baidu Pan](https://pan.baidu.com/s/1-emRTY5jC-YvDFtT17A-QQ)  
Password:  rs3j

## Data Description
 
Some cases of West Pacific are shown in the ‘Examples’ folder we provide above. For example, ‘tp_seq1.txt’ is one of the typhoon's best track data downloaded from IBTrACs (International Best Track Archive for Climate Stewardship). There are 516 files from 1979 to 2016 in total, and each file contains all the records starting from formation to extinction of a typhoon, and the time interval is 6 hours. Each record includes the time, longitude, latitude, minimum sea level pressure, and maximum wind speed (intensity) in the center of a typhoon.

<img src="https://github.com/wxnudt/Pictures/blob/main/tp_seq.png" width="300px" alt='tp_seq1.txt'>

The data in the ‘data_seq1’ folder are the ERA-Interim reanalysis data corresponding to the typhoon records in tp_seq1.txt, which are downloaded from ECMWF.
tp_1_pl.nc contains the atmospheric grid variables and tp_1_sf.nc contains the sea surface grid variables surrounding the typhoon center. Their domain size is 20°×20°, and the center of the domain is the longitude and latitude of the typhoon center in the first record of data_seq1.txt. For *_pl.nc, the variables are u (u-direction wind speed), v (v-direction wind speed), r (humidity), t (temperature), z (potential height) at 1000/975/925/850/800/700/600/500/400/300/200/100 hPa pressure levels. For *_sf.nc, the variables are the sea surface temperature. tp_2_pl.nc and tp_2_sf.nc are also the data corresponding to the second record in tp_seq1.txt, as well as others.

<img src="https://github.com/wxnudt/Pictures/blob/main/pl.png" width="600px" alt='tp_1_pl.nc'>

## Supplement

Auto download python script: how to download typhoon data from ECMWF?

```
#!/usr/bin/env python

import cdsapi

for i in range(0, len(BestTrack_data)):
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                'sea_surface_temperature',
            ],
            'year': str(BestTrack_data['year'][i]),
            'month': str(BestTrack_data['month'][i]),
            'day': str(BestTrack_data['date'][i]),
            'time': str(BestTrack_data['hour'][i]),
            'area': [
                BestTrack_data['N'][i]+10, BestTrack_data['W'][i]-10,
                BestTrack_data['S'][i]-10, BestTrack_data['E'][i]+10,
            ],
        },
        output_path+'tp_'+str(i+1) +sf.nc')

```

For instance, according to the first record in tp_seq1.txt, the tropical cyclone was formed at 00:00 on January 2, 1979, the central longitude and latitude were (168.7E, 5.2N). When inputting the time and location of a record into the python script, the program can automatically match the data with a domain size of 20°×20° based on the typhoon center (168.7E, 5.2N) at 00:00 on January 2, 1979. Noticeably, if this center is not located in an ERA-Interim grid, the program will round the center into the grid. Therefore, the whole domain of this typhoon's record is range is from 159-179E in longitude and 5S-15N in latitude.

Since ERA-Interim data does not update now, this program below is a case of ERA5 download script (https://cds.climate.copernicus.eu/api-how-to). There is an option to download the variables referred to ‘variable’ in this script, for example, selecting 'sea_surface_temperature' at the sea surface. Besides, 'year', 'month', 'day', ‘time’ are the location of the time of typhoon record, and ‘area’ is the location of the longitude and latitude of the typhoon's center. A loop is a good way to automatically download all the data of typhoon records.
