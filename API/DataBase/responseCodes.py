async def checkStatusCode(response):
    if response.status_code == 200:
        return response
    else:
        json_data = response.json()
        if 'details' in json_data:
            print('[API]: Error: '+ json_data['details']['code']+' [HTTP code '+str(response.status_code)+']')
            return None