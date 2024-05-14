import re
from rest_framework import serializers

def youtube_link_validator(value):
    if not re.match(r'^https:\/\/(?:www\.)?youtube\.com\/watch\?v=[\w-]+$', value):
        raise serializers.ValidationError("Only YouTube links are allowed.")
