import requests
import json

def get_json_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
        
#    except requests.exceptions.RequestException as e:
#        return None
#    except json.JSONDecodeError as e:
#         return None
    except:
        return None    

def convert_json_to_htmltable(jsondata):
    try:
        html = "<table border=1>"
        
        for land in jsondata['lands']: 
            html += f"<tr class=land><td colspan=3>{land['name']}</td></tr>"
            
            for ride in land['rides'] :
                html += f"<tr><td>{ride['name']}</td><td>{ride['is_open']}</td><td>{ride['wait_time']}</td></tr>"
                
        html += "</table>" 
                
        return html
    except:
        return None

data = get_json_from_url('https://queue-times.com/parks/6/queue_times.json')
res = convert_json_to_htmltable(data)
print(res)
