from django.shortcuts import render
from .models import Banner,AboutUs,Gallery,Service,Testimonial,MeetOurTeam,AboutBusiness

# Create your views here.

def home(request):
    banner = Banner.objects.order_by('-id').first()
    about = AboutUs.objects.order_by('-id').first()
    services = Service.objects.order_by('-id')
    testimonial = Testimonial.objects.all()

    context = {
        "banner":banner,
        "about":about,
        "services":services,
        "testi":testimonial
    }
    return render(request, 'home.html',context)


def about(request):
    about = AboutUs.objects.order_by("-id").first()
    about_business = AboutBusiness.objects.order_by("-id").first()
    ourteam = MeetOurTeam.objects.all()

    context = {
        'about':about,
        "about_business":about_business,
        'team': ourteam
    }
    return render(request, 'about.html', context)

def services(request):
    services = Service.objects.all()

    context={
        'service':services
    }
    return render(request, 'services.html',context)

def gallery(request):

    image = Gallery.objects.all()

    return render(request, 'gallery.html',{"image":image})

def contact(request):
    return render(request, 'contact.html')




