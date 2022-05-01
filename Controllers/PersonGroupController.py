from Resources import ReadFunctions, WritingFunctions, PersonGroupConfig
from Controllers import RequestsFunctions
import json


def create_person_group_id(person_name, description):
    PERSON_GROUP_ID = WritingFunctions.save_person_group_info(person_name)
        
    ENDPOINT, KEY = ReadFunctions.get_connection_string()
        
    headers = PersonGroupConfig.header(KEY)
    
    body = PersonGroupConfig.body(person_name, description)
        
    url = ReadFunctions.get_person_group_url(ENDPOINT, PERSON_GROUP_ID)
    
    try:
        response = RequestsFunctions.post_Http(url, headers, body)
        parse = json.loads(response.text)
        
    except Exception:
        print(f"\nError to create person group id {person_name}")
        
    else:    
        print(f"\nCreated person group id {person_name} successfully")
        return parse
        
    return None
        

