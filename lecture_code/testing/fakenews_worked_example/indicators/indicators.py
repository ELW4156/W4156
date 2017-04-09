import typing
import csv
from urllib.parse import urlparse
from tld import get_tld

class AbstractIndicator:

    def init(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def scoreLink(self, url: str) -> float:
        raise NotImplementedError("Subclass must implement abstract method")


class DomainFakenessIndicator(AbstractIndicator):

    def scoreLink(self, url: str) -> float:
        """Domain fakeness has a set of known domains which
        have a precalculated score. If the domain is not known then
        the score is None
        :param url: domain to rank
        :return: score
        """
        tld = get_tld(url, fail_silently=True)
        score = self.knownDomains.get(tld, None)
        return score

    def init(self, filename):
        self.knownDomains = {}
        with open(filename, 'rt') as csvfile:
            domainsfile = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(domainsfile, None)
            for row in domainsfile:
                self.knownDomains[row[0]] = float(row[1])


    def set_knowndomains(self, kd):
        self.knownDomains = kd




class URLPathFakenessIndicator(AbstractIndicator):

    def scoreLink(self, url: str) -> float:
        pass

class PageKeywordFakenessIndicator(AbstractIndicator):

    def scoreLink(self, url: str) -> float:
        pass


class SimpleIndicatorAggregator(AbstractIndicator):

    def init(self, indicators: list):
        self.indicators = indicators

    def scoreLink(self, url: str) -> float:
        aggregatedScore = None
        validIndicators = 0
        for indicator in self.indicators:
            indScore = indicator.scoreURL(url)
            if indScore is not None:
                validIndicators+=1
                if aggregatedScore is not None:
                    aggregatedScore += indScore
                else:
                    aggregatedScore = indScore
        return aggregatedScore / validIndicators


#Many different ways to implement design patterns in python
# Below is very crude implementation for reading access to emphasize the
# separation of creational logic from the rest of the code
class IndicatorFactory():

    def makeIndicator(self, args):
        domainFakeness = DomainFakenessIndicator()
        domainFakeness.init("data/domains.csv")

        urlFakeness = URLPathFakenessIndicator()
        urlFakeness.init()

        pageFakeness = PageKeywordFakenessIndicator()
        pageFakeness.init()

        aggregator = SimpleIndicatorAggregator()
        aggregator.init([domainFakeness, urlFakeness, aggregator])
        return aggregator