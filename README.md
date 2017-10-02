# custom-blog-theming
This is a blog implemented using Django, where the user can change de color scheme of the app. This app can be found at [custom-blog-theming.herokuapp.com](custom-blog-theming.herokuapp.com) and you can login with `john_snow/john1234`.

## Development
To run this project locally, you'll need to have Python 3.6, Pip and PostgreSQL installed and follow these steps:
1. Create a virtual env for the project
2. Install requirements by running `pip install -r requirements.txt`
3. Create the database and add correct config in `settings.py`
3. Inside `customblog` folder, run `python manage.py migrate`
4. Run `python manage.py runserver` to run locally
