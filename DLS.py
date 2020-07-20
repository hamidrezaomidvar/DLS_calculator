import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, date


def find_DLS(year):
    soup = BeautifulSoup(open("DLS/"+str(year)+".html"), features="lxml")
    table = soup.find('table', attrs={'class': 'tb-tz zebra tb-hover sep'})
    table_rows = table.find_all('tr')
    df = pd.DataFrame(columns=['Region', 'DLS_start', 'DLS_end'])

    for tr in table_rows:
        if tr.find_all('th'):
            ths = tr.find_all('th')
            tds = tr.find_all('td')
            if len(tds) == 3:
                try:
                    a = tds[1].text.split(', ')[1].split('*')[0]+' '+str(year)
                    month = datetime.strptime(a.split(' ')[1][0:3], '%b').month
                    date_1 = date(year, month, int(a.split(' ')[0]))
                    delta_d_start = date_1-date(year, 1, 1)

                    a = tds[2].text.split(', ')[1].split('*')[0]+' '+str(year)
                    month = datetime.strptime(a.split(' ')[1][0:3], '%b').month
                    date_2 = date(year, month, int(a.split(' ')[0]))
                    delta_d_end = date_2-date(year, 1, 1)

                    df = df.append({'Region': ths[0].text,
                                    'DLS_start': delta_d_start.days+1,
                                    'DLS_end': delta_d_end.days+1
                                    }, ignore_index=True)
                    # print(ths[0].text+'----'+str(delta_d_start.days+1)+'----'+str(delta_d_end.days+1))
                except:
                    pass
    return df


year = 2012
df = find_DLS(year)
print(df[df.Region == 'Sri Lanka'])
