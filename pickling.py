import pickle
import json

caps = {
    'Australia': 'Canberra',
    'Eire': 'Dublin',
    'UK': 'London',
    'US': 'Washington',
    'foo': ["fizz", "fuzz", "fozz"]
}
#
# create a pickle
outp = open('capitals.p', 'wb')
pickle.dump(caps, outp)
outp.close()

# load pickle
inp = open('capitals.p', 'rb')
caps_loaded = pickle.load(inp)
inp.close()



outp = open('capitals.json', 'w')
my_json_caps = json.dump(caps, outp)
#json.loads
outp.close()
caps_from_json = json.loads(my_json_caps)
print(caps_from_json)