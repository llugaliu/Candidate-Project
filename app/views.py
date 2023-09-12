from django.shortcuts import render, redirect
from .forms import CandidateRegisterForm, SignUpForm, EmailForm, ChatForm
from .models import Candidate, Email, Chat
from django.core.mail import EmailMessage, send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'base/signup.html', {'form': form})


@login_required(login_url='login')
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        candidates = Candidate.objects.filter(
            Q(firstname__icontains=q) |
            Q(lastname__icontains=q) |
            Q(age__icontains=q) |
            Q(job__icontains=q) |
            Q(email__icontains=q) |
            Q(gender__icontains=q)
        )
    else:
        candidates = Candidate.objects.all()
    paginator = Paginator(candidates, 10)
    page = request.GET.get('page')
    all_candidate = paginator.get_page(page)
    total = candidates.count()
    pd = candidates.filter(job='PD-22').count()
    sd = candidates.filter(job='SD-10').count()
    da = candidates.filter(job='DA-12').count()
    context = {
        'candidates': all_candidate,
        'total': total,
        'pd': pd,
        'sd': sd,
        'da': da
    }
    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def register_candidate(request):
    if request.method == 'POST':
        form = CandidateRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Candiate was added!')
            return redirect('/')
    else:
        form = CandidateRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'app/register_candidate.html', context)


@login_required(login_url='login')
def candidate(request, pk):
    candidate = Candidate.objects.get(pk=pk)
    return render(request, 'app/candidate.html', {'candidate': candidate})


@login_required(login_url='login')
def delete_canidate(request, pk):
    x = Candidate.objects.values_list('email', flat=True)
    y = Chat.objects.filter(candidate_email__in=x)
    candidate = Candidate.objects.get(pk=pk)
    for data in y:
        if data.candidate_email in candidate.email:
            candidate.delete()
            Chat.objects.exclude(candidate_email__in=x).delete()
            return redirect('/')
        else:
            candidate.delete()
            messages.info(request, 'Candidate was deleted!')
            return redirect('/')


@login_required(login_url='login')
def email(request):
    if request.method == 'POST':
        to_db = Email(
            name=request.POST.get('name'),
            status=request.POST.get('status'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
            email=request.POST.get('email'),

        )
        to_db.save()
        form = EmailForm(request.POST)
        company = 'provapython@outlook.com'
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, company, [email])
            messages.success(request, 'Email was sent!')

            return redirect('/')
    else:
        form = EmailForm()
    return render(request, {'form': form})


def chat(request, pk):
    candidate = Candidate.objects.get(pk=pk)
    chats = Chat.objects.all().order_by('-date')
    user_list = User.objects.all()
    form = ChatForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('chat', pk=candidate.id)
    context = {
        'candidate': candidate,
        'chats': chats,
        'user_list': user_list,
        'form': form
    }
    return render(request, 'app/chat.html', context)
