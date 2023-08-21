# Read data from the file
with open('extracted_data.txt', 'r') as f:
    lines = f.readlines()

# Process the data and create the key vector map
key_vector_map = {}
for line in lines:
    values = line.strip().split('\t')
    if len(values) >= 2:
        key = values[0]
        vector = values[1].split(',') if ',' in values[1] else values[1].split()
        vector = [v for v in vector if (v.startswith('NR') or v.startswith('NC')) and ',' not in v and len(v) > 3]  # Filter values starting with 'NR' or 'NC', without comma, and length greater than 3
        
        # Convert vector to a set to ensure distinct elements
        vector = list(set(vector))
        if vector and len(key) == 2:  # Include keys with length 2 and single values
            if key in key_vector_map:
                key_vector_map[key].extend(vector)
            else:
                key_vector_map[key]=vector


file_content = []
# making elements of each vector for different key unique
for key in key_vector_map:
    key_vector_map[key]=list(set(key_vector_map[key]))
with open('slot_mapping.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            words = line.split(',')
            words = [word.strip() for word in words]
            file_content.append(words)

# Print the vector of vectors to verify
# for vector in file_content:
result_vector = []

for vector in file_content:
    new_vector = []
    for key in vector:
        if key in key_vector_map:
            new_vector.extend(key_vector_map[key])
    result_vector.append(new_vector)

# Print the result vector of vectors
#print(result_vector)

#converting to json form
all_rooms=set([])
for i in result_vector:
    for j in i:
        all_rooms.add(j)
        
free_rooms = []
for i in result_vector:
    temp=list(all_rooms-set(i))
    free_rooms.append(temp)
        
# print(free_rooms)

day_json=[]
arr_json=[]
for i in range(46):
    if i and i%9==0:
        arr_json.append(day_json)
        day_json=[]
    if i==45:
        break
    timing={
        "id": i%9+1,
        "time": free_rooms[i]
    }
    day_json.append(timing)
    
json_file={
    "MON":arr_json[0],
    "TUE":arr_json[1],
    "WED":arr_json[2],
    "THU":arr_json[3],
    "FRI":arr_json[4]
}    

print(json_file)
