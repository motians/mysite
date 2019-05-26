# Mysite

Django application for blogging and polling.

Adminmodel included in admin.py. TabularInline included in admin.py to allow category
to be added when a new post is created.

RSS feed added to url http://127.0.0.1:8000/latest/feed/. A RSS feed reader extenstion was required in the browser to render the rss xml correctly.

ModelForm used to add new post input page at url http://127.0.0.1:8000/post/add/.