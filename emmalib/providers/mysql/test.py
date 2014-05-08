# -*- coding: utf-8 -*-
# emma
#
# Copyright (C) 2006 Florian Schmidt (flo@fastflo.de)
#               2014 Nickolay Karnaukhov (mr.electronick@gmail.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA	 02110-1301 USA

from MySqlHost import MySqlHost

host = MySqlHost(None, None, 'Localhost', 'localhost', 3306, 'root', 'root', '', 0)
host.connect()
host.use_db('bohprod')

host.databases['bohprod'].refresh()
host.databases['bohprod'].tables['boh_users'].refresh()

table = host.databases['bohprod'].tables['boh_users']
print "---------------------------"
print "Table:"
for p in table.__dict__:
    print p

print "---------------------------"
print "Table fields:"
for f in table.fields:
    print f.__dict__

print "---------------------------"
print "Table indexes:"
for i in table.indexes:
    print i.__dict__