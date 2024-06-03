from django.core.exceptions import ValidationError
import re

def validate_youtube_link(value):
    youtube_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$'
    )
    if not youtube_regex.match(value):
        raise ValidationError("Only YouTube links are allowed.")
