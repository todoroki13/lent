from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import LogItems, LogPerson, LogType, LogBorrow
from django.contrib.auth.mixins import LoginRequiredMixin
 

# Create your views here.
class LogListt(ListView):
  model = LogType
  ordering = ['-id']

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

#--------------------------
class LogListp(ListView):
  model = LogPerson
  ordering = ['-id']

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

#--------------------------
class LogCreateb(CreateView):
  model = LogBorrow
  # 新增時只顯示需填寫的部份欄位
  fields = ['borrowsl', 'borrowps', 'borrowdt', 'backdt']

  def get_success_url(self):
    return "/log/".format(self.object.id) 

#--------------------------
class LogCreatebs(CreateView):
  model = LogBorrow
  # 新增時只顯示需填寫的部份欄位
  fields = ['borrowps', 'borrowdt', 'backdt']

  def form_valid(self, form):
    form.instance.borrowsl = LogItems.objects.get(id=self.kwargs['aid'])
    return super().form_valid(form)

  def get_success_url(self):
    return "/log/".format(self.object.id) 

#--------------------------
class LogCreatebp(CreateView):
  model = LogBorrow
  # 新增時只顯示需填寫的部份欄位
  fields = ['borrowsl', 'borrowdt', 'backdt']

  def form_valid(self, form):
    form.instance.borrowps = LogPerson.objects.get(id=self.kwargs['eid'])
    return super().form_valid(form)

  def get_success_url(self):
    return "/log/".format(self.object.id) 