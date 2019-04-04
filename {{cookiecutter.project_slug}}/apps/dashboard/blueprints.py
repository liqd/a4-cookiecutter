from django.utils.translation import ugettext_lazy as _

from adhocracy4.dashboard.blueprints import ProjectBlueprint
{% if cookiecutter.add_polls_app == 'y' %}
from adhocracy4.polls import phases as poll_phases
{% endif %}
from apps.ideas import phases as ideas_phases
{% if cookiecutter.add_maps_and_mapideas_app == 'y' %}
from apps.mapideas import phases as map_ideas_phases
{% endif %}

blueprints = [
    ('brainstorming',
     ProjectBlueprint(
         title=_('Brainstorming'),
         description=_(
             'Collect first ideas for a specific topic and comment on them.'
         ),
         content=[
             ideas_phases.CollectPhase(),
         ],
         image='images/brainstorming.svg',
         settings_model=None,
     )),
    ('text-review',
     ProjectBlueprint(
         title=_('Text Review'),
         description=_(
             'In the text-review it’s possible to structure draft texts '
             'that can be commented.'
         ),
         content=[
             documents_phases.CommentPhase(),
         ],
         image='images/blueprints/text-review.svg',
         settings_model=None,
    )),
{% if cookiecutter.add_maps_and_mapideas_app == 'y' %}
    ('brainstorming_map',
     ProjectBlueprint(
         title=_('Spatial Brainstorming'),
         description=_(
             'Collect first ideas for a specific topic and comment on them.'
         ),
         content=[
             map_ideas_phases.CollectPhase(),
         ],
         image='images/map-brainstorming.svg',
         settings_model=('a4maps', 'AreaSettings'),
     )),
{% endif %}
{% if cookiecutter.add_polls_app == 'y' %}
    ('poll',
     ProjectBlueprint(
         title=_('Poll'),
         description=_('Run customizable, multi-step polls detailed opinions'
                       'on topics from the public or your members.'),
         content=[
             poll_phases.VotingPhase(),
         ],
         image='images/poll.svg',
         settings_model=None,
    )),
{% endif %}
]
