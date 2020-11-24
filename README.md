# Eat4Wellness

This project was built for my CPTR 460 - Software Engineering class.

The Eat4Wellness webapp allows members to record their meals into a personal diet log, replacing conventional paper-based solutions.
Eat4Wellness health coaches are able to access their assigned members' diet logs to analyze their nutrition.

## Live Deployment

Test out the app's functionality at [Heroku](https://eat4wellness-arn.herokuapp.com/homepage/)

## Frameworks
[Django 3.1](https://www.djangoproject.com/)

[Materialize 1.0.0](https://materializecss.com/)

[jQuery 3.5.1](https://jquery.com/)

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the dependencies listed in requirements.txt (includes some packages for deploying to Heroku).

```bash
pip install -r requirements.txt
```

Run database migrations using

```bash
python manage.py migrate
```

## Usage

### Test Users

```bash
python manage.py loaddata test_users.json
```

Test users include (username : password):
 - member : 123456
 - coach : 123456
 - admin : 123456
 - superadmin : 123456
 
The superadmin has access to the Django Admin site.

### API Key

Eat4Wellness uses the USDA's [FoodData Central](https://fdc.nal.usda.gov/) API to get food and nutritional information.

To run this app, follow the link above to register for a data.gov API key.
You can either add this key as 
 - an environment variable to using the environment key `'API_KEY'`
 
or

 - Modify `api_key_blank.py` and replace `[Your API Key Here]` with your key. Then rename `api_key_blank.py` to `api_key.py`
