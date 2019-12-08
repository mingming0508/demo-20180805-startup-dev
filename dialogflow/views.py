from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from . import actions
from django.http import JsonResponse
from .actions import save_location

def index(request):
    return render(request, 'dialogflow/index.html', {
        'WEB_DEMO_URL': settings.DIALOGFLOW['WEB_DEMO_URL'],
    })


@require_POST
@csrf_exempt
def fulfillment(request):
    print('start')
    # intent_name = request.JSON['result']['metadata']['intentName']
    try:
        action_name = request.JSON['queryResult']['action'].replace('-', '_')
        params = request.JSON['queryResult']['parameters']
    except:
        print(request.JSON)
    print(request.JSON)

    action = getattr(actions, action_name, None)
    print("action: ", action)
    print('params: ', params)
    print('action_name: ', action_name)
    
    if(action_name == 'find_location' or action_name == 'location_term'):
        print('-------------------------------------------------')
        queryText = request.JSON['queryResult']['queryText']
        response = {'fulfillmentText': save_location(queryText)}
        print('response: ', response)
        
        return response
        
                
    if callable(action):
        response = action(**params)
    else:
        response = {
            'speech': '제가 처리할 수 없는 부분입니다.',
        }
        
    response['fulfillmentText'] = response.pop('speech')
    print('response: ', response)
    return response

