from django.utils.text import slugify 
import string
import random

""" To ensure slugs don't overlap we change slug if that is already present"""
def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res


""" A slug is generated to give meaningful url """
def generate_slug(text):
    new_slug=slugify(text)
    from blogs.models import BlogModel
    if BlogModel.objects.filter(slug=new_slug).first():
        return generate_slug(text + generate_random_string(5))
    
    return new_slug