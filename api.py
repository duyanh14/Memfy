import json
import urllib
import urllib.parse
import urllib.request

class api:

    class config:
        host = 'https://memfy.net/api'

    class request:

        @staticmethod
        def make(action, parameter=None):
            data = urllib.parse.urlencode(parameter)
            data = data.encode('utf-8')
            response = urllib.request.urlopen(api.config.host + '/' + ('/'.join(action)), data)
            return json.loads(response.read())

