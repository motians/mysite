# Mysite

Django application for blogging and polling.

Adminmodel included in admin.py. TabularInline included in admin.py to allow category
to be added when a new post is created.

RSS feed added to url http://127.0.0.1:8000/latest/feed/. A RSS feed reader extenstion was required in the browser to render the rss xml correctly. File rsspostfeed.py contains class LatestEntriesFeed to implement RSS.

ModelForm used to add new post input page at url http://127.0.0.1:8000/post/add/. Modelform added in forms.py file. Template postadd.html added with view function add_model. Published date automatically set to current time so post will be in published state when Submit button pressed.