# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from stories.models import Story
from scrapy.exceptions import DropItem
from datetime import datetime, timedelta

class StoryPipeline(object):

    try:
    	last_record = Story.objects.all().order_by('-pubDate')[:1]
    except:
    	print 'Oops!  That was no valid record'

    if(len(last_record) == 0): 
    	last_run_time = datetime.now() - timedelta(hours = 24)
    else:
    	last_run_time = last_record[0].pubDate

    def process_item(self, item, spider):        
	
	election_list = ['paul ryan','biden','election','obama','romney','clinton','election 2012']
	
	if item['pubDate'] > self.last_run_time:
		if any(word in item['description'] for word in election_list):
			print 'Saved'
			item.save()
		else:
			print 'Missing Category'
			DropItem("Missing category - %s" % item)
	else:
		print 'Already Covered'
		DropItem("Already Covered in previous run - %s" % item)
        
	return item

    
