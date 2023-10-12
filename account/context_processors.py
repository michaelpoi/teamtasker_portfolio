from account.models import InviteRequest


def notification_count(request):
    if request.user.is_authenticated:
        n = InviteRequest.objects.filter(user_id=request.user).count()

    else: n = ''
    return {'notification_count': n}