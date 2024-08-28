from flask import Flask, render_template
import requests

app = Flask(__name__)

# API 키 및 도메인 설정
api_key = 'nbNrD0KMA2IREIQPuCg'
domain = '11st'
url = f'https://{domain}.freshservice.com/api/v2/assets'

def fetch_assets():
    all_assets = []
    page = 1
    per_page = 100
    include_type_fields = True

    while True:
        params = {
            'page': page,
            'per_page': per_page,
            'order_by': 'created_at',
            'order_type': 'desc'
        }
        if include_type_fields:
            params['include'] = 'type_fields'
        
        response = requests.get(url, auth=(api_key, 'X'), params=params)
        
        if response.status_code == 200:
            assets = response.json()
            all_assets.extend(assets['assets'])
            
            if len(assets['assets']) < per_page:
                break
            page += 1
        else:
            break
    
    return all_assets

@app.route('/')
def index():
    assets = fetch_assets()
    return render_template('index.html', assets=assets)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)