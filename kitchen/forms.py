from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Cook


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
