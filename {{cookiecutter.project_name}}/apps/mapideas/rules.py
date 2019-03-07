import rules

from adhocracy4.modules import predicates as module_predicates

from . import models

rules.add_perm(
    '{{cookiecutter.project_app_prefix}}_mapideas.view_mapidea',
    module_predicates.is_allowed_view_item
)

rules.add_perm(
    '{{cookiecutter.project_app_prefix}}_mapideas.add_mapidea',
    module_predicates.is_allowed_add_item(models.MapIdea)
)

rules.add_perm(
    '{{cookiecutter.project_app_prefix}}_mapideas.rate_mapidea',
    module_predicates.is_allowed_rate_item
)

rules.add_perm(
    '{{cookiecutter.project_app_prefix}}_mapideas.comment_mapidea',
    module_predicates.is_allowed_comment_item
)

rules.add_perm(
    '{{cookiecutter.project_app_prefix}}.change_mapidea',
    module_predicates.is_allowed_change_item
)

rules.add_perm(
    '{{cookiecutter.project_app_prefix}}.moderate_mapidea',
    module_predicates.is_context_moderator |
    module_predicates.is_context_initiator
)