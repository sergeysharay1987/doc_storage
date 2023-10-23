from django.contrib import admin
from document_storage.models import Document
from simple_history.admin import SimpleHistoryAdmin


class DocumentAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name', 'description')
    history_list_display = ('description', )


admin.site.register(Document, DocumentAdmin)
