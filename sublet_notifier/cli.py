from sublet_notifier.commands.wloo_listings_scraper import WlooListingsScraper
from sublet_notifier.email import send_email
from time import sleep


def main():
    scraper = WlooListingsScraper()

    while (1):
        urls = scraper.get_sublets()

        if len(urls) > 0:
            send_email("%s new sublets" % len(urls), "\n".join(urls))

        sleep(60 * 20)
