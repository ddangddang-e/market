from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # 메인 페이지로 리디렉션
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # 로그인 페이지로 리디렉션
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 로그인 후 홈 페이지로 리디렉션
            else:
                form.add_error(None, '잘못된 로그인 정보입니다.')
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})

#새넣
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Product

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    products = Product.objects.filter(user=user)
    liked_products = user.liked_products.all()
    followers_count = user.followers.count()
    following_count = user.following.count()

    context = {
        'user_profile': user,
        'products': products,
        'liked_products': liked_products,
        'followers_count': followers_count,
        'following_count': following_count,
    }
    return render(request, 'accounts/profile.html', context)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User
from products.models import Product  # Product 모델을 임포트
from django.contrib.auth.models import Group, Permission

@login_required
def profile(request):
    # 현재 로그인한 사용자 정보 가져오기
    user = request.user

    # 사용자가 등록한 상품 목록
    products = Product.objects.filter(owner=user)

    # 사용자가 찜한 상품 목록
    liked_products = user.liked_products.all()

    # 사용자의 팔로워와 팔로잉 목록
    followers = user.followers.all()  # User 모델에서 followers를 정의했다고 가정
    following = user.following.all()  # User 모델에서 following을 정의했다고 가정

    # 프로필 페이지 렌더링
    return render(request, 'accounts/profile.html', {
        'user': user,
        'products': products,
        'liked_products': liked_products,
        'followers': followers,
        'following': following
    })
