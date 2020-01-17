from django import forms
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import UserDetails, Internship, Intern, Topic, Subtopic, AssignedTopics,Data

INTERN_STATUS = (
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE"),
)

STATUS = (
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE"),
    ("COMPLETED", "COMPLETED"),
)

DATA_STATUS = (
    ("ACCEPTED", "ACCEPTED"),
    ("REJECTED", "REJECTED"),
    ("WAITING", "WAITING"),
    ("UNDER REVIEW", "UNDER REVIEW"),
)


class AddUserForm1(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AddUserForm2(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user_phone', 'user_role']


class AddInternship(ModelForm):
    class Meta:
        model = Internship
        fields = ['internship_topic', 'internship_thumbnail', 'internship_status']


class ManageInternship(ModelForm):
    class Meta:
        model = Internship
        fields = ['internship_status']


class ManageIntern(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user_status']


class AddIntern(ModelForm):
    class Meta:
        model = Intern
        labels = {
            'user_id' : 'Intern Name',
            'internship_id' : 'Internship Name'
        }
        fields = ['user_id','internship_id']
    def __init__(self, user, *args, **kwargs):
        super(AddIntern, self).__init__(*args, **kwargs)
        self.fields['user_id'].queryset = UserDetails.objects.filter(user_role="INTERN", user_status="ACTIVE")
    

class AssignTopic(ModelForm):
    class Meta:
        model = AssignedTopics
        fields = ['user_id','topic_id']
    def __init__(self, user, *args, **kwargs):
        super(AssignTopic, self).__init__(*args, **kwargs)
        self.fields['user_id'].queryset = UserDetails.objects.filter(user_role="INTERN", user_status="ACTIVE")



class data(ModelForm):
    class Meta:
        model=Data
        fields=['data_content','data_reference']


class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
        )

    def clean(self):
        user = self.authenticate_via_email()
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        else:
            self.user = user
        return self.cleaned_data

    def authenticate_user(self):
        return authenticate(
            username=self.user.username,
            password=self.cleaned_data['password'])

    def authenticate_via_email(self):
        """
            Authenticate user using email.
            Returns user object if authenticated else None
        """
        email = self.cleaned_data['email']
        if email:
            try:
                user = User.objects.get(email__iexact=email)
                if user.check_password(self.cleaned_data['password']):
                    return user
            except ObjectDoesNotExist:
                pass
        return user


class add_topic(forms.Form):
    # class Meta:
    #     model = Topic
    #     fields = ['topic_name']
    topic = forms.CharField(max_length=255, widget=forms.TextInput())


class add_subtopic(forms.Form):
    subtopic = forms.CharField(max_length=255, widget=forms.TextInput())

# # Edit data

# class edit_data(forms.ModelForm):
#     text = RichTextUploadingField()

#     class Meta:
#         model = data
#         fields = ('text',)

# class AddUserForm(forms.ModelForm):
#     firstname = forms.CharField(max_length=20)
#     lastname = forms.CharField(max_length=20)

#     class Meta:
#         model = AddUser
#         labels = {
#             "name" : "Username"
#         }
#         fields = ('firstname', 'lastname', 'name', 'email', 'topic', 'phone', 'role',)


# class DeleteUserForm(forms.ModelForm):
#     class Meta:
#         model = AddUser
#         fields = ('name', 'email',)
