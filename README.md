# Description
Downloads paywalled html source to a local temp file, then opens it in the user's default browser. Depending on how the site is paywalled, should bypass the paywall protection.

# Usage
* If using the python version of the code in src/:
<pre>python paywalled.py paywalled_url</pre>
* To use the GUI version, run: <pre>python gui_pay.py</pre>
* If using the windows executable version of the code in dist/, just enter the url into the GUI that opens.
* To display help message:
<pre>python paywalled.py --help</pre>
* If you are behind a network proxy: 
<pre>python paywalled.py paywalled_url --proxy proxy_url</pre>

# Using the executable in dist/
* This exe is provided for convenience purposes and may not necessarily kept up to date with the latest code additions.

# Requirements
* requests

# Disclaimer
* This package was written as a proof of concept and thus should not be used by anyone ever. Author takes no responsibility for effects of using this script.
