# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from bedrock.redirects.util import redirect

redirectpatterns = (
    # Bug 608370, 957664
    redirect(r"^press/kit(?:.*\.html|s/?)$", "https://blog.mozilla.org/press/kits/"),
    # bug 877198
    redirect(r"^press/news\.html$", "https://blog.mozilla.org/press/"),
    redirect(
        r"^press/mozilla-2003-10-15\.html$",
        "https://blog.mozilla.org/press/2003/10/mozilla-foundation-launches-new-web-browser-and-end-user-services/",
    ),
    redirect(
        r"^press/mozilla-2004-02-09\.html$",
        "https://blog.mozilla.org/press/2004/02/new-round-of-releases-extends-mozilla-project%C2%92s-standards-based-open-source-offerings/",
    ),
    redirect(r"^press/mozilla-2004-02-17\.html$", "https://blog.mozilla.org/press/2004/02/mozilla-gains-stronghold-in-europe/"),
    redirect(
        r"^press/mozilla-2004-02-26\.html$", "https://blog.mozilla.org/press/2004/02/mozilla-foundation-rallies-supporters-to-take-back-the-web/"
    ),
    redirect(r"^press/mozilla-2004-05-03\.html$", "https://blog.mozilla.org/press/2004/05/mozilla-foundation-releases-thunderbird-0-6/"),
    redirect(r"^press/mozilla-2004-06-15\.html$", "https://blog.mozilla.org/press/2004/06/mozilla-reloads-firefox/"),
    redirect(r"^press/mozilla-2004-06-16\.html$", "https://blog.mozilla.org/press/2004/06/mozilla-foundation-releases-thunderbird-0-7/"),
    redirect(
        r"^press/mozilla-2004-06-30\.html$", "https://blog.mozilla.org/press/2004/06/mozilla-foundation-announces-more-open-scriptable-plugins/"
    ),
    redirect(r"^press/mozilla-2004-08-02\.html$", "https://blog.mozilla.org/press/2004/08/mozilla-foundation-announces-security-bug-bounty-program/"),
    redirect(r"^press/mozilla-2004-08-10\.html$", "https://blog.mozilla.org/press/2004/08/mozilla-foundation-announces-xforms-development-project/"),
    redirect(r"^press/mozilla-2004-08-18\.html$", "https://blog.mozilla.org/press/2004/08/mozilla-affiliate-in-japan-kicks-off/"),
    redirect(
        r"^press/mozilla-2004-09-14-01\.html$",
        "https://blog.mozilla.org/press/2004/09/"
        "mozilla-foundation-announces-first-payments-of-security-bug-bounty-program-further-strengthens-browser-security/",
    ),
    redirect(r"^press/mozilla-2004-09-14-02\.html$", "https://blog.mozilla.org/press/2004/09/firefox-preview-release-and-thunderbird-0-8-released/"),
    redirect(
        r"^press/mozilla-2004-09-20\.html$",
        "https://blog.mozilla.org/press/2004/09/mozilla-firefox-preview-release-hits-one-million-downloads-in-first-four-days-of-availability/",
    ),
    redirect(r"^press/mozilla-2004-10-01-02\.html$", "https://blog.mozilla.org/press/2004/10/important-security-update-for-firefox-available/"),
    redirect(
        r"^press/mozilla-2004-11-09\.html$",
        "https://blog.mozilla.org/press/2004/11/mozilla-foundation-releases-the-highly-anticipated-mozilla-firefox-1-0-web-browser/",
    ),
    redirect(
        r"^press/mozilla-2004-11-22\.html$", "https://blog.mozilla.org/press/2004/11/important-update-to-german-language-version-of-firefox-1-0/"
    ),
    redirect(
        r"^press/mozilla-2004-12-15\.html$",
        "https://blog.mozilla.org/press/2004/12/mozilla-foundation-places-two-page-advocacy-ad-in-the-new-york-times/",
    ),
    redirect(r"^press/mozilla-2004-12-7\.html$", "https://blog.mozilla.org/press/2004/12/mozilla-thunderbird-1-0-email-client-has-landed/"),
    redirect(
        r"^press/mozilla-2005-01-07\.html$",
        "https://blog.mozilla.org/press/2005/01/mozilla-firefox-and-thunderbird-to-support-new-open-standard-platform-for-usb-drives/",
    ),
    redirect(
        r"^press/mozilla-2005-02-02\.html$",
        "https://blog.mozilla.org/press/2005/02/mozilla-foundation-announces-beta-release-of-xforms-1-0-recommendation/",
    ),
    redirect(
        r"^press/mozilla-2005-02-16\.html$",
        "https://blog.mozilla.org/press/2005/01/mozilla-firefox-and-thunderbird-to-support-new-open-standard-platform-for-usb-drives/",
    ),
    redirect(r"^press/mozilla-2005-02-24\.html$", "https://blog.mozilla.org/press/2005/02/mozilla-foundation-announces-update-to-firefox/"),
    redirect(r"^press/mozilla-2005-03-04\.html$", "https://blog.mozilla.org/press/2005/03/mozilla-foundation-expands-with-launch-of-mozilla-china/"),
    redirect(r"^press/mozilla-2005-03-23\.html$", "https://blog.mozilla.org/press/2005/03/mozilla-foundation-releases-security-update-to-firefox/"),
    redirect(r"^press/mozilla-2005-03-28\.html$", "https://blog.mozilla.org/press/2005/03/mozilla-foundation-awards-bug-bounties/"),
    redirect(
        r"^press/mozilla-2005-05-13\.html$",
        "https://blog.mozilla.org/press/2005/05/mozilla-foundation-co-hosts-europes-leading-xml-and-web-developer-conference/",
    ),
    redirect(
        r"^press/mozilla-2005-07-28\.html$",
        "https://blog.mozilla.org/press/2005/07/mozilla-headlines-two-key-open-source-development-conferences-in-august/",
    ),
    redirect(
        r"^press/mozilla-2005-08-03\.html$",
        "https://blog.mozilla.org/press/2005/08/mozilla-foundation-forms-new-organization-to-further-the-creation-"
        "of-free-open-source-internet-software-including-the-award-winning-mozilla-firefox-browser/",
    ),
    redirect(
        r"^press/mozilla-2005-10-03\.html$", "https://blog.mozilla.org/press/2005/10/mozilla-launches-beta-of-comprehensive-online-developer-center/"
    ),
    redirect(r"^press/mozilla-2005-10-19\.html$", "https://blog.mozilla.org/press/2005/10/firefox-surpasses-100-million-downloads/"),
    redirect(
        r"^press/mozilla-2005-11-29\.html$", "https://blog.mozilla.org/press/2005/11/mozilla-introduces-firefox-1-5-and-ups-the-ante-in-web-browsing/"
    ),
    redirect(r"^press/mozilla-2005-11-3\.html$", "https://blog.mozilla.org/press/2005/11/mozilla-kicks-off-extend-firefox-competition/"),
    redirect(r"^press/mozilla-2005-11-30\.html$", "https://blog.mozilla.org/press/2005/11/firefox-1-5-adds-answers-com-for-quick-reference/"),
    redirect(r"^press/mozilla-2005-12-2\.html$", "https://blog.mozilla.org/press/2005/12/mozilla-launches-firefox-flicks-campaign/"),
    redirect(r"^press/mozilla-2005-12-22\.html$", "https://blog.mozilla.org/press/2005/12/mozilla-launches-firefox-flicks-ad-contest/"),
    redirect(r"^press/mozilla-2006-01-12\.html$", "https://blog.mozilla.org/press/2006/01/mozilla-releases-thunderbird-1-5-email-client/"),
    redirect(r"^press/mozilla-2006-01-24\.html$", "https://blog.mozilla.org/press/2006/01/firefox-1-5-adoption-rising-as-browser-garners-acclaim/"),
    redirect(r"^press/mozilla-2006-01-25\.html$", "https://blog.mozilla.org/press/2006/01/indie-film-all-stars-foin-firefox-flicks-crew/"),
    redirect(
        r"^press/mozilla-2006-02-03\.html$",
        "https://blog.mozilla.org/press/2006/02/mozilla-releases-preview-of-application-framework-for-"
        "development-of-cross-platform-internet-client-applications/",
    ),
    redirect(r"^press/mozilla-2006-03-02\.html$", "https://blog.mozilla.org/press/2006/03/mozilla-announces-winners-of-extend-firefox-competition/"),
    redirect(
        r"^press/mozilla-2006-04-12\.html$",
        "https://blog.mozilla.org/press/2006/04/mozilla-showcases-first-round-of-community-produced-firefox-flicks-videos/",
    ),
    redirect(
        r"^press/mozilla-2006-04-18\.html$",
        "https://blog.mozilla.org/press/2006/04/mozilla-receives-over-280-community-produced-videos-for-firefox-flicks/",
    ),
    redirect(r"^press/mozilla-2006-04-27\.html$", "https://blog.mozilla.org/press/2006/04/firefox-flicks-video-contest-winners-announced/"),
    redirect(
        r"^press/mozilla-2006-06-14\.html$", "https://blog.mozilla.org/press/2006/06/mozilla-feeds-soccer-fans-passion-with-new-firefox-add-on/"
    ),
    redirect(
        r"^press/mozilla-2006-10-11\.html$",
        "https://blog.mozilla.org/press/2006/10/qualcomm-launches-project-in-collaboration-with-"
        "mozilla-foundation-to-develop-open-source-version-of-eudora-email-program/",
    ),
    redirect(r"^press/mozilla-2006-10-24-02\.html$", "https://blog.mozilla.org/press/2006/10/firefox-moving-the-internet-forward/"),
    redirect(
        r"^press/mozilla-2006-10-24\.html$",
        "https://blog.mozilla.org/press/2006/10/mozilla-releases-major-update-to-firefox-and-raises-the-bar-for-online-experience/",
    ),
    redirect(
        r"^press/mozilla-2006-11-07\.html$",
        "https://blog.mozilla.org/press/2006/11/adobe-and-mozilla-foundation-to-open-source-flash-player-scripting-engine/",
    ),
    redirect(
        r"^press/mozilla-2006-12-04\.html$",
        "https://blog.mozilla.org/press/2006/12/the-world-economic-forum-announces-technology-pioneers-2007-mozilla-selected/",
    ),
    redirect(r"^press/mozilla-2006-12-11\.html$", "https://blog.mozilla.org/press/2006/12/mozilla-firefox-headed-for-primetime/"),
    redirect(
        r"^press/mozilla-2007-02-07\.html$",
        "https://blog.mozilla.org/press/2007/02/kodak-and-mozilla-join-forces-to-make-sharing-photos-even-easier/",
    ),
    redirect(r"^press/mozilla-2007-03-27\.html$", "https://blog.mozilla.org/press/2007/03/mozilla-launches-new-firefox-add-ons-web-site/"),
    redirect(
        r"^press/mozilla-2007-03-28\.html$",
        "https://blog.mozilla.org/press/2007/03/mozilla-and-ebay-working-together-to-make-the-auction-"
        "experience-easier-for-firefox-users-in-france-germany-and-the-uk/",
    ),
    redirect(r"^press/mozilla-2007-04-19\.html$", "https://blog.mozilla.org/press/2007/04/mozilla-thunderbird-2-soars-to-new-heights/"),
    redirect(
        r"^press/mozilla-2007-05-16\.html$",
        "https://blog.mozilla.org/press/2007/05/united-nations-agency-awards-mozilla-world-information-society-award/",
    ),
    redirect(r"^press/mozilla-2007-07-04\.html$", "https://blog.mozilla.org/press/2007/07/mozilla-and-ebay-launch-firefox-companion-for-ebay-users/"),
    redirect(r"^press/mozilla-2007-08-10\.html$", "https://blog.mozilla.org/press/2007/08/mozilla-to-host-24-hour-worldwide-community-event/"),
    redirect(
        r"^press/mozilla-2007-08-28\.html$",
        "https://blog.mozilla.org/press/2007/08/mozilla-welcomes-students-back-to-school-with-firefox-campus-edition/",
    ),
    redirect(
        r"^press/mozilla-2007-09-17-faq\.html$",
        "https://blog.mozilla.org/press/2007/09/mozilla-launches-internet-mail-and-communications-initiative/",
    ),
    redirect(
        r"^press/mozilla-2007-09-17\.html$", "https://blog.mozilla.org/press/2007/09/mozilla-launches-internet-mail-and-communications-initiative/"
    ),
    redirect(
        r"^press/mozilla-2008-01-07-faq\.html$", "https://blog.mozilla.org/press/2008/01/mozilla-appoints-john-lilly-as-chief-executive-officer/"
    ),
    redirect(r"^press/mozilla-2008-01-07\.html$", "https://blog.mozilla.org/press/2008/01/mozilla-appoints-john-lilly-as-chief-executive-officer/"),
    redirect(r"^press/mozilla-2008-02-19-faq\.html$", "https://blog.mozilla.org/press/2008/02/mozilla-messaging-starts-up-operations/"),
    redirect(r"^press/mozilla-2008-02-19\.html$", "https://blog.mozilla.org/press/2008/02/mozilla-messaging-starts-up-operations/"),
    redirect(
        r"^press/mozilla-2008-05-28\.html$",
        "https://blog.mozilla.org/press/2008/05/mozilla-aims-to-set-guinness-world-record-on-firefox-3-download-day/",
    ),
    redirect(
        r"^press/mozilla-2008-06-17-faq\.html$", "https://blog.mozilla.org/press/2008/06/mozilla-releases-firefox-3-and-redefines-the-web-experience/"
    ),
    redirect(
        r"^press/mozilla-2008-06-17\.html$", "https://blog.mozilla.org/press/2008/06/mozilla-releases-firefox-3-and-redefines-the-web-experience/"
    ),
    redirect(
        r"^press/mozilla-2008-07-02\.html$", "https://blog.mozilla.org/press/2008/07/mozilla-sets-new-guinness-world-record-with-firefox-3-downloads/"
    ),
    redirect(
        r"^press/mozilla-2008-11-18\.html$",
        "https://blog.mozilla.org/press/2008/11/mozilla-launches-fashion-your-firefox-and-makes-it-easy-to-customize-the-browsing-experience/",
    ),
    redirect(
        r"^press/mozilla-2008-12-03\.html$",
        "https://blog.mozilla.org/press/2008/12/mozilla-and-zazzle-announce-strategic-relationship-for-apparel-on-demand/",
    ),
    redirect(
        r"^press/mozilla-2009-03-31\.html$",
        "https://blog.mozilla.org/press/2009/03/%C2%AD%C2%ADmozilla-adds-style-and-star-power-to-firefox-with-new-personas/",
    ),
    redirect(r"^press/mozilla-2009-06-30-faq\.html$", "https://blog.mozilla.org/press/2009/06/mozilla-advances-the-web-with-firefox-3-5/"),
    redirect(r"^press/mozilla-2009-06-30\.html$", "https://blog.mozilla.org/press/2009/06/mozilla-advances-the-web-with-firefox-3-5/"),
    redirect(
        r"^press/mozilla-foundation\.html$",
        "https://blog.mozilla.org/press/2003/07/mozilla-org-announces-launch-of-the-mozilla-foundation-to-lead-open-source-browser-efforts/",
    ),
    redirect(r"^press/mozilla1\.0\.html$", "https://blog.mozilla.org/press/2002/06/mozilla-org-launches-mozilla-1-0/"),
    redirect(
        r"^press/open-source-security\.html$",
        "https://blog.mozilla.org/press/2000/01/open-source-development-of-security-products-"
        "possible-worldwide-enhancing-security-and-privacy-for-e-commerce-and-communication/",
    ),
    # Bug 774331 - European press pages
    # en-GB
    redirect(r"^en-GB/press/?$", "https://blog.mozilla.org/press-uk/", locale_prefix=False),
    redirect(r"^en-GB/press/media/?$", "https://blog.mozilla.org/press-uk/media-library/", locale_prefix=False),
    redirect(r"^en-GB/press/media/logos/?$", "https://blog.mozilla.org/press-uk/media-library/", locale_prefix=False),
    redirect(r"^en-GB/press/media/screenshots/?$", "https://blog.mozilla.org/press-uk/media-library/product-screenshots/", locale_prefix=False),
    redirect(r"^en-GB/press/media/images/?$", "https://blog.mozilla.org/press-uk/media-library/", locale_prefix=False),
    redirect(r"^en-GB/press/media/videos/?$", "https://blog.mozilla.org/press-uk/media-library/videos/", locale_prefix=False),
    # de
    redirect(r"^de/press/?$", "https://blog.mozilla.org/press-de/", locale_prefix=False),
    redirect(r"^de/press/media/?$", "https://blog.mozilla.org/press-de/medienbibliothek/", locale_prefix=False),
    redirect(r"^de/press/media/logos/?$", "https://blog.mozilla.org/press-de/medienbibliothek/", locale_prefix=False),
    redirect(r"^de/press/media/screenshots/?$", "https://blog.mozilla.org/press-de/medienbibliothek/produkt-screenshots/", locale_prefix=False),
    redirect(r"^de/press/media/images/?$", "https://blog.mozilla.org/press-de/medienbibliothek/", locale_prefix=False),
    redirect(r"^de/press/media/videos/?$", "https://blog.mozilla.org/press-de/medienbibliothek/videos/", locale_prefix=False),
    redirect(r"^de/press/media/bios/?$", "https://blog.mozilla.org/press/media-library/bios/", locale_prefix=False),
    # fr
    redirect(r"^fr/press/?$", "https://blog.mozilla.org/press-fr/", locale_prefix=False),
    redirect(r"^fr/press/media/?$", "https://blog.mozilla.org/press-fr/bibliotheque-mozilla/", locale_prefix=False),
    redirect(r"^fr/press/media/logos/?$", "https://blog.mozilla.org/press-fr/bibliotheque-mozilla/", locale_prefix=False),
    redirect(
        r"^fr/press/media/screenshots/?$", "https://blog.mozilla.org/press-fr/bibliotheque-mozilla/captures-decran-produits/", locale_prefix=False
    ),
    redirect(r"^fr/press/media/images/?$", "https://blog.mozilla.org/press-fr/bibliotheque-mozilla/", locale_prefix=False),
    redirect(r"^fr/press/media/videos/?$", "https://blog.mozilla.org/press-fr/bibliotheque-mozilla/videos/", locale_prefix=False),
    redirect(r"^fr/press/media/bios/?$", "https://blog.mozilla.org/press/media-library/bios/", locale_prefix=False),
    # it
    redirect(r"^it/press/?$", "https://blog.mozilla.org/press-it/", locale_prefix=False),
    redirect(r"^it/press/media/?$", "https://blog.mozilla.org/press-it/galleria-multimediale/", locale_prefix=False),
    redirect(r"^it/press/media/logos/?$", "https://blog.mozilla.org/press-it/galleria-multimediale/", locale_prefix=False),
    redirect(
        r"^it/press/media/screenshots/?$", "https://blog.mozilla.org/press-it/galleria-multimediale/immagini-del-prodotto/", locale_prefix=False
    ),
    redirect(r"^it/press/media/images/?$", "https://blog.mozilla.org/press-it/galleria-multimediale/", locale_prefix=False),
    redirect(r"^it/press/media/videos/?$", "https://blog.mozilla.org/press-it/galleria-multimediale/videos/", locale_prefix=False),
    redirect(r"^it/press/media/bios/?$", "https://blog.mozilla.org/press/media-library/bios/", locale_prefix=False),
    # es
    redirect(r"^es(-[A-Z]{2})?/press/?$", "https://blog.mozilla.org/press-es/", locale_prefix=False),
    redirect(r"^es(-[A-Z]{2})?/press/media/?$", "https://blog.mozilla.org/press-es/galeria-multimedia-de-mozilla/", locale_prefix=False),
    redirect(r"^es(-[A-Z]{2})?/press/media/logos/?$", "https://blog.mozilla.org/press-es/galeria-multimedia-de-mozilla/", locale_prefix=False),
    redirect(
        r"^es(-[A-Z]{2})?/press/media/screenshots/?$",
        "https://blog.mozilla.org/press-es/galeria-multimedia-de-mozilla/imagenes-del-producto/",
        locale_prefix=False,
    ),
    redirect(r"^es(-[A-Z]{2})?/press/media/images/?$", "https://blog.mozilla.org/press-es/galeria-multimedia-de-mozilla/", locale_prefix=False),
    redirect(
        r"^es(-[A-Z]{2})?/press/media/videos/?$", "https://blog.mozilla.org/press-es/galeria-multimedia-de-mozilla/videos/", locale_prefix=False
    ),
    redirect(r"^es(-[A-Z]{2})?/press/media/bios/?$", "https://blog.mozilla.org/press/media-library/bios/", locale_prefix=False),
    # pl
    redirect(r"^pl/press/?$", "https://blog.mozilla.org/press-pl/", locale_prefix=False),
    redirect(r"^pl/press/media/?$", "https://blog.mozilla.org/press-pl/galeria-multimediow/", locale_prefix=False),
    redirect(r"^pl/press/media/logos/?$", "https://blog.mozilla.org/press-pl/galeria-multimediow/", locale_prefix=False),
    redirect(r"^pl/press/media/screenshots/?$", "https://blog.mozilla.org/press-pl/galeria-multimediow/screenshoty-produktow/", locale_prefix=False),
    redirect(r"^pl/press/media/images/?$", "https://blog.mozilla.org/press-pl/galeria-multimediow/", locale_prefix=False),
    redirect(r"^pl/press/media/videos/?$", "https://blog.mozilla.org/press-pl/galeria-multimediow/videos/", locale_prefix=False),
    redirect(r"^pl/press/media/bios/?$", "https://blog.mozilla.org/press/media-library/bios/", locale_prefix=False),
    # rest
    # Bug 747565
    redirect(r"^press/?$", "https://blog.mozilla.org/press/"),
    redirect(r"^press/ataglance/?$", "https://blog.mozilla.org/press/ataglance/"),
    redirect(r"^press/bios/?$", "https://blog.mozilla.org/press/bios/"),
    redirect(r"^press/kits/?$", "https://blog.mozilla.org/press/kits/"),
    redirect(r"^press/media/?$", "https://blog.mozilla.org/press/media-library/"),
    redirect(r"^press/media/logos/?$", "https://blog.mozilla.org/press/media-library/"),
    redirect(r"^press/media/bios/?$", "https://blog.mozilla.org/press/media-library/bios/"),
    redirect(r"^press/media/screenshots/?$", "https://blog.mozilla.org/press/media-library/screenshots/"),
    redirect(r"^press/media/videos/?$", "https://blog.mozilla.org/press/media-library/videos/"),
)
