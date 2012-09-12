# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from stories.models import Story

class StoryPipeline(object):

    def process_item(self, item, spider):        

	
	election_list = ['paul ryan','biden','election','obama','romney','clinton','election 2012']

	if any(word in item['description'] for word in election_list):
		item.save()
        return item
