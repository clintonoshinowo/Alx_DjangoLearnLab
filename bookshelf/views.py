from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

def profile(request):
    CustomUser = get_user_model()
    user = get_object_or_404(CustomUser, id=request.user.id)
    context = {'user': user}
    return render(request, 'bookshelf/profile.html', context)
# Create your views here.
