# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from unittest.mock import patch

from django.conf import settings
from django.test import RequestFactory

import pytest

from bedrock.firefox.redirects import mobile_app, validate_param_value


@pytest.mark.parametrize(
    "test_param, is_valid",
    (
        ("firefox-whatsnew", True),
        ("firefox-welcome-4", True),
        ("firefox-welcome-6", True),
        ("firefox-welcome-17-en", True),
        ("firefox-welcome-17-de", True),
        ("firefox-welcome-17-fr", True),
        ("firefox-browsers-mobile-get-app", True),
        ("firefox-browsers-mobile-focus", True),
        ("mzaonboardingemail-de", True),
        ("mzaonboardingemail-fr", True),
        ("mzaonboardingemail-es", True),
        ("firefox-all", True),
        ("fxshare1", True),
        ("fxshare2", True),
        ("fxshare3", True),
        ("fxshare4", True),
        ("fxshare12", True),
        ("fxshare14", True),
        ("fxshare15", True),
        ("DESKTOP_FEATURE_CALLOUT_SIGNED_INTO_ACCOUNT.treatment_a", True),
        ("DESKTOP_FEATURE_CALLOUT_SIGNED_INTO_ACCOUNT.treatment_b", True),
        ("wnp134-de-a", True),
        ("wnp134-de-b", True),
        ("wnp134-de-c", True),
        ("wnp134-en-ca-a", True),
        ("wnp134-en-ca-b", True),
        ("smi-marvintsp", True),
        ("smi-koschtaaa", True),
        ("smi-bytereview", True),
        ("pocket-test", True),
        ("some<nefarious$thing", False),
        ("ano+h3r=ne", False),
        ("ǖnicode", False),
        ("♪♫♬♭♮♯", False),
        ("", False),
        (None, False),
    ),
)
def test_param_verification(test_param, is_valid):
    if is_valid:
        assert validate_param_value(test_param) == test_param
    else:
        assert validate_param_value(test_param) is None


def test_mobile_app():
    rf = RequestFactory()

    # both args exist and have valid values
    req = rf.get("/firefox/app/?product=focus&campaign=firefox-all")
    with patch("bedrock.firefox.redirects.mobile_app_redirector") as mar:
        mobile_app(req)
        mar.assert_called_with(req, "focus", "firefox-all")

    # neither args exist
    req = rf.get("/firefox/app/")
    with patch("bedrock.firefox.redirects.mobile_app_redirector") as mar:
        mobile_app(req)
        mar.assert_called_with(req, "firefox", None)

    # both args exist but invalid values
    req = rf.get("/firefox/app/?product=dude&campaign=walter$")
    with patch("bedrock.firefox.redirects.mobile_app_redirector") as mar:
        mobile_app(req)
        mar.assert_called_with(req, "firefox", None)

    # other args exist
    req = rf.get("/firefox/app/?bunny=dude&maude=artist")
    with patch("bedrock.firefox.redirects.mobile_app_redirector") as mar:
        mobile_app(req)
        mar.assert_called_with(req, "firefox", None)


EXPECTED_REDIRECT_QS = "?redirect_source=mozilla-org"


@pytest.mark.django_db
@pytest.mark.parametrize(
    "path,expected_location,expected_status,follow_redirects",
    [
        (
            "/en-US/firefox/",
            f"{settings.FXC_BASE_URL}/en-US/{EXPECTED_REDIRECT_QS}",
            200,
            True,
        ),
        (
            "/en-US/firefox/new/",
            f"{settings.FXC_BASE_URL}/en-US/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/all/",
            f"{settings.FXC_BASE_URL}/en-US/download/all/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/installer-help/",
            f"{settings.FXC_BASE_URL}/en-US/download/installer-help/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/",
            f"{settings.FXC_BASE_URL}/en-US/{EXPECTED_REDIRECT_QS}",
            200,
            True,
        ),
        (
            "/en-US/firefox/browsers/best-browser/",
            f"{settings.FXC_BASE_URL}/en-US/more/best-browser/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/browser-history/",
            f"{settings.FXC_BASE_URL}/en-US/more/browser-history/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/chromebook/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/desktop/chromebook/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/compare/",
            f"{settings.FXC_BASE_URL}/en-US/compare/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/compare/brave/",
            f"{settings.FXC_BASE_URL}/en-US/compare/brave/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/compare/chrome/",
            f"{settings.FXC_BASE_URL}/en-US/compare/chrome/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/compare/edge/",
            f"{settings.FXC_BASE_URL}/en-US/compare/edge/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/compare/opera/",
            f"{settings.FXC_BASE_URL}/en-US/compare/opera/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/compare/safari/",
            f"{settings.FXC_BASE_URL}/en-US/compare/safari/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/incognito-browser/",
            f"{settings.FXC_BASE_URL}/en-US/more/incognito-browser/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/mobile/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/mobile/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/mobile/android/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/mobile/android/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/mobile/focus/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/mobile/focus/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/mobile/ios/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/mobile/ios/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/update-your-browser/",
            f"{settings.FXC_BASE_URL}/en-US/more/update-your-browser/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/what-is-a-browser/",
            f"{settings.FXC_BASE_URL}/en-US/more/what-is-a-browser/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/browsers/windows-64-bit/",
            f"{settings.FXC_BASE_URL}/en-US/more/windows-64-bit/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/channel/android/",
            f"{settings.FXC_BASE_URL}/en-US/channel/android/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/channel/desktop/",
            f"{settings.FXC_BASE_URL}/en-US/channel/desktop/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/channel/ios/",
            f"{settings.FXC_BASE_URL}/en-US/channel/ios/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/developer/",
            f"{settings.FXC_BASE_URL}/en-US/channel/desktop/developer/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/enterprise/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/enterprise/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/faq/",
            f"{settings.FXC_BASE_URL}/en-US/more/faq/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/",
            f"{settings.FXC_BASE_URL}/en-US/features/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/adblocker/",
            f"{settings.FXC_BASE_URL}/en-US/features/adblocker/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/add-ons/",
            f"{settings.FXC_BASE_URL}/en-US/features/add-ons/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/block-fingerprinting/",
            f"{settings.FXC_BASE_URL}/en-US/features/block-fingerprinting/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/bookmarks/",
            f"{settings.FXC_BASE_URL}/en-US/features/bookmarks/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/customize/",
            f"{settings.FXC_BASE_URL}/en-US/features/customize/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/eyedropper/",
            f"{settings.FXC_BASE_URL}/en-US/features/eyedropper/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/fast/",
            f"{settings.FXC_BASE_URL}/en-US/features/fast/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/password-manager/",
            f"{settings.FXC_BASE_URL}/en-US/features/password-manager/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/pdf-editor/",
            f"{settings.FXC_BASE_URL}/en-US/features/pdf-editor/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/picture-in-picture/",
            f"{settings.FXC_BASE_URL}/en-US/features/picture-in-picture/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/pinned-tabs/",
            f"{settings.FXC_BASE_URL}/en-US/features/pinned-tabs/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/private-browsing/",
            f"{settings.FXC_BASE_URL}/en-US/features/private-browsing/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/private/",
            f"{settings.FXC_BASE_URL}/en-US/features/private/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/sync/",
            f"{settings.FXC_BASE_URL}/en-US/features/sync/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/tips/",
            f"{settings.FXC_BASE_URL}/en-US/features/tips/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/features/translate/",
            f"{settings.FXC_BASE_URL}/en-US/features/translate/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/ios/testflight/",
            f"{settings.FXC_BASE_URL}/en-US/channel/ios/testflight/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/linux/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/desktop/linux/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/mac/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/desktop/mac/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/more/",
            f"{settings.FXC_BASE_URL}/en-US/more/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/set-as-default/",
            f"{settings.FXC_BASE_URL}/en-US/landing/set-as-default/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/set-as-default/thanks/",
            f"{settings.FXC_BASE_URL}/en-US/landing/set-as-default/thanks/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/unsupported-systems/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/unsupported-systems/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/en-US/firefox/windows/",
            f"{settings.FXC_BASE_URL}/en-US/browsers/desktop/windows/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/de/firefox/windows/",
            f"{settings.FXC_BASE_URL}/de/browsers/desktop/windows/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/fr-CA/firefox/windows/",
            f"{settings.FXC_BASE_URL}/fr-CA/browsers/desktop/windows/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        # Also test some without the
        (
            "/firefox/new/",
            f"{settings.FXC_BASE_URL}/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/firefox/set-as-default/",
            f"{settings.FXC_BASE_URL}/landing/set-as-default/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
        (
            "/firefox/browsers/incognito-browser/",
            f"{settings.FXC_BASE_URL}/more/incognito-browser/{EXPECTED_REDIRECT_QS}",
            301,
            False,
        ),
    ],
)
def test_springfield_redirect_patterns(
    client,
    path,
    expected_location,
    expected_status,
    follow_redirects,
):
    response = client.get(
        path,
        follow=follow_redirects,
    )
    assert response.status_code == expected_status
    if expected_status in [200, 404]:
        assert "Location" not in response.headers
    else:
        assert response.headers["Location"] == expected_location


@pytest.mark.django_db
@pytest.mark.parametrize(
    "path,expected_location,expected_status,follow_redirects",
    [
        (
            "/en-US/firefox/installer-help/?channel=beta&installer_lang=en_US",
            f"{settings.FXC_BASE_URL}/en-US/download/installer-help/?redirect_source=mozilla-org&channel=beta&installer_lang=en_US",
            301,
            False,
        ),
        (
            "/en-US/firefox/new/?foo=bar",
            f"{settings.FXC_BASE_URL}/en-US/?redirect_source=mozilla-org&foo=bar",
            301,
            False,
        ),
    ],
)
def test_springfield_redirects_carry_over_querystrings_and_add_redirect_source(
    client,
    path,
    expected_location,
    expected_status,
    follow_redirects,
):
    response = client.get(
        path,
        follow=follow_redirects,
    )
    assert response.status_code == expected_status
    if expected_status in [200, 404]:
        assert "Location" not in response.headers
    else:
        assert response.headers["Location"] == expected_location


@pytest.mark.django_db
@pytest.mark.parametrize(
    "path",
    (
        "/en-US/firefox/landing/get/",
        "/en-US/firefox/138.0/whatsnew/",
        "/en-US/firefox/nightly/firstrun/",
        "/en-US/firefox/welcome/19/",
        "/en-US/firefox/download/thanks/",
    ),
)
def test_paths_not_to_be_redirected_to_springfield(client, path):
    resp = client.get(path, follow=False)
    assert "Location" not in resp.headers
    assert resp.status_code == 200


def test_mobile_app_redirector_does_not_go_to_springfield(client):
    resp = client.get("/en-US/firefox/browsers/mobile/app/")
    assert resp.status_code == 301
    assert resp.headers["Location"] == "https://apps.apple.com/app/apple-store/id989804926"


@pytest.mark.django_db
@pytest.mark.parametrize(
    "path",
    (
        "/firefox/releasenotes/",
        "/firefox/system-requirements/",
        "/firefox/android/releasenotes/",
        "/firefox/android/system-requirements/",
        "/firefox/ios/releasenotes/",
        "/firefox/ios/system-requirements/",
        "/firefox/releases/",
    ),
)
def test_releasenotes_generic_urls_not_rediected_to_springfield(client, path):
    resp = client.get(path)
    assert resp.status_code == 302
    assert settings.FXC_BASE_URL not in resp.headers["Location"]
    assert resp.headers["Location"].startswith("/")


@pytest.mark.parametrize(
    "path, expected_dest",
    (
        ("/en-US/firefox/new/?hello=world", f"{settings.FXC_BASE_URL}/en-US/{EXPECTED_REDIRECT_QS}&hello=world"),
        ("/en-US/firefox/new/", f"{settings.FXC_BASE_URL}/en-US/{EXPECTED_REDIRECT_QS}"),
        (
            "/en-US/firefox/installer-help/?bar=baz&bam=bam",
            f"{settings.FXC_BASE_URL}/en-US/download/installer-help/{EXPECTED_REDIRECT_QS}&bar=baz&bam=bam",
        ),
        ("/en-US/firefox/installer-help/", f"{settings.FXC_BASE_URL}/en-US/download/installer-help/{EXPECTED_REDIRECT_QS}"),
    ),
)
def test_subsequent_redirects_do_not_carry_querystrings_from_earlier_requests(
    client,
    path,
    expected_dest,
):
    # Safety check that Django/Bedrock isn't cacheing querystrings used in other
    # responses. Both of the paramatrized paths above have been used in earlier
    # tests in this suite, where they DID include extra querystrings, which should
    # NOT appear in the responses for this test. We also include dupes here
    resp = client.get(path, secure=True)
    assert resp.status_code == 301
    assert resp.headers["Location"] == expected_dest


@pytest.mark.parametrize(
    "path, expected_dest",
    (
        ("/firefox/new/", f"{settings.FXC_BASE_URL}/{EXPECTED_REDIRECT_QS}"),
        ("/firefox/set-as-default/", f"{settings.FXC_BASE_URL}/landing/set-as-default/{EXPECTED_REDIRECT_QS}"),
        ("/firefox/browsers/incognito-browser/", f"{settings.FXC_BASE_URL}/more/incognito-browser/{EXPECTED_REDIRECT_QS}"),
    ),
)
def test_offsite_redirects_still_work_when_locale_not_in_source_path(
    client,
    path,
    expected_dest,
):
    # Our redirects kick in before our locale-prepending middleware, so we may
    # find we have some redirects that don't have a locale when they send the
    # user to www.firefox.com
    resp = client.get(path, secure=True)
    assert resp.status_code == 301
    assert resp.headers["Location"] == expected_dest
