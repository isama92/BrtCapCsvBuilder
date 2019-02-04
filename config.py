from settings import destinations_type

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
        'destinations_type': destinations_type['ARRAY'],
        'destinations_array': [
            {
                'cap': '22061',
                'city': 'CAMPIONE D\'ITALIA',
            },
            {
                'cap': '23041',
                'city': 'LIVIGNO',
            }
        ],
        'rates': rates['free_zone'],
    },
    {
        # standard
        'Method': 'Standard',
        'destinations_type': destinations_type['ALL'],
        'rates': rates['standard'],
    },
    {
        # disadvantaged
        'Method': 'Disagiate e Isole Minori',
        'destinations_type': destinations_type['FILE'],
        'destinations_file': 'disadvantaged.txt',
        'regex': r'(?=\d).*?(?=\()',
        'rates': rates['disadvantaged'],
    },
    {
        # priority
        'Method': 'Priority',
        'destinations_type': destinations_type['ALL'],
        'rates': rates['priority'],
    },
    # {
    #     # 10.30
    #     'Method': 'Entro le 10.30',
    #     'destinations_type': destinations_type['ALL'],
    #     'rates': rates['ten'],
    # },
]
