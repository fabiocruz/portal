import logging  # noqa: D100

from crispy_forms.layout import Field
from django import forms

from . import models

logger = logging.getLogger(__name__)


class CustomCheckbox(Field):  # noqa: D101
    template = "crispy/custom_checkbox.html"


class StudentAttendanceForm(forms.ModelForm):  # noqa: D101
    class Meta:  # noqa: D106
        model = models.Attendance
        fields = [
            # 'remote'
        ]

    def clean(self):  # noqa: D102
        cleaned_data = super().clean()
        if self.instance.hackathon.status != "taking_attendance":
            raise forms.ValidationError("Marking attendance is closed")
        return cleaned_data


class TeamForm(forms.ModelForm):  # noqa: D101
    class Meta:  # noqa: D106
        model = models.Team
        fields = ["name", "logo"]


class SubmitForm(forms.Form):  # noqa: D101
    data = forms.FileField()

    class Meta:  # noqa: D106
        fields = ["data"]


class InstructorHackathonForm(forms.ModelForm):  # noqa: D101
    class Meta:  # noqa: D106
        model = models.Hackathon
        fields = [
            "status",
            "max_submissions",
            "team_size",
            "max_team_size",
            "max_teams",
            "descending",
            "script_file",
            "data_file",
        ]

    # def clean_teams_closed(self):
    #     if self.cleaned_data['teams_closed']:
    #         if not self.instance.teams.exists():
    #             # TODO not shown
    #             raise forms.ValidationError("Generate teams first",
    #                                         code='invalid')
    #         self.cleaned_data['attendance_open'] = False
