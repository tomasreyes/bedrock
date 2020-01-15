# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.contribute.events import ContributeEventsPage


@pytest.mark.nondestructive
def test_events_table_is_displayed(base_url, selenium):
    page = ContributeEventsPage(selenium, base_url).open()
    assert page.events_table_is_displayed
