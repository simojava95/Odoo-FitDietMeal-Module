# Copyright 2021-22 Mohammed BOUQS
{
    'name': "FitDietMeal",
    'version': '12.0',
    "category": "sales",
    'author': "Mohammed Bouqs",
    'license': 'AGPL-3',
    'summary': """Diet meals planing app.""",
    'depends': ['product', 'sale', 'base'
                ],
    'data': [
        'views/dietfacts.xml',
        'security/ir.model.access.csv'

    ],
    'installable': True,
    'application': True,
    'images': ['static/description/icon.png'],
}
