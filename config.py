from rates import *
from settings import caps_type

# this will be the output file
csv_file = 'result.csv'
# csv headers
csv_fields = ['Country', 'Region/State', 'City', 'Zip/Postal Code From', 'Zip/Postal Code To', 'Weight>', 'Weight<=', 'Shipping Price', 'Shipping Method']
# methods
methods = [
    {
        # free zone
        'Method': 'Standard',
        'caps_type': caps_type['ARRAY'],
        'caps_array': [23041, 22061],
        'rates': free_zone_rates,
    },
    {
        # standard
        'Method': 'Standard',
        'caps_type': caps_type['ALL'],
        'rates': standard_rates,
    },
    {
        # disadvantaged
        'Method': 'Disagiate e Is. Minori',
        'caps_type': caps_type['FILE'],
        'caps_file': 'disadvantaged.txt',
        'rates': disadvantaged_rates,
    },
    {
        # priority
        'Method': 'Priority',
        'caps_type': caps_type['ALL'],
        'rates': priority_rates,
    },
    {
        # 10.30
        'Method': 'Entro le 10.30',
        'caps_type': caps_type['ALL'],
        'rates': ten_rates,
    },
]
