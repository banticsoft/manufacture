# Copyright 2016 Ucamco - Wim Audenaert <wim.audenaert@ucamco.com>
# Copyright 2016-18 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Multi Level MRP',
    'version': '11.0.1.0.0',
    'author': 'Ucamco, '
              'Eficent, '
              'Odoo Community Association (OCA)',
    'summary': 'Adds an MRP Scheduler',
    'website': 'https://github.com/OCA/manufacture',
    'category': 'Manufacturing',
    'depends': [
        'mrp',
        'stock',
        'purchase',
    ],
    'data': [
        'security/multi_level_mrp_security.xml',
        'security/ir.model.access.csv',
        'views/mrp_forecast_view.xml',
        'views/mrp_area_view.xml',
        'views/product_view.xml',
        'views/stock_location_view.xml',
        'views/mrp_product_view.xml',
        'wizards/mrp_inventory_procure_view.xml',
        'views/mrp_inventory_view.xml',
        'wizards/multi_level_mrp_view.xml',
        'views/mrp_menuitem.xml',
        'data/multi_level_mrp_cron.xml',
        'data/mrp_area_data.xml',
    ],
    'demo': [
        'demo/product_category_demo.xml',
        'demo/product_product_demo.xml',
        'demo/res_partner_demo.xml',
        'demo/product_supplierinfo_demo.xml',
        'demo/mrp_bom_demo.xml',
        'demo/initial_on_hand_demo.xml',
    ],
    'installable': True,
    'application': True,
}