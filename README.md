# TyphoonData:Best Path Record and Reanalysis Data of Typhoon 
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
the data in ‘data_seq1’ folder are the relevant ERA-Interim reanalysis data corresponding to the typhoon record in tp_seq1.txt, which is sourced from ECMWF.     
tp_1_pl.nc is the atmospheric variables at 20°×20° range near the longitude and latitude of the typhoon center when the time is the first record in data_seq1.txt. The variables are u(U-direction wind speed), v(v-direction wind speed), r(humidity), t(temperature), z(potential height) at 1000/975/925/850/800/700/600/500/400/300/200/100 hpa. tp_2_pl.nc is the time of second record in tp_seq1.txt and so on.
tp_1_sf.nc is the sea surface variables at 20°×20° range near the longitude and latitude of the typhoon center when the time is the first record in tp_seq1.txt. The variables are the sst of sea surface. tp_2_sf.nc is the time of second record in tp_seq1.txt and so on.
