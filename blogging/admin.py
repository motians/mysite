from django.contrib import admin
from blogging.models import Post, Category


class PostsInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostsInline
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
