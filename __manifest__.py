# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Kanban View',
    'version': '1.1',
    'website': 'https://www.laoodoo.com',
    'category': 'Project',
    'sequence': 10,
    'summary': 'Project Kanban View',
    'depends': [
        'project',
        'base',
    ],
    'description': "Modern and Useful Infomation in Kanban View",
    'data': [

         'views/project_kanban_view.xml',
        
    ],
    'qweb': [],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
