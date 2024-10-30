from django.db import models

from enum import unique
# Create your models here.
# 데이터베이스에서 사용할 테이블을 클래스로 생성한다
# 테이블 = 클래스

#Owner클래스 생성
class Owner(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=128)

#Brand클래스 생성
class Brand(models.Model):
    brand_name = models.CharField(max_length=128, unique=True)

#Car_Model클래스 생성
class Car_Model(models.Model):
    barnd = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=128)

#Car클래스 생성
class Car(models.Model):
    car_number = models.CharField(max_length=128)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car_Model, on_delete=models.CASCADE)