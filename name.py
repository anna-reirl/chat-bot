import apiai
import json

def send_message(message):
    request=apiai.ApiAI('efc7ba0fb31e45be9a94ba9cf4631599').text_request()
    request.lang='en'
    request.session_id='session_id'
    request.query=message
    response=json.loads(request.getresponse().read().decode('utf-8'))
    print(response['result']['fulfillment']['speech'])
    print(response)
print('Input your message')
message=input()
while message!='exit':
    send_message(message)
    message=input()


