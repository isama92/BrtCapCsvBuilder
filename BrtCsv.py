from os.path import isfile
import config
import re
import csv


class BrtCsv():
    def __init__(self):
        self.tot_rows = 0
        self.csv_rows = []

    @staticmethod
    def get_destinations_from_file(file):
        destinations = []
        if isfile(file):
            with open(file, 'r') as fh:
                content = fh.read()
            destinations = re.findall(r'(?=\d).*?(?=\()', content)
            for i in range(0, len(destinations)):
                d = destinations[i].replace('*', ' ')
                d = d.split(' ', 1)
                destinations[i] = {
                    'cap': d[0],
                    'city': d[1],
                }
            print('Destination from file %s: %d lines | %d cities' % (file, content.count('\n'), len(destinations)))
        else:
            print('File %s not found' % file)
        return destinations

    def get_method_destinations(self, method):
        destinations = []
        if method['destinations_type'] == config.destinations_type['ALL']:
            destinations = [{
                'cap': '*',
                'city': '*',
            }]
        elif method['destinations_type'] == config.destinations_type['ARRAY']:
            destinations = method['destinations_array']
        elif method['destinations_type'] == config.destinations_type['FILE']:
            destinations = BrtCsv.get_destinations_from_file(method['destinations_file'])
        return destinations

    def build_method_rows(self, method, rates, destinations, extra=0):
        for rate in rates:
            for destination in destinations:
                self.csv_rows.append({
                    'Country': 'ITA',
                    'Region/State': '*',
                    'City': destination['city'],
                    'Zip/Postal Code From': destination['cap'],
                    'Zip/Postal Code To': destination['cap'],
                    'Weight>': rate['weight_min'],
                    'Weight<=': rate['weight_max'],
                    'Shipping Price': rate['price'] + extra,
                    'Shipping Method': method,
                })
                self.tot_rows = self.tot_rows + 1

    def build_rows(self):
        for method in config.methods:
            destinations = self.get_method_destinations(method)
            self.build_method_rows(method['Method'], method['rates'], destinations)

    def build_csv(self):
        tot = 0
        print('Writing CSV...')
        with open(config.csv_file, 'w') as fh:
            writer = csv.DictWriter(fh, fieldnames=config.csv_fields, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in self.csv_rows:
                writer.writerow(row)
                tot = tot + 1
        if tot == len(self.csv_rows) and tot == self.tot_rows:
            print('CSV written successfully (%d rows)' % len(self.csv_rows))
        else:
            print('Error while writing CSV file')
