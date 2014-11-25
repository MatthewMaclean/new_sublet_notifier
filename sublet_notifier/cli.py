from sublet_notifier.commands.wloo_listings_scraper import WlooListingsScraper


def main():
    scraper = WlooListingsScraper()
    scraper.get_sublets()
    return 0
