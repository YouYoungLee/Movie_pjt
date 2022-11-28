from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.nickname = data.get('nickname')
        user.gender = data.get('gender')
        user.region = data.get('region')
        user.name = data.get('name')
        user.save()
        return user