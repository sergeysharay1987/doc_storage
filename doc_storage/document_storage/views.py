from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView
from .models import Document
from .forms import CreateDocForm
from django.contrib import messages


class IndexPageView(TemplateView):
    template_name = 'document_storage/index_page.html'


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
    form_class = CreateDocForm
    context_object_name = 'doc'

    def get_success_url(self):
        return reverse_lazy('update_document', kwargs={'pk': self.object.pk})

    def form_valid(self, form: CreateDocForm):

        if form.has_changed():
            messages.success(self.request, 'Document has updated successfully.')
            return super().form_valid(form)
        else:
            messages.warning(self.request, 'You have not updated your data.')
            return redirect(self.get_success_url())


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
        return super().get_queryset().get(id=self.kwargs['pk']).history.all()


class ListFirstLastVersions(DetailView):
    model = Document
    template_name = 'first_and_current_versions_of_document.html'
    context_object_name = 'doc'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        document = get_object_or_404(Document, id=self.kwargs['pk'])
        first = document.history.first()
        current = document.history.last()
        delta = first.diff_against(current)
        context['delta'] = delta
        context['pk'] = self.kwargs['pk']  # use to return to details document page
        context['title'] = 'Differences between first and current versions of document'
        return context
