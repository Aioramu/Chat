import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Chat,Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("conn")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name



        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.all_mes()

    def all_mes(self):
        chats=Chat.objects.all()
        for chat in chats:
            if chat.token==self.room_name:
                m=chat.message.all()
                for message in m:
                    #self.receive(json.dumps({"message":message.content}))
                    self.send(text_data=json.dumps({
                        'message': message.content
                    }))
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message = text_data_json['message']
        chats=Chat.objects.all()
        for chat in chats:
            if chat.token==self.room_name:
                chat.message.create(content=message)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
