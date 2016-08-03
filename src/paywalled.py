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
    TEMP_DIR = os.path.join(
        os.path.expandvars('%TEMP%')
    )
elif os.path.exists('/tmp/'):
    TEMP_DIR = os.path.join('/tmp/')
else:
    raise ValueError('Coudn\'t find temp dir to store html file')


def get_web_content(url, proxy=None, no_check_certificate=False):
    if proxy:
        proxies = {
            'http': proxy,
            'https': proxy,
        }
        r = requests.get(url, proxies=proxies, verify=no_check_certificate)
    else:
        r = requests.get(url, verify=no_check_certificate)

    if r.status_code == 200:
        return r.content
        
    else:
        raise ValueError('Connection failed: %s' % r)

def write_web_content_to_file(web_content):
    '''
    filename = url.split('/')[-1]
    if filename:
        full_path = os.path.join(TEMP_DIR, filename)
        if not full_path.endswith('.html'):
            full_path = full_path + '.html'
    else:
        full_path = os.path.join(TEMP_DIR, str(uuid4()) + '.html')
    '''
    full_path = os.path.join(TEMP_DIR, str(uuid4()) + '.html')
    with open(full_path, 'w') as file_:
        file_.write(web_content)
        
    return full_path
    
def open_web_content(full_path):
    webbrowser.open_new_tab('%s%s' % ('file://', full_path))

    
def main():
    parser = argparse.ArgumentParser(description='Pass in a url')
    parser.add_argument('url', nargs=1, help='url to open')
    parser.add_argument('--proxy', nargs=1, help='specify a proxy server to use')
    parser.add_argument('--no-check-certificate', action='store_false', help='disable SSL verification')
    args = parser.parse_args()
    
    if args.proxy:
        web_content = get_web_content(args.url[0], args.proxy[0], args.no_check_certificate)
    else:
        web_content = get_web_content(args.url[0], args.no_check_certificate)

    full_path = write_web_content_to_file(web_content)
    open_web_content(full_path)


if __name__ == '__main__':
    main()
