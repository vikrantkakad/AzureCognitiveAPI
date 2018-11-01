# Mission Mars Crew FaceId Detection using Microsoft Azure Cognitive APIs 

This is python implementation of APIs for [Microsoft Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/). The problem statement for this solution can be found at [Mission-Mars-Fourth-Horizon-Org/Mission-Briefings](https://github.com/Mission-Mars-Fourth-Horizon-Org/Mission-Briefings/tree/master/CognitiveServices).

[Microsoft Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/) let you build apps with powerful algorithms using just a few lines of code. They work across devices and platforms such as iOS, Android, and Windows, keep improving, and are easy to set up.

For more detailed information about Microsoft Cognitive Services you can refer its [API documentation](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236).

### Steps
1. Create Person Group using your *teamName* & *secreteKey*
> `python createPersonGroup.py <teamName> <personGroup> <key>`

2. You can get Person Group information using below API
> `python getPersonGroupInfo.py <personGroup> <key>`
``` 
Response Example:
{
    "personGroupId": "px_mars_crew",
    "name": "team10",
    "userData": "Mission Mars Crew Team 10"
}
```
3. Then add Person/Crew Members to the recently created Person Group
> `python createPersonInPersonGroup.py <personName> <personGroup> <key>`

4. Provide Face (Photo) details of each Person/Crew Member
> `python addPersonFace.py <personId> <person_photo_url> <personGroup> <key>`

5. If required, you can also delete any Person/Crew Member from Person Group
> `python deletePersonFromPersonGroup.py <personId> <personGroup> <key>`

6. You can also try getting Face Details (age, gender, moustache, beard, facialHair, etc) of any Person/Crew Member using Detect Face API.
> `python detectFace.py <img_url> <key>`
```
Response Example:
  [
      {
          "faceId": "ead1af3a-9e87-4131-9f0b-6f923f8ed221",
          "faceRectangle": {
              "top": 124,
              "left": 459,
              "width": 227,
              "height": 227
          },
          "faceAttributes": {
              "smile": 0.826,
              "headPose": {
                  "pitch": 0,
                  "roll": -16.9,
                  "yaw": 21.3
              },
              "gender": "female",
              "age": 23.8,
              "facialHair": {
                  "moustache": 0,
                  "beard": 0,
                  "sideburns": 0
              },
              "glasses": "ReadingGlasses"
          }
      }
  ]
```

7. Finally after adding all Crew Members to Person Group, train your Person Group
> `python trainPersonGroup.py <personGroup> <key>`

8. To test your API, provide any [Crew's Group Photo](https://raw.githubusercontent.com/MissionMarsFourthHorizon/Mission-Briefings/master/CognitiveServices/images/CrewPhoto.jpg) & verify Persons/Members identified by API
> `python identifyFace.py <group_img_url> <personGroup> <key>`
``` 
Response Example:
  person found:  Ivan Sidorov
  person found:  Jean Dupont
  person found:  Erika Mustermann
  person found:  Juan Pérez
  person found:  Anna Malli
  person found:  Seán Ó Rudaí
  Unknown faceId:  10298c3a-e395-4de9-a179-06995b22a9ca
```

