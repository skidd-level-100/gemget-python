#!/usr/bin/env python3

import socket
import ssl
import urllib.parse

def gemget(url):
    if not "://" in url:
        url = "gemini://" + url
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme != "gemini":
        return False
    # Do the Gemini transaction
    try:
        s = socket.create_connection((parsed_url.netloc, 1965))
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        s = context.wrap_socket(s, server_hostname = parsed_url.netloc)
        s.sendall((url + '\r\n').encode("UTF-8"))
        # Get header and check for redirects
        fp = s.makefile("rb")
        header = fp.readline()
        header = header.decode("UTF-8").strip()
        status, mime = header.split()
    except Exception as err:
        return False
    # Fail if transaction was not successful
    if not status.startswith("2"):
        return False
    # Handle text
    if mime.startswith("text/"):
        body = fp.read()
        body = body.decode("UTF-8") # yes I assume UTF-8 cgi was depricated and I didn't want to learn the new thing, bite me.
        #return data
        return str(body)

if __name__ == '__main__':
    data = gemget("gemini://kennedy.gemi.dev/search?gemget%20in%20python")
    print(data)