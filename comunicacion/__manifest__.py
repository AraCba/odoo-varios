# -*- coding: utf-8 -*-
##############################################################################
#
#    Módulo Docentes para Odoo
#    Copyright (C) Araceli Acosta.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
##############################################################################


{
    'name': 'Comunicación',
    'version': '0.1',
    'category': 'Base',
    'summary': """Comunicación""",

    'description': """
Este módulo permite organizar la comunicación con contactos
=========================================================================

---
    """,
    'author': "Araceli Acosta",
    'depends': ['base'],
    'data': [
        'views/contactos_view.xml',
    ],
    'application': True,
}

