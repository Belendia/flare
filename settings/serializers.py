from rest_framework import serializers
from .models import Language, Channel
from message.serializers import MessageSerializer

class LanguageSerializer(serializers.ModelSerializer):

    messages = MessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Language
        fields = ('id', 'name', 'code', 'messages')#'__all__' #we need to see all the fields in language model
        extra_kwargs = {'messages': {'required': False}}

class ChannelSerializer(serializers.ModelSerializer):

    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Channel
        fields = ('id', 'name', 'messages')
        extra_kwargs = {'messages': {'required': False}}