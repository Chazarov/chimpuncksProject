from django.shortcuts import render, redirect

from .forms import UserForm
from .models import EnterPass
from main.views import show_archive




def show_reg(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        checking_code = form.data['code']
        user_pas = EnterPass.objects.get(password=checking_code)
        
        if form.is_valid():
            new_record = form.save(commit=False)
            if( user_pas != None):
                new_record.user_type = form.cleaned_data['user_type']
                new_record.user_type = user_pas.user_type
                new_record.save()
                return redirect('archive')
            else: 
                error = "Ключ не найден"
            



            
        else:
            error = 'Форма неверная'
            print(form.errors)
    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "registration/registration.html", context)

