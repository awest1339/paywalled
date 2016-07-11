# Description
Downloads paywalled html source to a local temp file, then opens it in the user's default browser. Depending on how the site is paywalled, should bypass the paywall protection.

# Usage
* If using the python version of the code in src/:
    * python paywalled.py paywalled_url
* If using the windows executable version of the code in dist/:
    * paywalled.exe paywalled_url
* To display help message:
    * python paywalled.py --help
* If you are behind a network proxy: 
    * python paywalled.py paywalled_url --proxy <proxy_url>
    * paywalled.exe paywalled_url --proxy <proxy_url>

# Requirements
* requests

# Disclaimer
* This package was written as a proof of concept and thus should not be used by anyone ever. Author takes no responsibility for effects of using this script.
