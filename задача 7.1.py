import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

def lists_update(rates_list):

    rates = [float(str(rates_list[i-1])[4: -5]) for i in range(len(rates_list)-1, 3, -3)]
    dates = [str(rates_list[i-2])[6: -5] for i in range(len(rates_list)-1, 3, -3)]

    return dates, rates


url = 'https://mfd.ru/currency/?currency=USD'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

for usd in soup.find_all('table', {'class' : 'mfd-table mfd-currency-table'}):
    print(usd.text)

rates_list = usd.find_all('td')
dates, rates = lists_update(rates_list)
print(dates,rates)
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(4))
ax.grid(True)

ax.plot(dates, rates)

plt.show()