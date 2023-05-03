from django.contrib import admin
from document_storage.models import Document
from simple_history.admin import SimpleHistoryAdmin


class DocumentAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'name', 'content')
    list_display_links = ('name', 'content')
    history_list_display = ('content', )


admin.site.register(Document, DocumentAdmin)
