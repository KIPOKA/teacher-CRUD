from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm
from classroom.models import Teacher
# Create your views here.


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    # success URL
    success_url = reverse_lazy("classroom:thank_you")
    # what to do with the  form

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# class TeacherListView(ListView):
#     model = Teacher
class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"  # ['first_name', 'last_name', 'age', 'subject']
    success_url = reverse_lazy('classroom:teacher_list')


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')
