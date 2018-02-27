import osa
import math


def temp_avg(filename):

    all_temps = []
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')

    with open(filename) as f:
        for line in f:
            next_temp = line.strip().split(' ')[0]
            celsius_temp = client.service.ConvertTemp(next_temp, 'degreeFahrenheit', 'degreeCelsius')
            all_temps.append(celsius_temp)

    return sum(all_temps)/len(all_temps)


def total_rub(filename):

    total_cash = []
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')

    with open(filename) as f:
        for line in f:
            amount = line.strip().split(' ')[1]
            currency = line.strip().split(' ')[2]
            rub = client.service.ConvertToNum('', currency, 'RUB', amount, '', '', '')
            total_cash.append(rub)

    return math.ceil(sum(total_cash))


def total_km(filename):

    all_lengths = []
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')

    with open(filename) as f:
        for line in f:
            next_trip = line.strip().split(' ')[1].replace(',', '')
            km = client.service.ChangeLengthUnit(next_trip, 'Miles', 'Kilometers')
            all_lengths.append(km)

    return sum(all_lengths)


print("Средняя за неделю арифметическую температуру по Цельсию: {:.2f}".format(temp_avg('temps.txt')))
print("Сколько вы потратите на путешествие денег в рублях: {:.2f}".format(total_rub('currencies.txt')))
print("Суммарное расстояние пути в километрах с точностью до сотых: {:.2f}".format(total_km('travel.txt')))
