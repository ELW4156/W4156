import unittest
from indicators.indicators import DomainFakenessIndicator

class TestIndicators(unittest.TestCase):

    def test_black_box(self):
        domainFI = DomainFakenessIndicator()
        domainFI.init("data/knowndomains.csv")

        inWhitelistURL = "https://www.theguardian.com"
        score = domainFI.scoreLink(inWhitelistURL)
        self.assertEqual(score, 0.75)

        notInWhitelist = "https://www.gardenfurnitureonline.com"
        score = domainFI.scoreLink(notInWhitelist)
        self.assertEqual(score, None)

        poorlyFormed = ["this isnt a URL!", "", "127.0.0.1"]
        for poorURL in poorlyFormed:
            score = domainFI.scoreLink(poorURL)
            self.assertEqual(score, None)

        validVariants = ["http://www.theguardian.com?foo=bar",
                         "https://www.theguardian.com",
                         "http://www.theguardian.com",
                         "http://subdomain.theguardian.com"]
        for valid in validVariants:
            score = domainFI.scoreLink(valid)
            self.assertEqual(score, 0.75)


    def test_no_file(self):
        domainFI = DomainFakenessIndicator()
        with self.assertRaises(FileNotFoundError):
            domainFI.init("data/filedoesnotexist.csv")

    def test_mockingOutFile(self):
        domainFI = DomainFakenessIndicator()
        # domainFI.init() I DONT CALL THIS
        domainFI.set_knowndomains({"google.com",  1.0})

        score = domainFI.scoreLink("https://www.google.com/?foo=bar")
        self.assertEqual(score, 1.0)

if __name__ == '__main__':
    unittest.main()
