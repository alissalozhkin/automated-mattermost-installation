import json

with open('/opt/mattermost/config/config.json', 'r') as f:
    json_data = json.load(f)
    json_data["ServiceSettings"]["SiteURL"] = "http://localhost:8065"
    json_data["ServiceSettings"]["ListenAddress"] = "localhost:8065"
    json_data["SqlSettings"]["DriverName"] = "postgres"
    json_data["SqlSettings"]["DataSource"] = "postgres://<username>:<password>@localhost:5432/mattermost?sslmode=disable\u0026connect_timeout=10"


with open('/opt/mattermost/config/config.json', 'w') as f:
    f.write(json.dumps(json_data))