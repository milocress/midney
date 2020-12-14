from rest_framework import serializers
from mood.models import Thinker, Mood

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['mood', 'created']

class ThinkerSerializer(serializers.ModelSerializer):
    moods = MoodSerializer(many=True, read_only=True)

    class Meta:
        model = Thinker
        fields = ['name', 'moods']
