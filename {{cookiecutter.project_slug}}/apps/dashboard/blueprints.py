from django.utils.translation import ugettext_lazy as _

from adhocracy4.dashboard.blueprints import ProjectBlueprint
from apps.ideas import phases as ideas_phases
{% if cookiecutter.use_maps_and_mapideas == 'y' %}
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
{% if cookiecutter.use_maps_and_mapideas == 'y' %}
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
]
