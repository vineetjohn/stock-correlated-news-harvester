import json

from newspaper import Article

sample_url_list = \
 ['http://www.inc.com/jeff-bercovici/apple-becoming-blackberry.html',
  'http://business.financialpost.com/fp-tech-desk/blackberry-ltd-is-working-with-google-inc-to-secure-android-devices',
  'http://business.financialpost.com/midas-letter/apple-incs-smartphone-business-model-is-blackberry-ltds-opportunity',
  'http://www.fool.ca/2016/03/25/should-blackberry-ltd-be-disappointed-to-be-dumped-by-facebook-inc/',
  'http://www.fool.ca/2016/02/03/alphabet-inc-and-blackberry-ltd-a-perfect-match-for-growth/',
  'http://www.fool.ca/2016/09/23/will-blackberry-inc-release-a-new-flagship-device-this-year/',
  'https://www.benzinga.com/trading-ideas/long-ideas/16/03/7749928/facebook-and-its-messenger-app-are-leaving-blackberry',
  'http://business.financialpost.com/fp-tech-desk/apple-inc-hires-former-blackberry-ltd-head-and-ex-ceo-of-qnx-as-car-project-shifts-to-self-driving-software-sources',
  'http://business.financialpost.com/investing/blackberry-ltd-sierra-wireless-inc-among-canadian-tech-firms-that-face-labour-shortage-risk-report',
  'https://www.fool.com/investing/general/2015/12/18/carmax-inc-drops-and-blackberry-ltd-jumps-as-stock.aspx',
  'http://www.fool.com/investing/2016/05/24/is-apple-inc-the-next-blackberry-fiasco.aspx',
  'http://www.profitconfidential.com/stock/aapl-stock-is-apple-inc-the-next-blackberry/',
  'http://learnbonds.com/127703/facebook-inc-fb-whatsapp-dont-care-about-blackberry-ltd-bbry/',
  'http://www.valuewalk.com/2016/07/apple-hires-blackberry-exec-car/']


article_dict = dict()
for url in sample_url_list:
    article = Article(url)
    article.download()
    article.parse()

    article_dict[article.title] = article.text

print(json.dumps(article_dict))
