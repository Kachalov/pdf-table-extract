#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PDF Table Extraction Utility"""

from .core import process_page, output, table_to_list


__author__ = 'Ian McEwan, Ashima Research'
__copyright__ = (
    'Copyright (C) 2011 Ashima Research. All rights reserved. '
    'Distributed under the MIT Expat License. '
    'See LICENSE file. https://github.com/ashima/pdf-table-extract'
)
__credits__ = ['Ian McEwan', 'Ashima Research', 'Ronald Theodoro']
__license__ = 'MIT Expat'
__version__ = '0.1.1'
__maintainer__ = 'Ronald Theodoro'
__status__ = 'Development'

__all__ = ['process_page', 'output', 'table_to_list']
