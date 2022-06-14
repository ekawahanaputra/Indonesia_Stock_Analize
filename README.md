# Indonesia_Stock_Analize
Program opensource untuk menganalisa saham Indonesia.
Kami terbuka dan mengundang siapapun untuk mengembangkan program ini.

# Tool & Equiqment
- python 3.9.2
- pandas 1.4.2
- pandas_datareader 0.10.0

# Documentation
### class Saham
  - **collectData** berfungsi untuk mengambil data harga saham selama periode yang dipilih. 
    **Format :**```collectData(kode saham, tanggal)```. Untuk parameter tanggal gunakan format ```yyyy-m-d```. Parameter tanggal disini mengacu pada
    tanggal dimulainya proses pengambilan data. Dan secara otomatis data yang diambil adalah hingga data harga saham terakhir.
  - **printToCSV** berfungsi untuk mencetak data harga saham selama periode terpilih dengan format ```PrintOut.csv```. 
    **Format :** ```printToCSV(kode saham, tanggal)```. Untuk parameter tanggal gunakan format ```yyyy-m-d```. Parameter tanggal disini mengacu pada
    tanggal dimulainya proses pengambilan data. Dan secara otomatis data yang diambil adalah hingga data harga saham terakhir.
