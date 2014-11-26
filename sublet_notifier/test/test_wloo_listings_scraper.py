from unittest2 import TestCase
from sublet_notifier.commands.wloo_listings_scraper import WlooListingsScraper


class WeeklyWinnerTest(TestCase):
    def get_url_path(self, id):
        return "https://listings.och.uwaterloo.ca/Listings/Details/" + \
            "Show?rentalId=%s" % (id)

    def test_single_page(self):
        class TestWlooListingsScraper(WlooListingsScraper):
            def _get_ids(self, page):
                if page != 1:
                    raise Exception("Invalid page")

                return ["1"]

        scraper = TestWlooListingsScraper()
        self.assertEqual([self.get_url_path("1")], scraper.get_sublets())

    def test_multiple_pages(self):
        class TestWlooListingsScraper(WlooListingsScraper):
            def _get_ids(self, page):
                if page == 1:
                    return list(xrange(0, 50))
                elif page == 2:
                    return list(xrange(50, 65))
                else:
                    raise Exception("Invalid page")

        scraper = TestWlooListingsScraper()
        self.assertEqual(
            [self.get_url_path(id) for id in xrange(0, 65)],
            scraper.get_sublets())
