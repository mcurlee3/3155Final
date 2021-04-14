import pandas as pd

df_main = pd.read_csv("Data - General Data.csv")
cHappiness = df_main.sort_values(by='Happiness Value', ascending=False)
cGDP = df_main.sort_values(by='Logged GDP per capita', ascending=False)
cSocialSupport = df_main.sort_values(by='Social support', ascending=False)
cHLExpectancy = df_main.sort_values(by='Healthy life expectancy', ascending=False)
cFreedom = df_main.sort_values(by='Freedom to make life choices', ascending=False)
cGenerosity = df_main.sort_values(by='Generosity', ascending=False)
cCorruption = df_main.sort_values(by='Perceptions of corruption', ascending=False)
cHGDP = df_main.sort_values(by='Happiness/GDP', ascending=False)
cHLife = df_main.sort_values(by='Happiness/Life Expetancy', ascending=False)
cHSocSup = df_main.sort_values(by='Happiness/Social Support', ascending=False)
cHFreedom = df_main.sort_values(by='Happiness/Freedom', ascending=False)
cHGenerosity = df_main.sort_values(by='Happiness/Generosity', ascending=False)
cHCorruption = df_main.sort_values(by='Happiness/Corruption', ascending=False)
cHDystopia = df_main.sort_values(by='Happiness/Dystopia', ascending=False)

file = open('cHappiness.csv', 'w')
file.write(cHappiness.to_csv())
file.close()
file = open('cGDP.csv', 'w')
file.write(cGDP.to_csv())
file.close()
file = open('cSocialSupport.csv', 'w')
file.write(cSocialSupport.to_csv())
file.close()
file = open('cHLExpectancy.csv', 'w')
file.write(cHLExpectancy.to_csv())
file.close()
file = open('cFreedom.csv', 'w')
file.write(cFreedom.to_csv())
file.close()
file = open('cGenerosity.csv', 'w')
file.write(cGenerosity.to_csv())
file.close()
file = open('cCorruption.csv', 'w')
file.write(cCorruption.to_csv())
file.close()
file = open('cHGDP.csv', 'w')
file.write(cHGDP.to_csv())
file.close()
file = open('cHLife.csv', 'w')
file.write(cHLife.to_csv())
file.close()
file = open('cHSocSup.csv', 'w')
file.write(cHSocSup.to_csv())
file.close()
file = open('cHFreedom.csv', 'w')
file.write(cHFreedom.to_csv())
file.close()
file = open('cHGenerosity.csv', 'w')
file.write(cHGenerosity.to_csv())
file.close()
file = open('cHCorruption.csv', 'w')
file.write(cHCorruption.to_csv())
file.close()
file = open('cHDystopia.csv', 'w')
file.write(cHDystopia.to_csv())
file.close()
