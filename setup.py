#!/usr/bin/python
#
# WiiPCRT
# Wii Parental Control (PIN) Reset Tool
#
# Copyright (C) 2018-2021 Sindastra <https://github.com/sindastra/WiiPCRT>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
import py2exe

setup(
console=['reset_tool.py'],
options={'py2exe': {'bundle_files': 1, 'compressed': True, 'optimize': 2}},
zipfile = None
)
