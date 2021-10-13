import unittest
from unittest import result
from unittest.mock import patch

def repository():
    result={
  "message": "Validation Failed",
  "errors": [
    {
      "resource": "Search",
      "field": "q",
      "code": "missing"
    }
  ],
  "documentation_url": "https://docs.github.com/v3/search"
}
    return result


class test(unittest.TestCase):
    @patch('https://api.github.com/search/repositories')

    def test_repository(self,mocked_function):
        mocked_function.return_value= {
        "total_count": 1,
        "items": [
        {
        "id": 63476337,
        "name": "Python",
        "full_name": "TheAlgorithms/Python",
        "private": False,
        "description": "All Algorithms implemented in Python",
        "forks": 31806,
        "open_issues": 49,
        "watchers": 118919,
        "default_branch": "master",
        "score": 1.0
        }
        ]
        }
        print(self.assertEqual(repository,result))


if __name__== "__main__":
    unittest.main()
