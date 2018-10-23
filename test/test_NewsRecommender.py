from unittest import TestCase
from tvnews import ArticleExtraction, NewsRecommender

class TestNewsRecommender(TestCase):
    good_url = "https://www.huffingtonpost.com/entry/alex-jones-infowars-app-apple-google_us_5b694ec3e4b0de86f4a4bc1d"
    bad_url = "https://www.huffingtonpost.com/"
    urlencode_url = "https://www.vox.com/policy-and-politics/2018/9/24/17157194/rosenstein-trump-mueller-fired-doj-fbi"
    def test_makeRecommendations_json_response(self):
        article = ArticleExtraction.extract(ArticleExtraction.getHTML(self.good_url))
        clips = NewsRecommender.makeRecommendations(article)
        for clip in clips:
            self.assertTrue(clip.get("preview_url"))
            self.assertTrue(clip.get("similarity"))
            self.assertTrue(clip.get("show"))

    def test_makeRecommendations_using_urlencoding(self):
        article = ArticleExtraction.extract(ArticleExtraction.getHTML(self.urlencode_url))
        clips = NewsRecommender.makeRecommendations(article)
        for clip in clips:
            self.assertTrue(clip.get("preview_url"))
            self.assertTrue(clip.get("similarity"))
            self.assertTrue(clip.get("show"))


    def test_makeRecommendations_sort(self):
        article = ArticleExtraction.extract(ArticleExtraction.getHTML(self.good_url))
        clips = NewsRecommender.makeRecommendations(article)
        for i in range(len(clips)-1):
            self.assertTrue(clips[i].get("similarity") <= clips[i+1].get("similarity"))

    def test_getSearchQuery(self):
        article = ArticleExtraction.extract(ArticleExtraction.getHTML(self.good_url))
        entities = NewsRecommender.extractEntities(article)
        query = NewsRecommender.getSearchQuery(entities)
        self.assertTrue(len(query) == 3)
