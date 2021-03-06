# Scrapy settings for elections2012 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

def setup_django_env(path):
    import imp, os
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)       

    setup_environ(project)

setup_django_env('/home/tuva/webapps/muhtasari_demo/muhtasari_demo/muhtasari_demo')
#setup_django_env('/home/tuva/webapps/muhtasari_prod/muhtasari')

BOT_NAME = 'elections2012'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['elections2012.spiders']
NEWSPIDER_MODULE = 'elections2012.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'elections2012.pipelines.StoryPipeline',
]
