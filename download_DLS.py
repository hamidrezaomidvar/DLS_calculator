#%%
from urllib.request import urlopen

url = 'https://www.timeanddate.com/time/dst/'


for year in range(1970,2020):
    response = urlopen(url+str(year)+'.html')
    webContent = response.read()
    f = open('DLS/'+str(year)+'.html', 'wb')
    f.write(webContent)
    f.close

#%%