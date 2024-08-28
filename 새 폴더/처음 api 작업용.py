import requests

# API 키 및 도메인 설정
api_key = 'nbNrD0KMA2IREIQPuCg'
domain = '11st'
url = f'https://{domain}.freshservice.com/api/v2/assets'

# 초기 설정
all_assets = []
page = 1
per_page = 100  # 페이지당 요청할 자산 수
include_type_fields = True  # 자산 유형 필드를 포함할지 여부

# 자산 데이터 가져오기
while True:
    # API 호출
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
        
        # 가져온 자산 데이터를 전체 리스트에 추가
        all_assets.extend(assets['assets'])
        
        print(f"Page {page}: {len(assets['assets'])} assets fetched.")
        
        # 다음 페이지로 이동
        page += 1
        
        # 페이지에 데이터가 더 이상 없으면 반복 종료
        if len(assets['assets']) < per_page:
            print("All assets have been fetched.")
            break
    else:
        print(f"Failed to fetch data: {response.status_code}")
        break

# 전체 자산 데이터 출력 (갯수 확인)
print(f"Total assets fetched: {len(all_assets)}")

for asset in all_assets:
    print(f"Name: {asset['name']}, Asset Tag: {asset['asset_tag']}")
