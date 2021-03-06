import unittest
import graphite_url_parser

class GraphiteUrlParserTests(unittest.TestCase):
    def test_url_decoded_without_data_loss(self):
        raw_url = """http://graphite/render?width=500&from=-2hours\
&until=now&height=250&lineMode=connected&target=movingAverage%28\
*.timers.tweetsearch.query.mean%2C5%29&title=Tweet.Search&\
uniq=0.6707039752987425"""

        parsed_url = """http://graphite/render?
width=500
from=-2hours
until=now
height=250
lineMode=connected
target=movingAverage(*.timers.tweetsearch.query.mean,5)
title=Tweet.Search
uniq=0.6707039752987425"""

        transformed_url = graphite_url_parser.decode(raw_url)
        self.assertEqual(transformed_url, parsed_url)
        
    def test_url_encoded_without_data_loss(self):

        parsed_url = """http://graphite/render?
width=500
from=-2hours
until=now
height=250
lineMode=connected
target=movingAverage(*.timers.tweetsearch.query.mean,5)
title=Tweet.Search
uniq=0.6707039752987425"""

        raw_url = """http://graphite/render?width=500&from=-2hours\
&until=now&height=250&lineMode=connected&target=movingAverage(\
*.timers.tweetsearch.query.mean%2C5)&title=Tweet.Search&\
uniq=0.6707039752987425"""

        transformed_url = graphite_url_parser.encode(parsed_url)
        self.assertEqual(transformed_url, raw_url)

    def test_complex_url_decoded(self):

        raw_url = """http://graphite.awesome.graphs.com/render?\
width=400&from=-4hours&until=-&height=400&target=summarize\
(sumSeries(stats.timers.accounts.*.http.post.accounts.response_time.count))\
&drawNullAsZero=true&title=Example&\
_uniq=0.11944825737737119"""

        parsed_url = """http://graphite.awesome.graphs.com/render?
width=400
from=-4hours
until=-
height=400
target=summarize(sumSeries
  (stats.timers.accounts.*.http.post.accounts.response_time.count))
drawNullAsZero=true
title=Example
_uniq=0.11944825737737119"""

        transformed_url = graphite_url_parser.decode(raw_url)
        self.assertEqual(transformed_url, parsed_url)

    def test_complex_url_encoded(self):

        raw_url = """http://graphite.awesome.graphs.com/render?\
width=400&from=-4hours&until=-&height=400&target=summarize\
(sumSeries(stats.timers.accounts.*.http.post.accounts.response_time.count))\
&drawNullAsZero=true&title=Example&\
_uniq=0.11944825737737119"""

        parsed_url = """http://graphite.awesome.graphs.com/render?
width=400
from=-4hours
until=-
height=400
target=summarize(sumSeries
  (stats.timers.accounts.*.http.post.accounts.response_time.count))
drawNullAsZero=true
title=Example
_uniq=0.11944825737737119"""

        transformed_url = graphite_url_parser.encode(parsed_url)
        self.assertEqual(transformed_url, raw_url)
