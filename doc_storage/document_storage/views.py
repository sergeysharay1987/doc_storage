from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from document_storage.models import Document
from document_storage.forms import CreateDocForm, UpdateDocForm
from django.contrib import messages


# Create your views here.


def index_page(request):
    if request.method == 'GET':
        return render(request, 'document_storage/index_page.html')


class CreateDocumentView(CreateView):
    model = Document
    template_name = 'create_document.html'
    form_class = CreateDocForm
    success_url = reverse_lazy('create_document')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'New document is created.')
        return super().form_valid(form)


class ReadDocumentView(DetailView):
    model = Document
    template_name = 'details_document_page.html'
    context_object_name = 'doc'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Details of document'
        return context


class UpdateDocument(UpdateView):
    model = Document
    template_name = 'update_document_page.html'
    form_class = UpdateDocForm
    context_object_name = 'doc'

    def get_success_url(self):
        return reverse_lazy('update_document', kwargs={'pk': self.object.pk})

    def form_valid(self, form: UpdateDocForm):

        if form.has_changed():
            messages.success(self.request, 'Document has updated successfully.')
            return super().form_valid(form)
        else:
            messages.warning(self.request, 'Such document has already exist.')
            pass

        # self.success_url = reverse_lazy('update_document', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        return super().form_invalid(form)


class ListDocument(ListView):
    model = Document
    template_name = 'list_document_page.html'
    context_object_name = 'docs'


class ListVersionDocument(ListView):
    model = Document
    template_name = 'list_versions_of_document_page.html'
    context_object_name = 'docs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']  # use to return to details document page
        context['title'] = 'List of all versions of documents'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.kwargs['pk'])
        document = queryset.get(id=self.kwargs['pk'])
        return document.history.all()


class ListFirstLastVersions(ListView):
    model = Document
    template_name = 'first and current versions of document.html'
    context_object_name = 'versions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        document = Document.objects.get(id=self.kwargs['pk'])
        first_version = document.history.first()
        current_version = document.history.last()
        first_version = {'name': first_version.name, 'content': first_version.content}
        current_version = {'name': current_version.name, 'content': current_version.content}
        context['pk'] = self.kwargs['pk']  # use to return to details document page
        context['versions'] = {'first version': first_version, 'current version': current_version}
        context['title'] = 'First and current versions of document'
        return context


def show_doc(request):
    doc = Document.objects.get(id=id)
    context = {'doc': doc}
    if request.method == 'GET':
        return render(request, 'document_storage/index_page.html', context)


def edit_doc(request, id):
    doc = Document.objects.get(id=id)
    context = {'doc': doc}
    if request.method == 'GET':
        return render(request, 'document_storage/update_document_page.html', context)
