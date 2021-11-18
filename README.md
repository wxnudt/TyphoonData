# TyphoonData:Best track Record and Reanalysis Data of Typhoon 
If you are using this dataset please cite

>Rui Chen, Xiang Wang, Weimin Zhang, Xiaoyu Zhu, Aiping Li, and Chao Yang. A hybrid CNN-LSTM model for typhoon formation forecasting[J]. Geoinformatica, 2019, 23(3): 375-396.

Download [here](https://www.researchgate.net/profile/Chen-Rui-21/publication/333008232_A_hybrid_CNN-LSTM_model_for_typhoon_formation_forecasting/links/5f16633592851c1eff23c8be/A-hybrid-CNN-LSTM-model-for-typhoon-formation-forecasting.pdf)

## Data Source
https://www.ecmwf.int/en/forecasts/datasets/browse-reanalysis-datasets

## Download the data
The whole Dataset includes 12 rAR files, whose names start with WP_ from West Pacific, EP_ from East Pacific, NA_ from North Atlantic. The numbers in filename are the first and the last typhoon order number in this file.  

[Baidu Pan](https://pan.baidu.com/s/1-emRTY5jC-YvDFtT17A-QQ)  
Password:  rs3j

## Data Description
 
Some sample data of West Pacific are put in ‘WP_solo’ folder. Take it for example , ‘tp_seq1.txt’ is the best path record data from IBTrACs between 1979 and 2016. A text file is a typhoon record and there are all 516 files. Each text file contains records of all times from the formation to the extinction of the typhoon. The records of each time include the date, time, longitude, latitude, minimum pressure in the center and maximum wind speed (intensity) in the center.

<img src="https://github.com/wxnudt/Pictures/blob/main/tp_seq.png" width="300px" alt='tp_seq1.txt'>


the data in ‘data_seq1’ folder are the relevant ERA-Interim reanalysis data corresponding to the typhoon record in tp_seq1.txt, which is sourced from ECMWF.     
tp_1_pl.nc is the atmospheric variables at 20°×20° range near the longitude and latitude of the typhoon center when the time is the first record in data_seq1.txt. The variables are u(U-direction wind speed), v(v-direction wind speed), r(humidity), t(temperature), z(potential height) at 1000/975/925/850/800/700/600/500/400/300/200/100 hpa. tp_2_pl.nc is the time of second record in tp_seq1.txt and so on.

<img src="https://github.com/wxnudt/Pictures/blob/main/pl.png" width="600px" alt='tp_1_pl.nc'>

<img src="https://github.com/wxnudt/Pictures/blob/main/pl1.png" width="250px" alt='tp_1_pl.nc'><img src="https://github.com/wxnudt/Pictures/blob/main/pl11.png" width="250px" alt='tp_1_pl.nc'>

<img src="https://github.com/wxnudt/Pictures/blob/main/pl2.png" width="250px" alt='tp_1_p1.nc'><img src="https://github.com/wxnudt/Pictures/blob/main/pl21.png" width="250px" alt='tp_1_pl.nc'>

According to the first record in tp_seq1.txt, the tropical cyclone was born at 00:00 on January 2, 1979, the central longitude and latitude were (168.7E, 5.2N), the minimum sea level pressure in the center was 990hpa, and the maximum wind speed was 50kt.  


So the script `ec_mangkhut.py` automatically matches the data within the surrounding  20°×20° range according to (168.7E, 5.2N) (specifically, it would be matched after rounding). The whole data longitude range is from 159-179E and latitude is 5S-15N. 


tp_1_sf.nc is the sea surface variables at 20°×20° range near the longitude and latitude of the typhoon center when the time is the first record in tp_seq1.txt. The variables are the sst of sea surface. tp_2_sf.nc is the time of second record in tp_seq1.txt and so on.  


EP_solo、NA_solo folder are all the same.
