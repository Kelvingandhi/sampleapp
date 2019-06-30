import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import subprocess

# Load Firebase configuration from environment
#credent = credentials.Certificate('C:\\Users\\Kelvin\\Downloads\\firebase_key.json')
#credent = credentials.Certificate('C:\\Users\\Kelvin\\Downloads\\wowza_firebase_key.json')
credent = credentials.Certificate('C:\\Users\\Kelvin\\Downloads\\Firebase Key Files\\thermalimaging-firebase.json')
my_app = firebase_admin.initialize_app(credent)

#print(my_app.name)

message = messaging.Message(

    #data={
     #   "image_url" = "http://leanport.com/wp-content/uploads/2017/03/20151123175709661.jpg"
    #},

    data={'title':'Flame is on',
        'body':'Please turn it off or call emergency',
        }
        ,
    
    notification=messaging.Notification(
        title='Flame is on',
        body='Please turn it off or call emergency'),
        
    topic = 'Emergency'

)

response = messaging.send(message)
print("Message sent succssfully: ", response)

