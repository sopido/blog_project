from django.contrib import admin
from bloggers.models import Blogger
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'blogger', 'likes_count','comments_count','post_date','is_published')
    list_display_links=['id','title']
    list_editable=['is_published']
    list_filter=['blogger']
    search_fields = ['title','text','blogger__name']
    readonly_fields= [ 'likes_count','comments_count','blogger']
    list_per_page = 10
    

    #link post to login user 
    def save_model(self, request, obj, form, change) -> None:
        obj.blogger = Blogger.objects.filter(user=request.user).first()
        return super().save_model(request, obj, form, change)
    #every one just see him posts
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        #for super user can see any thing
        return qs.filter(blogger__user =request.user)

admin.site.register(Post, PostAdmin)

