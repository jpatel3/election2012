# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.contrib_exp.djangoitem import DjangoItem
from stories.models import Story
from scrapy.item import Item, Field
from datetime import datetime

class StoryItem(DjangoItem):
    django_model = Story

#class StoryItem2(DjangoItem):
#    django_model = Story
#    created = Field(default=datetime.now())
#    source = Field(default='BBC')
#    pubDate = Field(default=datetime.now())
