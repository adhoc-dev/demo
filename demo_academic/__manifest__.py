##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Demo Academic',
    'version': "16.0.1.0.0",
    'category': 'Tools',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'demo_base',
        # Módulos que se instalan mediante productos en nube, si vendemos estos productos se auto instalan estos módulos.
        # como por ahora runbot ni las bases demo, implementan esta logica de auto instalar en funcion de productos,
        # hicimos una análisis manual de que “productos” que consideramos importantes para retail y
        # agregamos como dependencia el modulo que instala dicho producto.

        # Sitio web / Eventos:
        'event',
        # Servicios / Proyecto:
        'project',
        # Servicios / Suscripciones:
        'sale_subscription',
        'academic',

        # A este listado sumamos sumamos los módulos que comercial nos pide agregar y que no se auto instalarían por productos.
        # Si eventualmente implementamos logica de instalacion mediante productos la sección de arriba deberia poder borrarse.
        'event_sale',

    ],
    'data': [
    ],
    'demo': [
        'companies_data.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
