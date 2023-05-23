from django.shortcuts import render,HttpResponse,redirect
from app.models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.

# login
def loginn(request):
    return render(request,'login.html')

def login_post(request):
    username = request.POST['name']
    password = request.POST['password']
    res=login.objects.filter(username=username,password=password)
    if res.exists():
        res=login.objects.get(username=username,password=password)
        request.session['lid']=res.id
        if res.type=='user':
            return redirect('/styled/')
        elif res.type=='admin':
            return redirect('/admin_styled/')
        else:
            return redirect('/')
    else:
        return redirect('/')

# logout
def logout(request):
    request.session['lid']=''
    return redirect('/')

# register
def register(request):
    return render(request,'register.html')

def register_post(request):
    name=request.POST['name']
    gender=request.POST['gender']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    photo=request.FILES['photo']
    password=request.POST['pass']
    confirm=request.POST['pass2']
    if password==confirm:
        lobj=login()
        lobj.username=email
        lobj.password=password
        lobj.type='user'
        lobj.save()
        robj=user()
        robj.name=name
        robj.gender=gender
        robj.email=email
        robj.phone=phone
        robj.place=place
        from datetime import datetime
        fs=FileSystemStorage()
        dt=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
        fn=fs.save(dt,photo)
        robj.photo=fs.url(dt)
        robj.LOGIN=lobj
        robj.save()
        return HttpResponse("<script>alert('Added Successfully');window.location=''</script>")
    else:
        return HttpResponse("<script>alert('Password Does not Match');window.location='/register/'</script>")


# user Home

def  user_home(request):
    return render(request,'user_home.html')

# admin Home

def admin_home(request):
    return render(request,'admin_home.html')

# admin add item

def admin_add_item(request):
    return render(request,'admin_add_product.html')

def admin_add_item_post(request):
    productt=request.POST['product']
    price=request.POST['price']
    image=request.FILES['photo']
    from datetime import datetime
    dt=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fn=fs.save(dt,image)
    pobj=product()
    pobj.product=productt
    pobj.price=price
    pobj.photo=fs.url(dt)
    pobj.save()
    return HttpResponse("<script>alert('Added Successfully');window.location='/admin_add_item/'</script>")


# admin view product

def admin_view_product(request):
    res=product.objects.all()
    return render(request,'admin_view_product.html',{'data':res})

# admin delete product

def admin_delete_product(request,pid):
    product.objects.filter(pk=pid).delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/admin_view_product/'</script>")

# admin edit item

def admin_edit_item(request,pid):
    res=product.objects.get(pk=pid)
    return render(request,'admin_edit_product.html',{'data':res})

def admin_edit_item_post(request):
    pid=request.POST['pid']
    productt=request.POST['product']
    price=request.POST['price']
    if 'photo' in request.FILES:
        image=request.FILES['photo']
        if image.name!='':
            from datetime import datetime
            dt=datetime.now().strftime("%Y%m%d-%H%M%S")
            fs=FileSystemStorage()
            fn=fs.save(dt,image)
            res=product.objects.filter(pk=pid).update(product=productt,price=price,photo=fs.url(dt))
            return HttpResponse("<script>alert('Updated Successfully');window.location='/admin_view_product/'</script>")
        else:
            res = product.objects.filter(pk=pid).update(product=productt, price=price)
            return HttpResponse("<script>alert('Updated Successfully');window.location='/admin_view_product/'</script>")
    else:
        res=product.objects.filter(pk=pid).update(product=productt,price=price)
        return HttpResponse("<script>alert('Updated Successfully');window.location='/admin_view_product/'</script>")


# user view product

def user_view_product(request):
    res=product.objects.all()
    return render(request,'user_view_product.html',{'data':res})

# user add cart

def user_add_cart(request,pid):
    request.session['pid']=pid
    return render(request,'add_cart.html')

def user_add_cart_post(request):
    quantity=request.POST['qty']
    pid=request.session['pid']
    uid=user.objects.get(LOGIN_id=request.session['lid'])
    res=cart.objects.filter(PRODUCT_id=pid,USER_id=uid)
    if res.exists():
        res2=cart.objects.get(PRODUCT_id=pid,USER_id=uid)
        oldqty=res2.qty
        newqty=oldqty+quantity
        cart.objects.filter(pk=res2.id).update(qty=newqty)
        return HttpResponse("<script>alert('Updated Successfully');window.location='/user_view_cart/'</script>")
    else:
        cobj=cart()
        cobj.qty=quantity
        cobj.USER_id=uid.id
        cobj.PRODUCT_id=pid
        cobj.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/user_view_cart/'</script>")

# user view cart

def user_view_cart(request):
    res=cart.objects.filter(USER_id=user.objects.get(LOGIN_id=request.session['lid']).id)
    li=[]
    for i in res:
        price=i.PRODUCT.price
        qty=i.qty
        tot=price*qty
        li.append(tot)
    total=sum(li)
    return render(request,'user_view_cart.html',{'data':res,'total':total})

# delete cart

def user_delete_cart(request,cid):
    cart.objects.filter(pk=cid).delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/user_view_cart/'</script>")


def styled(request):
    return render(request,'styled.html')

def admin_styled(request):
    return render(request,'admin_styled.html')
