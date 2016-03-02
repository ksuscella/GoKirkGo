#MongoDB Me Crazy - Practice Python File

from pymongo import MongoClient
import json

client = MongoClient()
db = client.kirk

json_test = '{"robot_id":1,"run_number":20160228011453,"angle":0,"distance":0,"decision":0,"cord_list" :{"0":47,"5":56,"10":52,"15":56,"20":59,"25":19,"30":18,"35":17,"40":17,"45":15,"50":15,"55":15,"60":14,"65":15,"70":14,"75":15,"80":15,"85":14,"90":15,"95":16,"100":16,"105":16,"110":17,"115":687,"120":687,"125":687,"130":687,"135":688,"140":688,"145":688,"150":688,"155":688,"160":688}}'

result = db.test.insert_one(
    json.loads(json_test)
)

print result.inserted_id
