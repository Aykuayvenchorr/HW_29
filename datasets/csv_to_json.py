import csv
import json

ADS = 'ad'
CATEGORY = 'category'
USER = 'user'
LOCATION = 'location'


def convert_file(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {'model': model, 'pk': int(row['id'] if 'id' in row else row['Id'])}
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'is_published' in row:
                row['is_published'] = bool(row['is_published'].lower())
            if 'price' in row:
                row['price'] = int(row['price'])
            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']

            to_add['fields'] = row
            result.append(to_add)
    with open(json_file, 'w', encoding='utf-8') as js_file:
        js_file.write(json.dumps(result, ensure_ascii=False))


convert_file(f"{ADS}.csv", f"{ADS}.json", "ads.ad")
convert_file(f"{CATEGORY}.csv", f"{CATEGORY}.json", "ads.category")
convert_file(f"{USER}.csv", f"{USER}.json", "user.user")
convert_file(f"{LOCATION}.csv", f"{LOCATION}.json", "user.location")



