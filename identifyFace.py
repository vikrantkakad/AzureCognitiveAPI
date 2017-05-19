import httplib, urllib, base64
import json
import sys
import cognitive_face as CF

img_url = sys.argv[1]
personGroup = sys.argv[2]
KEY = sys.argv[3]

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}

faceList = []
CF.Key.set(KEY)
result = CF.face.detect(img_url)
for i in result:
	faceList.append(i["faceId"])

bodyData = {}
bodyData['personGroupId'] = personGroup
bodyData['faceIds'] = faceList
bodyData['maxNumOfCandidatesReturned'] = 5
bodyData['confidenceThreshold'] = 0.5
body = json.dumps(bodyData)

params = urllib.urlencode({
})
listParams = urllib.urlencode({
    # Request parameters
    'start': '0',
    'top': '1000',
})

data = ''
try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/identify?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

listData = ''
try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/face/v1.0/persongroups/" + personGroup + "/persons?%s" % listParams, "", headers)
    response = conn.getresponse()
    listData = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

faceJson = json.loads(data)
listJsonData = json.loads(listData)
for val in faceJson:
    if (len(val['candidates']) != 0):
        personId = val['candidates'][0]['personId']
        for id in listJsonData:
            if (personId == id['personId']):
                print 'person found: ', id['name']
    else:
        print "Unknown faceId: ", val['faceId']

