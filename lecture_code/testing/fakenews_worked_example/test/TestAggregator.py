import unittest
from indicators.indicators import SimpleIndicatorAggregator
from unittest.mock import MagicMock, Mock

class TestAggregator(unittest.TestCase):

    def test_one_none(self):
        mockIndicator = self.createMocks([0.75, None])

        aggregator = SimpleIndicatorAggregator()
        aggregator.init(mockIndicator)

        score = aggregator.scoreLink("www.google.com")
        self.assertAlmostEqual(score, 0.75)

    def test_aggregator(self):
        mockIndicator = self.createMocks([0.75,1.0,0.25])

        aggregator = SimpleIndicatorAggregator()
        aggregator.init(mockIndicator)

        score = aggregator.scoreLink("www.google.com")
        self.assertAlmostEqual(score, 0.666, delta=0.001)

    def createMocks(self, vals):
        mocks = []
        for v in vals:
            mock = Mock()
            mock.scoreURL = MagicMock(return_value=v)
            mocks.append(mock)
        return mocks

if __name__ == '__main__':
    unittest.main()
