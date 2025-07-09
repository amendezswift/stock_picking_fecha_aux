{
    'name': 'Stock Picking - Fecha Entrega Auxiliar',
    'version': '17.0.1.0',
    'summary': 'Campo auxiliar para filtrar por fecha sin hora en stock.picking',
    'depends': ['stock'],
    'author': '',
    'category': 'Warehouse',
    'description': 'Agrega un campo Date basado en scheduled_date para facilitar búsquedas por fecha en traslados.',
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
