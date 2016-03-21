# -*- coding: utf-8 -*-

from scrapy.pipelines.images import ImagesPipeline
import re
#from scrapy.http import Request

class OotsdwPipeline(ImagesPipeline):

    regex_name = re.compile('.*?(?P<name>[0-9]{1,4})\.(?P<ext>png|gif|jpg|jpeg).*?')

    @classmethod
    def file_path(self, request, response=None, info=None):
        name = self.regex_name.match(str(request))
        return 'full/{0:04d}.jpg'.format(int(str(name.group('name'))))
