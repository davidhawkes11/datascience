"""
urllib3 tests for data mining.
Reference page is at:
https://pypi.python.org/pypi/urllib3#downloads
"""

import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://google.com/')
print r.status, r.data
