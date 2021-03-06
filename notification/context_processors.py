from notification.models import Notice

def notification(request):
    if request.user.is_authenticated():
        return {
            'notice_unseen_count': Notice.objects.unseen_count_for(request.user, on_site=True),
            'latest_notices': Notice.objects.notices_for(request.user)[0:8]
        }
    else:
        return {}
