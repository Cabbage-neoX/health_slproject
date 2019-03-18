from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20,verbose_name='真实姓名')
    nickname=models.CharField(max_length=50,verbose_name='昵称')
    phone=models.IntegerField(verbose_name='手机')
    sex=models.CharField(max_length=5,verbose_name='性别')
    height=models.FloatField(max_length=200,verbose_name='身高')
    weight=models.FloatField(max_length=500,verbose_name='体重')
    age=models.IntegerField(verbose_name='年龄')
    blood_type=models.CharField(max_length=10,verbose_name='血型')

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name=models.CharField(max_length=10,verbose_name='姓名')
    phone = models.IntegerField(verbose_name='手机')
    department = models.CharField(max_length=10, verbose_name='科室')

    def __str__(self):
        return self.name

class Diagnostic_results(models.Model):
    data=models.DateTimeField(verbose_name='日期')
    department=models.CharField(max_length=10,verbose_name='科室')
    doctor=models.ManyToManyField(Doctor)
    result=models.TextField(max_length=300,verbose_name='诊断结果')
    user=models.OneToOneField(User,on_delete=models.PROTECT,verbose_name='病人')
    solution=models.TextField(max_length=500,verbose_name='解决方法')

    def __str__(self):
        return self.result
class Doctor_to_user(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT,verbose_name='病人')
    diagnostic_results=models.OneToOneField(Diagnostic_results,on_delete=models.PROTECT,verbose_name='诊断结果')
    doctor=models.ForeignKey(Doctor,on_delete=models.PROTECT,verbose_name='医生')

