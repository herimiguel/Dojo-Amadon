from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index(request):
    if 'total_quantity' not in request.session:
        request.session['total_quantity'] = 0
        request.session['total_cost']= 0

    return render(request, 'my_app/index.html')

def buying(request):
    if request.method == 'POST':
        print "-----------"
        request.session['new_quantity'] = int(request.POST['quantity'])
        request.session['new_price'] = float(request.POST['price']) * int(request.session['new_quantity'])
        # request.session['price'] = float(request.POST['price'])
    return redirect('/checkingOut')

def checkingOut(request):
    try:
        request.session['total_quantity'] += int(request.session['new_quantity'])
        request.session['total_cost'] += float(request.session['new_price'])
    except:
        request.session['total_quantity'] = int(request.session['new_quantity'])
        request.session['total_cost'] = float(request.session['new_price']) * request.session['new_quantity']
    # request.session['new_quantity'] = request.POST['quantity'] 
    return render(request, 'my_app/checkOut.html')

def reset(request):
    request.session.clear()
    return redirect('/')



