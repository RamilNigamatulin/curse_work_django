from django.forms import inlineformset_factory
from django.shortcuts import render
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.contrib import messages


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_create')


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = context_data['products']

        for product in products:
            active_version = Version.objects.filter(product=product, current_sign=True).first()
            product.active_version = active_version

        return context_data


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_create')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid() and formset.is_valid():
            # Проверка на наличие только одной активной версии
            active_versions = [version for version in formset if version.cleaned_data.get('current_sign')]
            if len(active_versions) > 1:
                messages.error(self.request, 'Выберите только одну активную версию.')
                return self.render_to_response(self.get_context_data(form=form, formset=formset))

            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'