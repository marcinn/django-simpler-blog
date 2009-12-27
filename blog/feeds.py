from django.contrib.syndication.feeds import Feed
from models import Entry
from django.conf import settings

class LatestEntries(Feed):
    title = getattr(settings, 'BLOG_TITLE', 'Your blog entries')
    link = "/"
    description = getattr(settings, 'BLOG_SUBTITLE', 'Your blog description')

    def items(self):
        return Entry.public.order_by('-published')[:5]
