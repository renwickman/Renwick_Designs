from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

party = {'1': "Birthday Party",
        '2': "Wedding",
		'3': "Engagement",
		'4': "Baby Shower",
        '5': "Surprise Party",
        '6': "Graduation Party"
}

people = {'1': "0-50",
        '2': "51-100",
        '3': "101-150",
        '4': "151-200",
        '5': "200-250",
        '6': "251-299",
        '7': "300+"
}

art = {'1': "Calligraphy",
            '2': "Lettering"
}

def index(request):
    return render(request, "index.html")

def createUser(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print("User's password entered was " + request.POST['password'])
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_pw, email=request.POST['email'])
            print("User's password has been changed to " + user.password)
    return redirect('/')

def login(request):
     if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if not user:
            messages.error(request, "Invalid credentials")
            return redirect('/')
        if user:
            user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id #IMPORTANT!!!
                request.session['user'] = user.first_name
            return redirect("/profile")

def profile(request):
    context = {
        'all_designs': Design.objects.all()
    }
    if "user_id" in request.session:
        return render(request, "user.html", context)
    else:
        return redirect('/')

def portfolio(request):
    return render(request, "portfolio.html")

def project(request):
    return render(request, "project.html")

def selectedProject(request):
    Design.objects.create(
        project=request.POST['project'],
        user=User.objects.get(id=request.session['user_id'])
    )
    request.session['project'] = art[request.POST['project']]
    return redirect('/context')

def context(request):
    return render(request, "context.html")

def selectedContext(request):
    design = Design.objects.order_by('id')[0]
    design.context = party[request.POST['context']]
    design.save()
    # design = Design.objects.latest('project')
    # Design.objects.create(
    #     context=request.POST["context"],
    #     user=User.objects.get(id=request.session['user_id'])
    # )
    request.session['context'] = party[request.POST['context']]
    return redirect('/location')

def location(request):
    return render(request, "location.html")

def additionalInput(request):
    if request.method == "POST":
        errors = Location.objects.location_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/location')
        else:
            design = Design.objects.order_by('id')[0]
            full_address = Location.objects.create(address=request.POST['address'], city=request.POST['city'], state=request.POST['state'], zip_code=request.POST['zip_code'], user=User.objects.get(id=request.session['user_id']))
            print(full_address.address, "------------------------------------------")
            design.guests = people[request.POST['guests']]
            design.save()
            request.session['address'] = full_address.address
            request.session['city'] = full_address.city
            request.session['state'] = full_address.state
            request.session['zip_code'] = full_address.zip_code
            request.session['guests'] = people[request.POST['guests']]
    return redirect('/cart')

def cart(request):
    total = 150.00
    fee = 20.00
    charge = 20.00
    grand_total = total + charge + fee
    if Design.objects.order_by('id')[0].context == 'Wedding':
        if Design.objects.order_by('id')[0].guests == '300+' :
            total = 275.00
            fee = 30.00
    context = {
        'all_designs': Design.objects.all(),
        'total': total,
        'fee': fee,
        'charge': charge,
        'grand_total': grand_total,
    }
    return render(request, "cart.html", context)

def checkout(request):
    return render(request, "checkout.html")

def completeService(request):
    # design = Design.objects.order_by('id')[0]
    # design.fee = request.POST['fee']
    # design.total = request.POST['total']
    # design.charge = request.POST['charge']
    # design.grand_total = request.POST['grand_total']
    # design.save()

    return redirect('/checkout')

def scheduledConsult(request):
    design = Design.objects.order_by('id')[0]
    design.consultation = request.POST['consultation']
    design.save()
    context = {
        'all_designs': Design.objects.all(),
        "consultation": request.POST['consultation']
    }
    request.session['consultation'] = request.POST['consultation']
    return render(request, "consultation.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')

def homepage(request):
    if "user" in request.session:
        return render(request, "index.html")
    else:
        return redirect('/')

# Create your views here.


#  request.session['context'] = request.POST['context']
#     request.session['guests'] = request.POST['guests']
#     request.session['full_address'] = request.POST['full_address']

# context = {
#         "project": request.POST['project'],
#         "context": request.POST['context'],
#         "guests": request.POST['guests'],
#         "grand_total": request.POST['grand_total']
#     }