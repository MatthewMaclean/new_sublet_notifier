from bs4 import BeautifulSoup
from re import findall
from urllib2 import urlopen


class WlooListingsScraper:
    BASE_URL = "https://listings.och.uwaterloo.ca/Listings"
    NUMBER_PER_PAGE = 50
    SEARCH_URL = "Search/Results?re=0&rl=&ru=&aa=2&trm=1&occ=0&g=0&smk=0&" + \
        "cty=Waterloo&str=&its=&v=3&tt=&afm=1&afy=2015&atm=4&aty=2015&" + \
        "bt=&pt=1&pkm=2&ps=%s" % (NUMBER_PER_PAGE)

    def __init__(self):
        self.sublets_already_known = []

    def get_sublets(self):
        return_urls = []
        page = 1

        while(1):
            ids = self._get_ids(page)

            return_urls.extend(self.__generate_urls_from_ids(ids))
            page += 1

            if len(ids) < self.NUMBER_PER_PAGE:
                break

        return return_urls

    def clear_history(self):
        del self.sublets_already_known[:]

    def _get_ids(self, page):
        page_contents = urlopen("%s/%s&page=%s" % (
            self.BASE_URL,
            self.SEARCH_URL,
            page)).read()

        soup = BeautifulSoup(page_contents)
        rental_contents = "\n".join(
            [tag.prettify() for tag in soup.find_all(id="Rentals")])

        return findall(
            r"href=\"\/Listings\/Details\/Show\?rentalId=(\d+)",
            rental_contents)

    def __generate_urls_from_ids(self, ids):
        urls = []

        for id in ids:
            if id in self.sublets_already_known:
                continue

            self.sublets_already_known.append(id)
            urls.append("%s/Details/Show?rentalId=%s" % (self.BASE_URL, id))

        return urls
