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

import os
import sys

import klupung
import klupung.ktweb
import klupung.models

app = klupung.create_app("sqlite:////tmp/klupung.db")
app.test_request_context().push()

for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    # Continue if the dir is not a meeting document dir.
    if "htmtxt0.htm" not in filenames:
        continue

    meetingdoc = klupung.ktweb.parse_meetingdoc(dirpath)
    policymaker_abbrev = meetingdoc["policymaker_abbreviation"]
    policymaker = klupung.models.Policymaker.query.filter_by(
        abbreviation=policymaker_abbrev).first()
    if policymaker is None:
        policymaker = klupung.models.Policymaker(policymaker_abbrev)
        klupung.db.session.add(policymaker)
        klupung.db.session.commit()

    meeting_start_datetime, _ = meetingdoc["meeting_datetimes"][0]
    meeting = klupung.models.Meeting.query.filter_by(
        policymaker_id=policymaker.id,
        start_datetime=meeting_start_datetime).first()
    if meeting is None:
        meeting = klupung.models.Meeting(meeting_start_datetime,
                                         policymaker.id)
        klupung.db.session.add(meeting)
        klupung.db.session.commit()

    meeting_document = klupung.models.MeetingDocument.query.filter_by(
        origin_id=meetingdoc["origin_id"]).first()
    if meeting_document is None:

        meeting_document = klupung.models.MeetingDocument(
            meetingdoc["origin_url"],
            meeting.id,
            meetingdoc["origin_id"])
        klupung.db.session.add(meeting_document)
        klupung.db.session.commit()
