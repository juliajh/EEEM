from django.contrib import admin
from .models import newterm, communityText, communityComment, manner
# Register your models here.

admin.site.register(newterm)
admin.site.register(communityText)
admin.site.register(communityComment)
admin.site.register(manner)
