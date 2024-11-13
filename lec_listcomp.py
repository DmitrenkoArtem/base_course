symbols='gol'
symbol_codes=[ord(symbol) for symbol in symbols]
print(symbol_codes)
symbol_codes=(ord(symbol) for symbol in symbols) #генератор
print(symbol_codes)