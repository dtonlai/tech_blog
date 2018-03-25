from django.contrib import admin
from blog_app.models import BlogPost, UserProfileInfo, BlogPostComment

admin.site.register(BlogPost)
admin.site.register(BlogPostComment)
admin.site.register(UserProfileInfo)

#-blogadmin -admin@gmail.com -adminpassword
