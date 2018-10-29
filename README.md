# Article 2 TV News

Uses python 3.4

Article2TVNews allows users to find TV news clips on subjects related
to an article they are reading.  It provides methods to extract text from an
article and get tv news clips based on the article's subject.  This package is
written for the Internet Archive's WayBack Machine and its Context browser
extension. Typical usage looks something like this::

    #!/usr/bin/env python

    from article2tvnews import ArticleExtraction, NewsRecommender

    url = <news-article-url>
    html = ArticleExtraction.getHTML(url)
    article = ArticleExtraction.extract(html)
    for clip in NewsRecommender.makeRecommendations(article):
        print(clip)


Must include a config.json file::

    {
      "OpenCalais" : {
        "CALAIS_ENDPOINT" : "https://api.thomsonreuters.com/permid/calais",
        "CALAIS_HEADER" : {
          "X-AG-Access-Token" : <OPEN_CALAIS_TOKEN>,
          "Content-Type" : "text/raw",
          "outputformat" : "application/json"
        }
      },
      "GDELT" : {
        "GDELT_HEADER" : {
          "Content-Type" : "application/json",
          "outputformat" : "application/json"
        }
      }
    }


## Possible Changes:
- Time period for videos
- extract embedded tweets (possible added weight)


## Thanks


Thanks to the wonderful people at *The Internet Archive* for giving me this
opportunity, and a special thanks to:

* Mark

* Dvd

* Vangelis

* Anish

* And of course, Brewster Kahle
