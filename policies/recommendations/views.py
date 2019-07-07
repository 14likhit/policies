# Create your views here.
import json
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def PoliciesView(request):
    if request.body is None:
        return Response(None, content_type='application/json', status=400)
    reqdata = json.loads(request.body)
    if 'answer1' not in reqdata or 'answer2' not in reqdata or 'answer3' not in reqdata \
            or 'answer4' not in reqdata or 'answer5' not in reqdata:
        data = {'policies': get_policies(None)}
        return Response(data, content_type='application/json', status=200)
    answer1 = reqdata['answer1']
    answer2 = reqdata['answer2']
    answer3 = reqdata['answer3']
    answer4 = reqdata['answer4']
    answer5 = reqdata['answer5']

    data = None
    if ((answer1 is not None) and (answer2 is not None) and (answer3 is not None) and (answer4 is not None) and (
            answer5 is not None)):
        answer = (answer1 + answer2 + answer3 + answer4 + answer5) % 5
        if answer == 0:
            answer = random.randint(1, 5)
        data = get_policies(answer)
    else:
        data = {'policies': get_policies(None)}

    return Response(data, content_type='application/json', status=200)


def get_policies(rating: int):
    policy1 = {'id': 1,
               'name': 'LIC Suraksha Bima',
               'description': 'The theory specializes a cigarette without the polished mercury. '
                              'A liquor chooses inside the luggage! Can a feasible courage punt? '
                              'Will a defined thumb work? A recommended sunrise relays a politician near the stressed cake. '
                              'A trifle overloads a freedom.',
               'image': 'https://www.licindia.in/CorporateSiteDemo/media/LIC_Media/LIC_LOGO.png'}
    policy2 = {'id': 2,
               'name': 'ICICI Prudential',
               'description': 'The dictionary elaborates in a recovery. The biscuit flashes. '
                              'The agenda migrates after the absolute.'
                              ' An important news bounces across the workable room. An epic kingdom indulges.',
               'image': 'https://www.iciciprulife.com/content/icici-prudential-life-insurance/_jcr_content/headerpar/header_sightly/navHeader.img.png/1533272453567.png'}
    policy3 = {'id': 3,
               'name': 'Bajaj Allianz',
               'description': 'An expanded bulletin bringings a supreme turnround. '
                              'The unlucky microcomputer invalidates the centered duplicate.'
                              ' The controlling aircraft waffles behind each negotiable spray. '
                              'The load sweeps before a flute!',
               'image': 'https://www.bajajallianz.com/Corp/images/logo.jpg'}
    policy4 = {'id': 4,
               'name': 'TATA Aig',
               'description': 'A snobbery poses as the width. When can any audio notice the supreme? '
                              'Will our pump rush toward its spoilt correspondence? '
                              'A muttering wrap budgets the mouth. The landscape squeezes whatever outer tear.',
               'image': 'https://www.tataaig.com/content/dam/tagic/images/LOGO.png'}
    policy5 = {'id': 5,
               'name': 'MaxBupa',
               'description': 'A career burns with a snobbery. Will the joined geography knock over a drunken thoroughfare? '
                              'The killing disregard trashes her oar. The counterpart purges opposite the silicon. '
                              'Each above charter bundles the fun inverse.',
               'image': 'https://www.maxbupa.com/Style%20Library/MaxBupa/images/GAHome/mb-logo.png'}

    if rating is None:
        return [policy1, policy2, policy3, policy4, policy5]
    elif rating == 1:
        return policy1
    elif rating == 2:
        return policy2
    elif rating == 3:
        return policy3
    elif rating == 4:
        return policy4
    elif rating == 5:
        return policy5
