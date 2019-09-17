from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings

import datetime
import json


class ChatConsumer(WebsocketConsumer):


    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        me = self.scope['user']
        self.room_group_name = ("chat_", self.room_name)
        print("WSconnect:: ", me, " connected to websocket in room:", self.room_name)
        print(self.room_group_name)

        # async_to_sync(self.channel_layer.group_add)(
        # self.room_name, self.channel_name)

        # if self.scope['user'].is_anonymous:
        #     self.close()
        # else:
        self.accept()







    def disconnect(self, close_code):
        # async_to_sync(self.channel_layer.group_discard)(
        # self.room_group_name, self.channel_name)
        pass


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = str(self.scope['user'])
        now_time = datetime.datetime.now().strftime(settings.DATETIME_FORMAT)
        #
        # context = {
        #     'username': username
        # }
        # self.send(text_data=json.dumps({
        #     "type": "chat_message",
        #     'message': message,
        #     "text": json.dumps(context),
        #     'now_time': now_time
        # }))

        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        #
        self.send(text_data=json.dumps({
            'message': message,
            'now_time': now_time,
        }))
        self.send(text_data="Hello!")
        # new_event = {
        #     "type": "chat_message",
            # "type": "websocket.send",
            # "text": json.dumps(context),
        #     "username": username,
        #     "message": message
        # }
        # self.channel_layer.group_send(
        #     self.room_name,
        #     new_event

        # )
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name, {
        #         "type": "chat_message",
        #         "username": username,
        #         "message": message
        # })

    def chat_message(self, event):
        print ('message', event)
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
        }))
