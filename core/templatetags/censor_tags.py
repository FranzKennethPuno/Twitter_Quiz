# myapp/templatetags/censor_tags.py
from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter(name='censor_usernames')
@stringfilter
def censor_usernames(value, usernames):
    """
    Censors specified usernames in the given text by replacing them with asterisks.

    Args:
        value (str): The text where usernames will be censored.
        usernames (str): A comma-separated list of usernames to be censored.

    Returns:
        str: The text with censored usernames.
    """
    usernames_to_censor = [username.strip() for username in usernames.split(',')]
    for username in usernames_to_censor:
        # Create a regex pattern to match the username
        pattern = r'\b' + re.escape(username) + r'\b'
        value = re.sub(pattern, '*' * len(username), value, flags=re.IGNORECASE)
    return value