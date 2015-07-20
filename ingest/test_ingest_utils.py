import unittest
import ingest_utils
import test_ingest_utils_fixtures as fixtures


class TestIngestUtils(unittest.TestCase):
    def test_assert_good_response(self):
        fake_response = fixtures.FakeBadResponse()
        self.assertRaises(AssertionError,
                          ingest_utils.assert_good_response,
                          fake_response)

    def test_html_to_links(self):
        links = ingest_utils.html_to_links(fixtures.html)
        self.assertItemsEqual(links, fixtures.links)

if __name__ == '__main__':
    unittest.main()
