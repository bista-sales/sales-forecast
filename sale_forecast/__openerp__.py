# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2012 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'Sale Forecast',
    'category': '',
    'summary': '',
    'version': '1.0',
    'description': """
Provides ability to forecast the quantity for the products and based upon the calculation of action quantity, Purchase Order or Manufacture order can be created.

contribution by : purvesh.parmar@bistasolutions.com

    """,
    'author': '',
    'depends': ['sale', 'stock','crm','procurement_jit','purchase','mrp'],
    'data': [
        'sale_forecast_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
