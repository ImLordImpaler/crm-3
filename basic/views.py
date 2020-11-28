from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Enquiry , Product , Employee , Client , Bill , Slip
from .forms import ProductForm , EnquiryForm , EmployeForm , SignUpForm , NewBill , NewClient , NewSlip
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginPage')
def cover(request):
    return render(request , 'basic/cover.html')

def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        user = authenticate(username=uname , password = pwd)

        if user is not None:
            login(request , user)
            return redirect('calendarapp:calendar')
        else:
            return render(request , 'basic/404.html')
    else :
        pass

    return render(request , 'basic/login.html')

def register(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('calendarapp:index')
        else:
            return HttpResponse("Nai hua bhau")
    else :
        form = SignUpForm()
    params = {
    'form': form
    }

    return render(request , 'basic/register.html' , params )
    
     


def logoutPage(request):
    logout(request)
    return redirect('loginPage')
@login_required(login_url='loginPage')
def home(request):
    enq = Enquiry.objects.all()
    
    pro = Product.objects.all().order_by('quantity')
   
    params = {
        'enq': enq ,
        'pro' : pro
    }
    return render(request , 'basic/dashboard.html' , params)


@login_required(login_url='loginPage')
def enquiry(request):
    enq = Enquiry.objects.all()
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')
        else :
            return HttpResponse('<h3> Try again </h3>')
    else :
        form = EnquiryForm()
    params = {
        'form' : form ,
        'pro' : enq
    }

    return render(request , 'basic/enquiry.html' , params)
@login_required(login_url='loginPage')
def enquiryUpdate(request , pk):
    enq = Enquiry.objects.get(id = pk)
    
    if request.method == 'POST':
        form = EnquiryForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = EnquiryForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/enquiryForm.html' , params)

@login_required(login_url='loginPage')
def deleteEnquiry(request , pk):
    pro = Enquiry.objects.get(id=pk)
    if request.method=='POST':
        pro.delete()
        return redirect('enquiry')
    params = {
        'item': pro
    }
    return render(request , 'basic/deleteEnquiry.html' , params )


@login_required(login_url='loginPage')
def product(request):
    enq = Product.objects.all()
    form = EnquiryForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else :
            return HttpResponse('<h3> Try again </h3>')
    else :
        form = ProductForm()
    params = {
        'form' : form ,
        'pro' : enq
    }

    return render(request , 'basic/product.html' , params)
    

@login_required(login_url='loginPage')
def productEnquiry(request , pk):
    enq = Product.objects.get(id = pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = ProductForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/productForm.html' , params)
@login_required(login_url='loginPage')
def employee(request):
    emp = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else :
            return HttpResponse('kya hai reh halkat. Tereko likhne ka nai atta kya?')
    else:
        form = EmployeForm()
    params = {
        'form': form,
        'pro': emp
    }
    return render(request , 'basic/employee.html' , params)
@login_required(login_url='loginPage')
def employeeUpdate(request , pk):
    enq = Employee.objects.get(id = pk)
    
    if request.method == 'POST':
        form = EmployeForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = EmployeForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/empForm.html' , params)
@login_required(login_url='loginPage')
def stock(request):
    pro = Product.objects.all()
    params = {
        'stock': pro
    }
    return render(request , 'basic/album.html' , params)
@login_required(login_url='loginPage')
def clients(request):
    cli = Client.objects.all()
    form = NewClient()
    if request.method=='POST':
        form = NewClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendarapp:calendar')
        else :
            return render(request , 'basic/404.html')
    else : 
        form = NewClient()
        
    params = {
        'pro' : cli,
        'form' : form
    }
    return render(request , 'basic/forms/newClient.html' , params)

def clientUpdate(request , pk):
    enq = Client.objects.get(id = pk)
    
    if request.method == 'POST':
        form = NewClient(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = NewClient(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/forms/updateClient.html' , params)
def deleteClient(request , pk):
    cli = Client.objects.get(id=pk)
    if request.method == 'POST':
        cli.delete()
        return redirect('clients')
    params = {
        'item': cli
    }
    return render(request , 'basic/forms/deleteClient.html' , params)



@login_required(login_url='loginPage')
def deleteEmployee(request , pk):
    Emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        Emp.delete()
        return redirect('employee')
       
    
    params = {
        'item': Emp
    }

    return render(request, 'basic/deleteEmployee.html' , params)
@login_required(login_url='loginPage')
def deleteProduct(request , pk):
    pro = Product.objects.get(id=pk)
    if request.method=='POST':
        pro.delete()
        return redirect('product')
    params = {
        'item': pro
    }
    return render(request , 'basic/deleteProduct.html' , params)


def serviceSlip(request):
    cli = Slip.objects.all()
    form = NewSlip()
    if request.method=='POST':
        form = NewSlip(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serviceSlip')
        else :
            return render(request , 'basic/404.html')
    else : 
        form = NewSlip()
        
    params = {
        'pro' : cli,
        'form' : form
    }
    return render(request , 'basic/forms/serviceSlip.html' , params)

def updateSlip(request , pk):
    slip = Slip.objects.get(id=pk)
    if request.method == 'POST':
        form = NewSlip(request.POST , instance=slip)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = NewSlip(instance= slip)
    params = {
        'form': form,
        'pro' : slip
    }

    return render(request , 'basic/forms/updateSlip.html' , params)

def deleteSlip(request , pk):
    slip = Slip.objects.get(id=pk)
    if request.method == 'POST':
        slip.delete()
        return redirect('calendarapp:calendar')
    params = {
        'item' : slip
    }
    return render(request , 'basic/forms/deleteSlip.html' , params)

def billing(request):
    bill = Bill.objects.all()
    form = NewBill()
    if request.method == 'POST':
        form = NewBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing')
        else:
            return render(request , 'basic/404.html')
    else: 
        form = NewBill()

    params = {
        'pro': bill,
            'form' : form
    }
    return render(request , 'basic/forms/billing.html', params)