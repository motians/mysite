from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "Get the latest Posts"
    link = "/latest/feed"
    description = "Updates on changes and additions to all the Posts."

    def items(self):
        return Post.objects.order_by('-modified_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return f'/posts/{int(item.id)}/'
