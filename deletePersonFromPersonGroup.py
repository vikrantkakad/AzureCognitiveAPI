import httplib, urllib, base64
import sys

personId = sys.argv[1]
personGroup = sys.argv[2]
KEY = sys.argv[3]

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("DELETE", "/face/v1.0/persongroups/" + personGroup + "/persons/" + personId +"?%s" % params, "", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

