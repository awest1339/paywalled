'''
Library to circumvent certain paywalled web pages.
This CL script accepts a URL as an argument, saves
the corresponding html file to the local filesystem,
and then opens it in a new instance of a web browser.

The page should be opened in the user's default directory.
The html is stored in a temp file on the local filesystem.

Author: Austin West
'''
import os
import argparse
import webbrowser
import requests
from uuid import uuid4

if os.path.exists(os.path.expandvars('%TEMP%')):
    TEMP_FILE = os.path.join(
        os.path.expandvars('%TEMP%'),
        '%s.html' % str(uuid4())
    )
elif os.path.exists('/tmp/'):
    TEMP_FILE = os.path.join('/tmp/', '%s.html' % str(uuid4()   ))
else:
    raise ValueError('Coudn\'t find temp dir to store html file')

def main():
    parser = argparse.ArgumentParser(description='Pass in a url')
    parser.add_argument('url', nargs=1, help='url to open')
    args = parser.parse_args()

    r = requests.get(args.url[0], verify=False)

    if r.status_code == 200:
        with open(TEMP_FILE, 'w') as file_:
            file_.write(r.content)

    webbrowser.open_new_tab('%s%s' % ('file://', TEMP_FILE))


if __name__ == '__main__':
    main()
