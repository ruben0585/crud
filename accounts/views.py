from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
#estoy creando la clase que llamo SignUpView que hereda de CreateView
# form_class, success_url y template_name son parametros, el primera tendra el comportamiento ya predefinido UserCreationForm
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'