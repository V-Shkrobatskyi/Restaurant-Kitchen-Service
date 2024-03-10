from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

from kitchen.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience", )

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(years_of_experience,):
    if len(str(years_of_experience)) > 2:
        raise ValidationError("Years of experience should be maximum 2 digits")

    return years_of_experience


class CookExperienceUpdateForm(forms.ModelForm):
    years_of_experience = forms.CharField(
        required=True,
        validators=[validate_years_of_experience,]
    )

    class Meta:
        model = Cook
        fields = ("years_of_experience",)


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"
