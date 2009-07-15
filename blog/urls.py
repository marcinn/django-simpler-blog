from django.conf.urls.defaults import *
from django.conf import settings
from models import Entry
from views import preview, post_comment
from feeds import LatestEntries

urlpatterns = patterns('',
                       url(r'^admin/blog/entry/(?P<object_id>\d+)/preview/$', preview),
                       url(r'^feed/(?P<url>.*)/?$', 'django.contrib.syndication.views.feed', {'feed_dict': {'latest': LatestEntries}}, name='blog-feed'),
                       url(r'^comments/post/$', post_comment, name='comments-post-comment'),
                       )

urlpatterns += patterns('django.views.generic',
                        url('^$', 'list_detail.object_list', dict(queryset=Entry.public.order_by('-published'), paginate_by=getattr(settings, 'SET_DETAILS_ENTRIES_PER_PAGE', 5)), name='blog-index'),
                        url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[\w\-]+)/?$',
                            'date_based.object_detail', dict(queryset=Entry.public.all(), date_field='published'), name='blog-entry'),
)

