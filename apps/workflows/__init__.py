from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from project_setup.api import register_setup
from navigation.api import Link, bind_links

from .permissions import (PERMISSION_WORKFLOW_SETUP_VIEW,
    PERMISSION_WORKFLOW_SETUP_CREATE, PERMISSION_WORKFLOW_SETUP_EDIT,
    PERMISSION_WORKFLOW_SETUP_DELETE, PERMISSION_STATE_SETUP_VIEW,
    PERMISSION_STATE_SETUP_CREATE, PERMISSION_STATE_SETUP_EDIT,
    PERMISSION_STATE_SETUP_DELETE)
from .models import Workflow, State, Transition, WorkflowState


setup_workflow_list_link = Link(text=_(u'workflow list'), view='setup_workflow_list', sprite='chart_organisation', permissions=[PERMISSION_WORKFLOW_SETUP_VIEW])
setup_workflow_create_link = Link(text=_(u'create new workflow'), view='setup_workflow_create', sprite='chart_organisation_add', permissions=[PERMISSION_WORKFLOW_SETUP_CREATE])
setup_workflow_edit_link = Link(text=_(u'edit'), view='setup_workflow_edit', args='workflow.pk', sprite='chart_organisation', permissions=[PERMISSION_WORKFLOW_SETUP_EDIT])
setup_workflow_delete_link = Link(text=_(u'delete'), view='setup_workflow_delete', args='workflow.pk', sprite='chart_organisation_delete', permissions=[PERMISSION_WORKFLOW_SETUP_DELETE])
setup_workflow_states_list_link = Link(text=_(u'states'), view='setup_workflow_states_list', args='workflow.pk', sprite='transmit_go', permissions=[PERMISSION_WORKFLOW_SETUP_EDIT])
setup_workflow_states_add_link = Link(text=_(u'add state'), view='setup_workflow_state_add', args='workflow.pk', sprite='transmit_add', permissions=[PERMISSION_WORKFLOW_SETUP_EDIT])
setup_workflow_states_edit_link = Link(text=_(u'edit state'), view='setup_workflow_state_edit', args='workflow_state.pk', sprite='transmit_edit', permissions=[PERMISSION_WORKFLOW_SETUP_EDIT])

setup_state_list_link = Link(text=_(u'state list'), view='setup_state_list', sprite='transmit', permissions=[PERMISSION_STATE_SETUP_VIEW])
setup_state_create_link = Link(text=_(u'create new state'), view='setup_state_create', sprite='transmit_add', permissions=[PERMISSION_STATE_SETUP_CREATE])
setup_state_edit_link = Link(text=_(u'edit'), view='setup_state_edit', args='object.pk', sprite='transmit_edit', permissions=[PERMISSION_STATE_SETUP_EDIT])
setup_state_delete_link = Link(text=_(u'delete'), view='setup_state_delete', args='object.pk', sprite='transmit_delete', permissions=[PERMISSION_STATE_SETUP_DELETE])

bind_links([Workflow], [setup_workflow_states_list_link, setup_workflow_edit_link, setup_workflow_delete_link])
bind_links([Workflow, State, 'setup_workflow_list', 'setup_workflow_create', 'setup_state_list'], [setup_workflow_list_link], menu_name=u'form_header')
bind_links([Workflow, 'setup_workflow_list', 'setup_workflow_create'], [setup_workflow_create_link], menu_name=u'secondary_menu')
bind_links(['setup_workflow_states_list', 'setup_workflow_states_add'], [setup_workflow_states_add_link], menu_name=u'sidebar')

bind_links([State], [setup_state_edit_link, setup_state_delete_link])
bind_links([State, Workflow, 'setup_state_list', 'setup_workflow_list', 'setup_workflow_create'], [setup_state_list_link], menu_name=u'form_header')
bind_links([State, 'setup_state_list', 'setup_state_create'], [setup_state_create_link], menu_name=u'secondary_menu')

bind_links([WorkflowState], [setup_workflow_states_edit_link])

register_setup(Link(text=_(u'workflows'), view='setup_workflow_list', icon='chart_organisation.png', permissions=[PERMISSION_WORKFLOW_SETUP_VIEW]))