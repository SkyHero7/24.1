from django.core.exceptions import ValidationError
import re

def validate_youtube_url(value):
    if not re.match(r'^https?://(www\.)?youtube\.com/', value):
        raise ValidationError("Only YouTube URLs are allowed.")
