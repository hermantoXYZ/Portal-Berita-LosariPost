from django.contrib import admin
from django.db import models
from .models import UserAdmin, UserAnggota, Article, Category, Page, Topic
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .admin_resources import UserAnggotaResource

# Resource untuk Topic
class TopicResource(resources.ModelResource):
    class Meta:
        model = Topic
        fields = ('name', 'slug')
        import_id_fields = ('name',) 

# Admin dengan import/export
@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    resource_class = TopicResource
    list_display = ('name', 'slug')
    search_fields = ('name',)


class UserAnggotaImport(ImportExportModelAdmin):
    resource_class = UserAnggotaResource  # Import User DOSEN

admin.site.register(UserAnggota)
admin.site.register(UserAdmin)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Page)
