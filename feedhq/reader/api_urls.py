from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^token$', views.token, name='token'),

    url(r'^user-info$', views.user_info, name='user_info'),

    url(r'^unread-count$', views.unread_count, name='unread_count'),

    url(r'^subscription/list$', views.subscription_list,
        name='subscription_list'),

    url(r'^subscription/edit$', views.edit_subscription,
        name='subscription_edit'),

    url(r'^subscription/quickadd$', views.quickadd_subscription,
        name='subscription_quickadd'),

    url(r'^subscribed$', views.subscribed, name='subscribed'),

    url(r'^stream/contents/(?P<content_id>.+)?$', views.stream_contents,
        name='stream_contents'),

    url(r'^stream/items/ids$', views.stream_items_ids,
        name='stream_items_ids'),

    url(r'^stream/items/count$', views.stream_items_count,
        name='stream_items_count'),

    url(r'^stream/items/contents$', views.stream_items_contents,
        name='stream_items_contents'),

    url(r'^tag/list$', views.tag_list,
        name='tag_list'),

    url(r'^edit-tag$', views.edit_tag,
        name='edit_tag'),

    url(r'^mark-all-as-read$', views.mark_all_as_read,
        name='mark_all_as_read'),

    # Dummy prefs
    url(r'^preference/list$', views.preference_list, name='preference_list'),

    url(r'^preference/stream/list$', views.stream_preference,
        name='stream_preference'),
)

"""
Missing URLS:

    subscription/
        export

    /disable-tag
    /rename-tag
    /related/list

    /stream
        /details

    /item
        /edit
        /delete
        /likers

    /friend
        /groups
        /acl
        /edit
        /list
        /feeds

    /people
        /search
        /suggested
        /profile

    /comment/edit
    /conversation/edit
    /shorten-url

    /preference
        /set
        /stream/set

    /search/items/ids

    /recommendation
        /edit
        /list

    /list-user-bundle
    /edit-bundle
    /get-bundle
    /delete-bundle
    /bundles
    /list-friends-bundle
    /list-featured-bundle
"""
