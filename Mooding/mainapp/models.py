
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	nickname = models.CharField(max_length=100, blank=True, null=True)

class Cafe(models.Model): # 카페 클래스
    Relax = 0
    Average = 1
    Congestion = 2
    CONGESTION_CHOICE =(
        (Relax, '여유'),
        (Average, '보통'),
        (Congestion, '혼잡')
    )
    WEEK =(
        ('MON', '월요일'),
        ('TUS', '화요일'),
        ('WEN', '수요일'),
        ('THR', '목요일'),
        ('FRI', '금요일'),
        ('SAT', '토요일'),
        ('SON', '일요일'),
    )
    id = models.AutoField(primary_key=True) # 카페 아이디(프라이머리 키)
    title = models.CharField(max_length=100) # 카페이름
    explanation = models.TextField(blank=True) # 카페 설명
    reservation_available = models.BooleanField() #예약 가능여부
    charge_available = models.BooleanField() # 충전 가능 여부
    total_seats = models.SmallIntegerField() # 총 좌석 수
    used_seats = models.SmallIntegerField(null=True) # 사용하고 있는 좌석 수
    unused_seats = models.SmallIntegerField(null=True) # 미사용 좌석 수
    congestion_status = models.SmallIntegerField(default=0, choices=CONGESTION_CHOICE) # 혼잡여부(숫자료 표현 0, 1, 2) choice 활용
    lat = models.SmallIntegerField() #위도 (영빈이형 말대로 네이버 GPS사용하기.)(영빈이형 말로는 위도 경도는 정수가 아닌 문자열로 받아서 소수점 변환이 좋음)
    lng = models.SmallIntegerField() #경도
    thumbnail = models.ImageField(default ="#") #썸네일 이미지
    operating_hour = models.TextField(blank=True) #운영시간
    close_day = models.TextField(blank=True, choices=WEEK)  #ㅇㅣ거는 choices 활용해서 다시한번더 바꿔보기/
    cafe_phone_number = models.TextField(blank=True)
class Review(models.Model): # 리뷰 서비스
    Star1 = 1
    Star2 = 2
    Star3 = 3
    Star4 = 4
    Star5 = 5
    RATING =(
        (Star1, '1점'),
        (Star2, '2점'),
        (Star3, '3점'),
        (Star4, '4잠'),
        (Star5, '5점'),
    )
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE) # 카페 하나에 종속
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    writer = models.CharField(max_length=20)# 작성자
    rating = models.SmallIntegerField(default=5, choices=RATING) # 별점
    comment = models.TextField() #리뷰내용


class Product(models.Model): #판매할 상품
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE) # 카페 하나에 종속
    title = models.CharField(max_length=100) #상품 이름
    price = models.IntegerField() # 상품가격
    reduced_price = models.IntegerField()#할인가격
    out_of_stock = models.BooleanField() # 매진여부
    

class Image(models.Model): # 이미지 
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE) #카페 종속
    representative_image = models.ImageField() #카페 대표 이미지

class Coupon(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stamp = models.IntegerField(default=0)
    prizes = models.TextField(default="아메리카노 1잔")
    free_coupon = models.IntegerField(default=0)
   
class Queuing(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    used_table = models.IntegerField(default=0)
    waiting_team = models.IntegerField(default=0)
    estimated_latency_default = models.IntegerField(default=30)
    estimated_latency = models.IntegerField(default=0)