{
    'name' : 'Puerto application',
    'version' : '1.0',
    'summary': 'Puerto',
    'sequence': 1,
    'description': """
        Puerto transit v1.0
    """,
    'category': 'Puerto',
    'depends': ['base', 'mail'],
    'data': [
             'security/ir.model.access.csv',
             'views/folders_view.xml',
             'views/menu.xml',
             'views/folders_form_view.xml',
             'views/folders_tree_view.xml',
             'views/folders_search_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
