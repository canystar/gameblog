from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from django.views.generic import FormView, CreateView, DeleteView

from django.urls import reverse_lazy

from .forms import ContactForm, GamePostForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.core.mail import EmailMessage

from .models import GamePost

class IndexView(TemplateView):
    template_name='index.html'
    
class LoginView(TemplateView):
    template_name='login.html'
    
class ContactView(FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('gamelog:contact')
    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject='お問い合わせ:{}'.format(title)
        message=\
            '送信者名:{0}\nメールアドレス:{1}\n タイトル:{2}\n メッセージ:\n{3}' \
                .format(name, email, title, message)
        from_email='admin@example.com'
        to_list=['admin@example.com']
        message=EmailMessage(subject=subject,
                             body=message,
                             from_email=from_email,
                             to=to_list,
                             )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました'
        )
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class CreateGamelogView(CreateView):
    form_class=GamePostForm
    template_name="post_game.html"
    success_url=reverse_lazy('gamelog:post_done')
    
    def form_valid(self, form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name='post_success.html'
    
class ContentView(ListView):
    
    template_name='content.html'
    queryset=GamePost.objects.order_by('-posted_at')
    paginate_by=5

class CategoryView(ListView):
    template_name='content.html'
    paginate_by=5
    def get_queryset(self):
        category_id=self.kwargs['Category']
        categories=GamePost.objects.filter(
            Category=category_id).order_by('-posted_at')
        return categories
    
class UserView(ListView):
    template_name='content.html'
    paginate_by=5
    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list=GamePost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list
    
class DetailView(DetailView):
    template_name='detail.html'
    model=GamePost
    
class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=5
    
    def get_queryset(self):
        queryset=GamePost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset
    
class GameDeleteView(DeleteView):
    model=GamePost
    template_name='game_delete.html'
    success_url=reverse_lazy('gamelog:mypage')
    def delete(self, request,*args,**kwargs):
        return super().delete(request,*args, **kwargs)