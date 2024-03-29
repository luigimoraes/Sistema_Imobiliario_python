from django import forms

# importar usuário 
from django.contrib.auth.models import User

# importar um formulário padrão para criação de usuários
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError

class UsuariosForm(UserCreationForm):

    # campos abaixo criados para tornar obeigatórios
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', ]

    # função criada para incluir o verbose name
    def __init__(self, *args, **kwargs):
        super(UsuariosForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nome"
        self.fields['last_name'].label = "Sobrenome"

    # função criada para validar o campo email
    def clean_email(self):
        valida_email = self.cleaned_data['email']
        if User.objects.filter(email=valida_email).exists():
            raise ValidationError("Esse email já está cadastro no nosso sistema")
        return valida_email
