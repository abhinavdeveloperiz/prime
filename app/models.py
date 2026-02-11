from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
    
class AboutUs(models.Model):
    image=models.ImageField(upload_to='about_us/')

    def __str__(self):
        return "About Introduction Image"
    
    class Meta:
        verbose_name = "About Us Introduction"
        verbose_name_plural = "About Us Introduction"


class AboutBusiness(models.Model):
    image=models.ImageField(upload_to='about_us/')

    def __str__(self):
        return "About Image"
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True ,blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"



class MeetOurTeam(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Our Team"
        verbose_name_plural = "Our Team"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    

