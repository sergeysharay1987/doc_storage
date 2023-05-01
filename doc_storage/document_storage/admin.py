from django.contrib import admin
from document_storage.models import Document, HistoricalRecords
from simple_history.admin import SimpleHistoryAdmin


# Register your models here.

class DocumentAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'name', 'content')
    list_display_links = ('name', 'content')
    history_list_display = ('content',)


admin.site.register(Document, DocumentAdmin)
