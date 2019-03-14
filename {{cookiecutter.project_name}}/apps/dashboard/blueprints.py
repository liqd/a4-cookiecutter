from django.utils.translation import ugettext_lazy as _

from adhocracy4.dashboard.blueprints import ProjectBlueprint
from adhocracy4.polls import phases as poll_phases
from apps.ideas import phases as ideas_phases
from apps.mapideas import phases as map_ideas_phases

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
     ('poll',
     ProjectBlueprint(
         title=_('Poll'),
         description=_('Run customizable, multi-step polls detailed opinions'
                       'on topics from the public or your members.'),
         content=[
             poll_phases.VotingPhase(),
         ],
         image='images/poll.png',
         settings_model=None,
         requirements=Requirements(
             aims=[Aim.run_survey],
             results=[Result.majority_vote],
             experience=Experience.no_projects,
             motivation=Motivation.not_found
         ),
         complexity=COMPLEXITY_VECTOR_E,
         type=BlueprintNames.a4_poll.name
))
]
