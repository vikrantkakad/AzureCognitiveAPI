import httplib, urllib, base64
import sys

personGroup = sys.argv[1]
KEY = sys.argv[2]

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': KEY,
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/face/v1.0/persongroups/" + personGroup + "?%s" % params, "", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
