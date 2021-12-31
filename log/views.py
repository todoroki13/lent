from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import LogItems, LogPerson, LogType, LogBorrow
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

def style(request):
  return render(request, 'base.html')

# Create your views here.
class LogListt(ListView):
  model = LogType
  ordering = ['-id']
  paginate_by = 15

class LogViewt(DetailView):
  model = LogType

  # def get_context_data(self, **kwargs):
  #   ctx = super().get_context_data(**kwargs)
  #   ctx['logitems_list'] = LogItems.objects.filter(itemtype = self.kwargs['pk'])
  #   return ctx
  def get_object(self):
    logtype = super().get_object()
    logtype.save()
    return logtype

class LogCreatet(CreateView):
  model = LogType
  # 新增時只顯示需填寫的部份欄位
  fields = ['type', 'buydate', 'detail']
  
  def get_form(self):
    form = super().get_form()   # 取得原本的表單定義
    date_fields = ['buydate']    # 要修改的欄位名稱
    for field in date_fields:
        # form.fields[field] 就是表單上的欄位
        # .widget 是用來描述它在頁面上的樣子
        # 改用 forms.DateInput 元件來取代預設的 forms.TextInput 元件
        # attrs 裡指定的屬性，最終會變成 render 後的 HTML 元素的屬性，以此例來說：
        # 這個欄位最終輸出的 HTML 碼應該會變這樣: <input type="date">
        form.fields[field].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    return form

  def get_success_url(self):
    return "/log/{}/".format(self.object.id)

class LogUpdatet(UpdateView):
  model = LogType
  fields = ['type', 'buydate', 'detail']

  
  def get_form(self):
    form = super().get_form()
    date_fields = ['buydate']
    for field in date_fields:
        form.fields[field].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    return form
  
  def get_success_url(self):
    return "/log/{}/".format(self.object.id)

class LogDeletet(DeleteView):
  model = LogType
  success_url = '/log/'

#--------------------------
class LogListp(ListView):
  model = LogPerson
  ordering = ['-id']
  paginate_by = 15

class LogViewp(DetailView):
  model = LogPerson

class LogCreatep(CreateView):
  model = LogPerson
  # 新增時只顯示需填寫的部份欄位
  fields = ['subject', 'status', 'department', 'title', 'phone', 'mail', 'isatwork']

  def get_success_url(self):
    return "/log/person/{}/".format(self.object.id)
    
  def get_object(self):
    logperson = super().get_object()
    logperson.save()
    return logperson

class LogUpdatep(UpdateView):
  model = LogPerson
  fields = ['subject', 'status', 'department', 'title', 'phone', 'mail', 'isatwork']
  
  def get_success_url(self):
    return "/log/person/{}/".format(self.object.id)

class LogDeletep(DeleteView):
  model = LogPerson
  success_url = '/log/person'

#--------------------------
class LogViewi(DetailView):
  model = LogItems

class LogCreatei(CreateView):
  model = LogItems
  # 新增時只顯示需填寫的部份欄位
  fields = ['serial', 'itemtype', 'tenure', 'remark', 'eqpst']

  def get_success_url(self):
    return "/log/item/{}/".format(self.object.id) 
    
  def get_object(self):
    logitems = super().get_object()
    logitems.save()
    return logitems

class LogCreateisl(CreateView):
  model = LogItems
  # 新增時只顯示需填寫的部份欄位
  fields = ['serial', 'tenure', 'remark', 'eqpst']

  def form_valid(self, form):
    form.instance.itemtype = LogType.objects.get(id=self.kwargs['iid'])
    return super().form_valid(form)

  def get_success_url(self):
    return "/log/item/{}/".format(self.object.id) 
    
  def get_object(self):
    logitems = super().get_object()
    logitems.save()
    return logitems

class LogUpdatei(UpdateView):
  model = LogItems
  fields = ['serial', 'itemtype', 'tenure', 'remark', 'eqpst']
  
  def get_success_url(self):
    return "/log/item/{}/".format(self.object.id)

class LogDeletei(DeleteView):
  model = LogItems

  def get_success_url(self):
    return "/log/{}/".format(self.object.itemtype.id)

#--------------------------
class LogCreateb(CreateView):
  model = LogBorrow
  # 新增時只顯示需填寫的部份欄位
  fields = ['borrowsl', 'borrowps', 'borrowdt']

  def get_form(self):
    form = super().get_form()
    date_fields = ['borrowdt']
    for field in date_fields:
        form.fields[field].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    return form

  def get_success_url(self):
    return "/log/item/{}".format(self.object.borrowsl.id) 

class LogCreatebs(CreateView):
  model = LogBorrow
  # 新增時只顯示需填寫的部份欄位
  fields = ['borrowps', 'borrowdt']

  
  def get_form(self):
    form = super().get_form()
    date_fields = ['borrowdt']
    for field in date_fields:
        form.fields[field].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    return form

  def form_valid(self, form):
    form.instance.borrowsl = LogItems.objects.get(id=self.kwargs['aid'])
    return super().form_valid(form)

  def get_success_url(self):
    return "/log/item/{}".format(self.object.borrowsl.id) 

class LogCreatebp(CreateView):
  model = LogBorrow
  # 新增時只顯示需填寫的部份欄位
  fields = ['borrowsl', 'borrowdt']

  
  def get_form(self):
    form = super().get_form()
    date_fields = ['borrowdt']
    for field in date_fields:
        form.fields[field].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    return form

  def form_valid(self, form):
    form.instance.borrowps = LogPerson.objects.get(id=self.kwargs['eid'])
    return super().form_valid(form)

  def get_success_url(self):
    return "/log/item/{}".format(self.object.borrowsl.id)  

class LogUpdateb(UpdateView):
  model = LogBorrow
  fields = ['borrowsl', 'borrowps', 'borrowdt', 'backdt']

  def get_form(self):
    form = super().get_form()
    date_fields = ['borrowdt', 'backdt']
    for field in date_fields:
        form.fields[field].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    return form
  
  def get_success_url(self):
    return "/log/item/{}/".format(self.object.borrowsl.id)

class LogDeleteb(DeleteView):
  model = LogBorrow

  def get_success_url(self):
    return "/log/item/{}/".format(self.object.borrowsl.id)