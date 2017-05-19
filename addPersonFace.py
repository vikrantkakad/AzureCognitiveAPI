import httplib, urllib, base64
import sys

personId = sys.argv[1]
pURL = sys.argv[2]
personGroup = sys.argv[3]
KEY = sys.argv[4]

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/" + personGroup + "/persons/" + personId +"/persistedFaces?%s" % params, "{'url':'" + pURL + "'}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
