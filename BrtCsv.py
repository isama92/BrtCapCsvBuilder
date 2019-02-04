from os.path import isfile
import config
import re
import csv


class BrtCsv():
    def __init__(self):
        self.tot_rows = 0
        self.csv_rows = []

    @staticmethod
    def get_caps_from_file(file):
        caps = []
        if isfile(file):
            with open(file, 'r') as fh:
                content = fh.read()
            caps = re.findall(r'(\d{5})', content)
            caps = list(set(caps))
            print('Caps from file %s: %d lines | %d caps (Note: there might be a lot of duplicates)' % (file, content.count('\n'), len(caps)))
        else:
            print('File %s not found' % file)
        return caps

    def get_method_caps(self, method):
        caps = []
        if method['caps_type'] == config.caps_type['ALL']:
            caps = ['*']
        elif method['caps_type'] == config.caps_type['ARRAY']:
            caps = method['caps_array']
        elif method['caps_type'] == config.caps_type['FILE']:
            caps = BrtCsv.get_caps_from_file(method['caps_file'])
        return caps

    def build_method_rows(self, method, rates, caps, extra=0):
        for rate in rates:
            for cap in caps:
                self.csv_rows.append({
                    'Country': 'ITA',
                    'Region/State': '*',
                    'City': '*',
                    'Zip/Postal Code From': cap,
                    'Zip/Postal Code To': cap,
                    'Weight>': rate['weight_min'],
                    'Weight<=': rate['weight_max'],
                    'Shipping Price': rate['price'] + extra,
                    'Shipping Method': method,
                })
                self.tot_rows = self.tot_rows + 1

    def build_rows(self):
        for method in config.methods:
            caps = self.get_method_caps(method)
            self.build_method_rows(method['Method'], method['rates'], caps)

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
