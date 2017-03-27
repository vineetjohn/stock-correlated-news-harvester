import json

from utils.article_parse_helper import get_article_content

sample_url_list = \
 ['http://www.inc.com/jeff-bercovici/apple-becoming-blackberry.html',
  'http://business.financialpost.com/fp-tech-desk/blackberry-ltd-is-working-with-google-inc-to-secure-android-devices',
  'http://www.valuewalk.com/2016/07/apple-hires-blackberry-exec-car/']


articles = get_article_content(sample_url_list)
print(json.dumps(articles))
