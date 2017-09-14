# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IzdvajanjeIvica
                                 A QGIS plugin
 Izdvajanje ivica
                             -------------------
        begin                : 2017-09-07
        copyright            : (C) 2017 by Mirko Milanovic
        email                : milanovic_mirko@ymail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load IzdvajanjeIvica class from file IzdvajanjeIvica.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .izdvajanje_ivica import IzdvajanjeIvica
    return IzdvajanjeIvica(iface)
