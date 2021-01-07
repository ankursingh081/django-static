from django.shortcuts import render, redirect
from .models import Post, Club, Detail, Status
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# posts = [
#     {
#         'author': 'AbhiKN',
#         'title': 'Saiyajin',
#         'content': 'Level 1',
#         'date_posted': 'June 11, 2020'
#     },
#     {
#         'author': 'PratyushaP',
#         'title': 'Human',
#         'content': 'Level 1',
#         'date_posted': 'Nov 18, 2020'
#     }
# ]

# Create your views here.
def home(request) :
    group_list = []
    for g in request.user.groups.all():
        group_list.append(g.name)
    details_list = Detail.objects.all().order_by('-id')
    paginator = Paginator(details_list, 5)
    page_number = request.GET.get('page',1)
    try:
        details = paginator.page(page_number)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    context = {
        'groups': group_list,
        'group_exist': request.user.groups.exists(),
        'details': details,
    }
    return render(request,'blog/home.html', context)

def about(request) :
    return render(request,'blog/about.html')

class ClubChartView(TemplateView):
    template_name = 'blog/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_list = []
        for g in self.request.user.groups.all():
            group_list.append(g.name)
        context['groups'] = group_list
        context['group_exist'] = self.request.user.groups.exists()
        context["qs"] = Club.objects.all()
        context["details"] = Detail.objects.filter(assign_to=self.request.user)
        context["all_details"] = Detail.objects.all()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["qs"] = Club.objects.all()
    #     context["details"] = Detail.objects.filter(assign_to=self.request.user)
    #     context["all_details"] = Detail.objects.all()
    #     return context

    # def get(self, request, *args, **kwargs):
    #     details = Detail.objects.filter(assign_to=self.request.user)
    #     return render(request, self.template_name, {'details': details})

def add_detail(request):
    status = Status.objects.values()
    users_dict = User.objects.values()
    users = []
    for i in range(len(User.objects.all())):
        users.append(users_dict[i]['username'])
    context = {
        'status': status,
        'users': users,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'blog/add_detail.html', context)

    if request.method == 'POST':
        task = request.POST['task']
        assign_date = request.POST['assign_date']
        user_list = request.POST['user_list']
        status = request.POST['status']

        if not task:
            messages.error(request, 'Task name is required')
            return render(request, 'blog/add_detail.html', context)

        if not assign_date:
            messages.error(request, 'Assign Date is required')
            return render(request, 'blog/add_detail.html', context)

    Detail.objects.create(task=task, assign_date=assign_date,
                          assign_to=User.objects.get(username=user_list),
                          status=status)
    messages.success(request, 'Details saved successfully')

    return redirect('blog-home')


def user_home(request) :
    details_list = Detail.objects.filter(assign_to=request.user)
    paginator = Paginator(details_list, 1)
    page_number = request.GET.get('page',1)
    try:
        details = paginator.page(page_number)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    context = {
        'details': details,
    }
    return render(request,'blog/user_home.html', context)