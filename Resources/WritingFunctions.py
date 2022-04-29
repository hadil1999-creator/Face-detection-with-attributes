from Resources import ReadFunctions



def create_file_txt(file_name, data):
    try:
        f = open(file_name+'.txt', "w+")
        
    except Exception:
        print(f"\nError to create file {file_name}")
        
    else: 
        f.write(data)
        f.close()
        
def save_person_group_info(person_name):
    person_group_info = ""
    
    try:
        PERSON_GROUP_ID, TARGET_PERSON_GROUP_ID = ReadFunctions.get_person_group_id()
        person_group_info += (person_name + '\r\n')
        person_group_info += ('Person-Group-ID\r\n' + PERSON_GROUP_ID + '\r\n')
        person_group_info += ('Tarjet-Person-Group-ID\r\n' + TARGET_PERSON_GROUP_ID + '\r\n')
        
    except Exception:
        print(f"\nError to save {person_name} group info")

    else:
        create_file_txt(person_name, person_group_info)
        return PERSON_GROUP_ID
        