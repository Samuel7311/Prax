import configparser

FILE = "performance.txt"

# storing payload to the file
def store_performance(payload):

    # TODO: zapisanie payload do suboru pomocou configparser

    parser = configparser.RawConfigParser()
    parser.add_section('performance')
    
    for key, value in payload.items():
        parser.set('performance', key, str(value))
    
    try:
        with open(FILE, 'a') as configfile:
            parser.write(configfile)
            configfile.write('\n')
    except IOError:
        print("Error writing to file!")


# nacitanie posledneho zaznamu
def load_performance():
    payload = {}
    parser = configparser.RawConfigParser()
    
    try:
        with open(FILE, 'r') as configfile:
            content = configfile.read()
            sections = content.split('[performance]\n')
            
            if sections:
                last_section = sections[-1]
                parser.read_string('[performance]\n' + last_section)
                
                if parser.has_section('performance'):
                    for key in parser.options('performance'):
                        payload[key] = parser.get('performance', key)
    except IOError:
        print("Error reading the file!")
    
    return payload

payload = {
    "datum": "2024-05-21",
    "cas": "12:20.20",
    "a": 1,
    "b": 2
}
store_performance(payload)

payload = {
    "datum": "2024-05-21",
    "cas": "12:40.20",
    "a": 1,
    "b": 2
}
store_performance(payload)

payload = {
    "datum": "2024-05-21",
    "cas": "15:20.20",
    "a": 1,
    "b": 2
}
store_performance(payload)

payload = {'current_date': '2024-05-21', 'current_time': '12:10:00', 'duration': '65', 'selected_icon': 5}
store_performance(payload)

x = load_performance()
print(x)
