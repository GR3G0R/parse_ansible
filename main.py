import json
import re
from pprint import pprint

def pr_number_from(url):
  matcher = re.compile(".*?/pr-(?P<pr_number>\d{4})")
  full_url = url['Names'][0]
  pr_number = matcher.match(full_url)
  if pr_number:
    pr_number = pr_number.group('pr_number')
    return pr_number

if __name__ == '__main__':
  with open('ansible_dump.json') as data_file:
    data = json.load(data_file)
    pr_numbers = map(pr_number_from, data)
    pr_numbers = filter(lambda value: value is not None, pr_numbers)
    pprint(pr_numbers)

  pprint(len(data))
