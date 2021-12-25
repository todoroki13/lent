from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import LogItems, LogPerson, LogType, LogBorrow
from django.contrib.auth.mixins import LoginRequiredMixin

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
  
  def get_success_url(self):
    return "/log/{}/".format(self.object.id)

class LogUpdatet(UpdateView):
  model = LogType
  fields = ['type', 'buydate', 'detail']
  
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

  def get_success_url(self):
    return "/log/item/{}".format(self.object.borrowsl.id) 

class LogCreatebs(CreateView):
  model = LogBorrow
  # 新增時只顯示需填寫的部份欄位
  fields = ['borrowps', 'borrowdt']

  def form_valid(self, form):
    form.instance.borrowsl = LogItems.objects.get(id=self.kwargs['aid'])
    return super().form_valid(form)

  def get_success_url(self):
    return "/log/item/{}".format(self.object.borrowsl.id) 

class LogCreatebp(CreateView):
  model = LogBorrow
  # 新增時只顯示需填寫的部份欄位
  fields = ['borrowsl', 'borrowdt']

  def form_valid(self, form):
    form.instance.borrowps = LogPerson.objects.get(id=self.kwargs['eid'])
    return super().form_valid(form)

  def get_success_url(self):
    return "/log/item/{}".format(self.object.borrowsl.id)  

class LogUpdateb(UpdateView):
  model = LogBorrow
  fields = ['borrowsl', 'borrowps', 'borrowdt', 'backdt']
  
  def get_success_url(self):
    return "/log/item/{}/".format(self.object.borrowsl.id)

class LogDeleteb(DeleteView):
  model = LogBorrow

  def get_success_url(self):
    return "/log/item/{}/".format(self.object.borrowsl.id)