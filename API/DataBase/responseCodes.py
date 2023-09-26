async def checkStatusCode(response):
    if response.status_code == 200:
        return response
    
    if response.status_code == 400:
        if response.content:
            if response.json()['error'].startswith('Користувача'):
                print('[API]: User not found (400)')
            
    return None