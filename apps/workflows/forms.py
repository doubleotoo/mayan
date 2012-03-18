from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Workflow, State, Transition, WorkflowState


class WorkflowSetupForm(forms.ModelForm):
    class Meta:
        model = Workflow


class StateSetupForm(forms.ModelForm):
    class Meta:
        model = State


class WorkflowStateSetupForm(forms.ModelForm):
    class Meta:
        model = WorkflowState