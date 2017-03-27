from newspaper import Article


def get_article_content(url_list):
    article_tuples = list()

    for url in url_list:
        article = Article(url)
        article.download()
        article.parse()
        article_tuple = (article.title, article.text)
        article_tuples.append(article_tuple)

    return article_tuples
