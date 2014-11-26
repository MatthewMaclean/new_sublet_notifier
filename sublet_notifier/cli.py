from sublet_notifier.commands.wloo_listings_scraper import WlooListingsScraper
from sublet_notifier.email import send_email


def main():
    scraper = WlooListingsScraper()
    urls = scraper.get_sublets()

    if len(urls) > 0:
        return send_email("%s new sublets" % len(urls), "\n".join(urls))
