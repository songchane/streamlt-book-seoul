# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:11:06 2024

@author: 213
"""

import requests
import json
import pandas as pd

API_KEY = '4d6b43495864736537377145565341'


def main() :
    data = pd.DataFrame()
    for i in range(1, 21):

        # 'tbLnOpendataRtmsV'' 데이터세트의 최근 1000*11 데이터 요청
        url = f'http://openapi.seoul.go.kr:8088/{API_KEY}/json/tbLnOpendataRtmsV/{1+((i-1)*1000)}/{i*1000}'
        print(url)
        req = requests.get(url)
        content = req.json()
        con = content['tbLnOpendataRtmsV']['row']
        result = pd.DataFrame(con)
        data = pd.concat([data, result])
    data = data.reset_index(drop=True)
    data['DEAL_YMD'] = pd.to_datetime(data['DEAL_YMD'], format=("%Y%m%d"))
    data.to_csv('seoul_real_estate.csv', index=False)
    
    print(data.head())
    print(len(data), type(data))

if __name__ == "__main__":
    main()