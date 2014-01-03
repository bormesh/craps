# vim: set expandtab ts=4 sw=4 syntax=python fileencoding=utf8:

import argparse
import logging
import uuid
import wsgiref.simple_server

import pyrax

log = logging.getLogger('apfur')

def parse_args():

    ap = argparse.ArgumentParser()

    return ap.parse_args()

def serve_upload_page(upload_url, download_url):

    class MyApp(object):

        def __init__(self, upload_url, download_url):
            self.upload_url = upload_url
            self.download_url = download_url

        def render_upload_page(self):

            page = open('./upload.html').read()

            return page.format(
                upload_url=self.upload_url,
                download_url=self.download_url)

        def __call__(self, environ, start_response):

            start_response('200 OK', [])
            return [self.render_upload_page()]

    app = MyApp(upload_url, download_url)
    s = wsgiref.simple_server.make_server('', 8765, app)

    logging.info("About to fire up the wsgi server...")
    s.serve_forever()


if __name__ == '__main__':

    args = parse_args()

    logging.basicConfig(level=logging.DEBUG)

    log.info('Configured logging.')

    # Give credentials to pyrax.

    download_url = "http://doesntwork"
    upload_url = "http://doesntwork"

    log.debug('download_url: {0}'.format(download_url))


    serve_upload_page(upload_url, download_url)
