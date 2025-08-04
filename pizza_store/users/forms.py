from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

