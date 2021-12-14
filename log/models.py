from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class LogPerson(models.Model):
  #身分清單
  ST_OPTIONS = [
    (0, '行政人員'),
    (1, '正式教師'),
    (2, '代理教師'),
    (3, '兼任教師'),
  ]
  #高國中部清單
  HJ_OPTIONS = [
    (0, '高中部'),
    (1, '國中部'),
  ]
  #在職狀態清單
  ATWORK_OPTIONS = [
    (0, '工作中'),
    (1, '已離職'),
  ]

  #借用人
  subject = models.CharField('借用人', max_length=255)
  #身分
  status = models.IntegerField(
              '在校身分', 
              default=0, 
              choices=ST_OPTIONS
           )
  #國高中部
  department = models.IntegerField(
              '國/高中部', 
              default=0, 
              choices=HJ_OPTIONS
           )
  #職稱科目
  title = models.CharField('科目/行政職稱', max_length=255)
  # 聯絡電話
  phone = models.CharField('聯絡電話', max_length=30)
  # 信箱
  mail = models.EmailField('電子信箱', max_length=255)
  #在職狀態
  isatwork = models.IntegerField(
              '在職狀態', 
              default=0, 
              choices=ATWORK_OPTIONS
           )
  def __str__(self):
    return self.subject

class LogType(models.Model):
  #型號
  type = models.CharField('型號', max_length=63)
  #購買時間
  buydate = models.DateField('購買時間')
  #詳細規格
  detail = models.TextField('詳細規格', max_length=511)
  
  def __str__(self):
    return self.type

class LogItems(models.Model):
  #狀態清單
  EQPST_OPTIONS = [
    (0, '使用中'),
    (1, '已淘汰'),
  ]
  #設備編號
  serial = models.CharField('設備編號', max_length=63)
  #型號
  itemtype = models.ForeignKey(LogType, on_delete = models.CASCADE, null=True, verbose_name="型號")
  #財產編號
  tenure = models.CharField('財產編號', max_length=63)
  #備註
  remark = models.TextField('備註', max_length=511)
  #狀態
  eqpst = models.IntegerField(
              '設備狀態', 
              default=0, 
              choices=EQPST_OPTIONS
           )
  def __str__(self):
    return self.serial

class LogBorrow(models.Model):
  #設備編號
  borrowsl = models.ForeignKey(LogItems, on_delete = models.CASCADE, null=True, verbose_name="設備編號")
  #借用人
  borrowps = models.ForeignKey(LogPerson, on_delete = models.CASCADE, null=True, verbose_name="借用人")
  #借出日期
  borrowdt = models.DateField('借出時間')
  #歸還日期
  backdt = models.DateField('歸還日期', blank=True, null=True)
  def __str__(self):
    return self.borrowsl