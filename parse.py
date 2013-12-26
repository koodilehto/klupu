# KlupuNG
# Copyright (C) 2013 Koodilehto Osk <http://koodilehto.fi>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import sys

import klupung.ktweb

for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    # Continue if the dir is not a meeting document dir.
    if "htmtxt0.htm" not in filenames:
        continue

    meetingdoc = klupung.ktweb.parse_meetingdoc(dirpath)
    print(meetingdoc)
