from apps.contrib.emails import Email


class InviteParticipantEmail(Email):
    template_name = '{{ cookiecutter.project_app_prefix}}_projects/emails/invite_participant'

    def get_receivers(self):
        return [self.object.email]


class InviteModeratorEmail(Email):
    template_name = '{{ cookiecutter.project_app_prefix}}_projects/emails/invite_moderator'

    def get_receivers(self):
        return [self.object.email]
