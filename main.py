from tracemalloc import start, stop
import numpy as np
import pandas as pd
from pandas_datareader import data as dt

# CLASS
class Saham:

# FUNCTION
    def __init__(self):
        pass

    def collectData(self, kodeSaham, tanggalMulai):  # untuk mencari data harga saham dari tanggal tertentu sampai tanggal saat ini
        stock = dt.DataReader(kodeSaham +'.JK', data_source = 'yahoo', start = tanggalMulai)
        return stock

    def printToCSV(self, kodeSaham, tanggalMulai):   # untuk mencetak data harga saham dengan format .csv
        stock = dt.DataReader(kodeSaham +'.JK', data_source = 'yahoo', start = tanggalMulai)
        stock.to_csv('PrintOut.csv')
        #print('=== print berhasil ===')



    
# OBJECT
saham = Saham()

# EXECUTE



