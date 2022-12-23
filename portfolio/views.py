import sendgrid   
from .models import Contact,Project,Comment,DemoImages,Languages
from django.views import View
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, redirect, render, get_object_or_404
from .forms import ContactForm,CommentForm
from django.views.generic import TemplateView,ListView,DetailView
from django.conf import settings 
from sendgrid.helpers.mail import Mail   
from django.contrib import messages
from django.db.models import Q
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class ProjectListView(ListView):
   template_name = 'home.html'
   model = Project
   context_object_name = 'ProjectList'
   
class ProjectListDetailView(DetailView):
   template_name = 'home.html'
   model = Project
   context_object_name = 'project'
   
class DetailView(View):
    def get(self, request, detail_id):
        portfolioDetail = False
        data = get_object_or_404(Project, pk=detail_id)
        if data :
            portfolioDetail = True
            comment = Comment.objects.all().order_by('-created')
            picture = DemoImages.objects.all().order_by('-created')
            logo = Languages.objects.all().order_by('-created')
            context = {
                "project":data,
                "picture":picture,
                "portfolioDetail" : portfolioDetail,
                "comment":comment,
                "languages":logo
            }
            return render(request, "home.html", context)
        context = {
                "project":'',
                "portfolioDetail" : portfolioDetail
            }
        return render(request, "home.html", context)
    
    def post(self, request, detail_id):
        
            data = { 
                    'fistName' : request.POST.get('fistName'),
                    'lastName' : request.POST.get('lastName'),
                    'email'    : request.POST.get('email'),
                    'message'  : request.POST.get('message'),   
            }
            forms = CommentForm(data)
            if forms.is_valid():
                ContactNew = Comment.objects.create(
                    project = Project.objects.get(id=detail_id),
                    fistName = request.POST.get('fistName'),
                    lastName = request.POST.get('lastName'),
                    email = request.POST.get('email'),
                    message = request.POST.get('message'),
                )
                ContactNew.save()
                messages.success(request, f'Your Comment submited successfully!')
                return HttpResponseRedirect(reverse('portfolio:project-list'))
            else:
                return render(request,"home.html",{})
        
class ContactView(View): 
    
    def get(self, request):
        comment = Comment.objects.all().order_by('-created')    
        context = { "allComment":comment}
        return render(request, "home.html", context) 
    
    def post(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                sender = 'temf2006@gmail.com'# system email
                subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
                to = 'egolebearingplc@gmail.com'# admin email
                content = form.cleaned_data['message']
                send_email(to, subject, content, sender)
                messages.success(request, 'Thank you and Your contact information and message submited successfully!!. I will get in touch soon.',
                                extra_tags='successful_submit')
                return render(request, 'home.html')
        form = ContactForm()
        context = {'form': form}
        return render(request, 'home.html', context)           
             
def send_email(to, subject, content, sender ='temf2006@gmail.com'):
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    mail = Mail(
        from_email=sender,
        to_emails=to,
        subject=subject,
        html_content=content
    )
    return sg.send(mail)
    
