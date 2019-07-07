# Policies

Policies is heroku hosted simple recommendation django api. 

  - Post a request with answers.
  - Recommends the policy best suited on basis of it.
  - Also provides list of policies.


## API
Link
```sh
https://polies.herokuapp.com
```

Post Api : /policies

```sh
{"answer1":1,"answer2":2,"answer3":1,"answer4":2,"answer5":3}
```
Response
```sh
{
    "id": 4,
    "name": "TATA Aig",
    "description": "A snobbery poses as the width. When can any audio notice the supreme? Will our pump rush toward its spoilt correspondence? A muttering wrap budgets the mouth. The landscape squeezes whatever outer tear.",
    "image": "https://www.tataaig.com/content/dam/tagic/images/LOGO.png"
}
```

Response for list of Policies when no answers pass.

```sh
{
    "policies": [
        {
            "id": 1,
            "name": "LIC Suraksha Bima",
            "description": "The theory specializes a cigarette without the polished mercury. A liquor chooses inside the luggage! Can a feasible courage punt? Will a defined thumb work? A recommended sunrise relays a politician near the stressed cake. A trifle overloads a freedom.",
            "image": "https://www.licindia.in/CorporateSiteDemo/media/LIC_Media/LIC_LOGO.png"
        },
        {
            "id": 2,
            "name": "ICIC Lombard",
            "description": "The dictionary elaborates in a recovery. The biscuit flashes. The agenda migrates after the absolute. An important news bounces across the workable room. An epic kingdom indulges.",
            "image": "https://www.icicilombard.com/feo-cdn/R/4/2Ll5vONmo.webp"
        },
        {
            "id": 3,
            "name": "Bajaj Allianz",
            "description": "An expanded bulletin bringings a supreme turnround. The unlucky microcomputer invalidates the centered duplicate. The controlling aircraft waffles behind each negotiable spray. The load sweeps before a flute!",
            "image": "https://www.bajajallianz.com/Corp/images/logo.jpg"
        },
        {
            "id": 4,
            "name": "TATA Aig",
            "description": "A snobbery poses as the width. When can any audio notice the supreme? Will our pump rush toward its spoilt correspondence? A muttering wrap budgets the mouth. The landscape squeezes whatever outer tear.",
            "image": "https://www.tataaig.com/content/dam/tagic/images/LOGO.png"
        },
        {
            "id": 5,
            "name": "MaxBupa",
            "description": "A career burns with a snobbery. Will the joined geography knock over a drunken thoroughfare? The killing disregard trashes her oar. The counterpart purges opposite the silicon. Each above charter bundles the fun inverse.",
            "image": "https://www.maxbupa.com/Style%20Library/MaxBupa/images/GAHome/mb-logo.png"
        }
    ]
}
```

## Steps

Polcies uses Django and django rest framework for the api.

* Step1: setup python, django and drf
* Step2: write api
* Step3: freeze requirements.
* Step4: runserver 0.0.0.0:8000 and test api.
* Step5: create Procfile with command :
```sh
web: python policies/manage.py runserver 0.0.0.0:$PORT
```
* Step6:create runtime.txt
* Step7: install gunicorn and whitenose
* Step8: update settings.py with static variables.
* Step9: init git if not initated previously
* Step10: run cli heroku
* Step11: Login to your heroku account
* Step12: Create an app on heroku
* Step13: Run Commit for the project
* Step14: push the commit on heroku app you created.
