import requests 
import json

def format_date(timestamp_object):
    from datetime import datetime
    datetime_object = datetime.fromtimestamp(timestamp_object)
    return str(datetime_object)

def get_data(url):
    response = requests.get(url, headers = {'User-agent': 'your bot is 0.1'})
    python_object = json.loads(response.text)
    news = python_object['data']['children']
    filter_data = []
    number = 1
    for new in news:
        news_data = {
            f'The number of new is {number}' : {
                'title': new['data']['title'],
                'author' : new['data']['author'],
                'created' : format_date(new['data']['created'])
            }
        }

        filter_data.append(news_data)
        number += 1
    return filter_data
    # print(news)

def write_to_json(data):
    with open('RedditNews.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

def main(url):
    data = get_data(url)
    # print(data)
    write_to_json(data)

# main('https://www.reddit.com/r/entertainment/.json')
main('https://www.reddit.com/r/travel/.json')















