import unittest
from unittest import mock
import main
import warnings

class MyTestCase(unittest.TestCase):
    @mock.patch("aws_s3.S3Management",
                mock.MagicMock(return_value={'Buckets':[{'Name': 'jinmin-1'},{'Name': 'jinmin-2'}]}))
    def test_main(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        result = main.run('jinmin')
        assert len(result) > 0

if __name__ == '__main__':
    unittest.main()