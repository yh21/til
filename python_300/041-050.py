ticker = "btc_krw"
ticker_1 = ticker.upper()
print(ticker_1) #041

ticker_2 = "BTC_KRW"
ticker_3 = ticker_2.lower()
print(ticker_3) #042

print("Hello".capitalize()) #043

file_name = "보고서.xlsx"
print(file_name.endswith("xlsx")) #044

print(file_name.endswith(("xlsx", "xls"))) #045

file_name_1 = "2020_보고서.xlsx"
print(file_name_1.startswith("2020"))