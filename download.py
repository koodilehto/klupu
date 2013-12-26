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

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import klupung.ktweb

policymaker_url = "http://www3.jkl.fi/paatokset/karltk.htm"

meetingdoc_urls = klupung.ktweb.query_meetingdoc_urls(policymaker_url)

for meetingdoc_url in meetingdoc_urls:
    meetingdoc_dir = klupung.ktweb.download_meetingdoc_dir(meetingdoc_url)
    print(meetingdoc_dir)
