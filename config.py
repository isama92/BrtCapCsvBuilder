from settings import caps_type

# this will be the output file
csv_file = 'result.csv'

# csv headers
csv_fields = ['Country', 'Region/State', 'City', 'Zip/Postal Code From', 'Zip/Postal Code To', 'Weight>', 'Weight<=', 'Shipping Price', 'Shipping Method']

# rates
rates = {
    'standard': [
        {
            'weight_min': '0',
            'weight_max': '1',
            'price': 4.50,
        },
        {
            'weight_min': '1',
            'weight_max': '10',
            'price': 5.9,
        },
        {
            'weight_min': '10',
            'weight_max': '*',
            'price': 0,
        },
    ],
    'priority': [
        {
            'weight_min': '0',
            'weight_max': '1',
            'price': 6,
        },
        {
            'weight_min': '1',
            'weight_max': '10',
            'price': 7.4,
        },
        {
            'weight_min': '10',
            'weight_max': '*',
            'price': 2,
        },
    ],
    'ten': [
        {
            'weight_min': '0',
            'weight_max': '1',
            'price': 7.50,
        },
        {
            'weight_min': '1',
            'weight_max': '10',
            'price': 8.9,
        },
        {
            'weight_min': '10',
            'weight_max': '*',
            'price': 4,
        },
    ],
    'disadvantaged': [
        {
            'weight_min': '0',
            'weight_max': '1',
            'price': 7.50,
        },
        {
            'weight_min': '1',
            'weight_max': '10',
            'price': 8.9,
        },
        {
            'weight_min': '10',
            'weight_max': '*',
            'price': 0,
        },
    ],
    'free_zone': [
        {
            'weight_min': '*',
            'weight_max': '*',
            'price': 40,
        },
    ],
}

# methods
methods = [
    {
        # free zone
        'Method': 'Standard',
        'caps_type': caps_type['ARRAY'],
        'caps_array': [23041, 22061],
        'rates': rates['free_zone'],
    },
    {
        # standard
        'Method': 'Standard',
        'caps_type': caps_type['ALL'],
        'rates': rates['standard'],
    },
    {
        # disadvantaged
        'Method': 'Disagiate e Is. Minori',
        'caps_type': caps_type['FILE'],
        'caps_file': 'disadvantaged.txt',
        'rates': rates['disadvantaged'],
    },
    {
        # priority
        'Method': 'Priority',
        'caps_type': caps_type['ALL'],
        'rates': rates['priority'],
    },
    {
        # 10.30
        'Method': 'Entro le 10.30',
        'caps_type': caps_type['ALL'],
        'rates': rates['ten'],
    },
]
