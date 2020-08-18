from django.db import models

# Create your models here.
class Devices(models.Model):
    # 设备名称
    devicename = models.CharField(max_length=200)

    # 设备系统
    devicesystem = models.CharField(max_length=200)

    # 系统版本号
    deviceversion = models.CharField(max_length=200)

    # 设备状态
    devicestate = models.CharField(max_length=200)