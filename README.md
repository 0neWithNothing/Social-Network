# Social Network
This is a twitter like application

## Functionality
* Register/login user system
* Manage profile data
* Creating new posts
* Like and comment posts
* Add to friend with friend request
* Real time chat on WebSockets
* Simple search

### Installation
1. Copy repository
2. Create and activate virtual enviroment </br>
`python3 -m venv venv` </br>
`source venv/bin/activate` or `venv\Scripts\activate` for windows
3. Install requirements </br>
`pip install -r requirements.txt`
4. Run migrations </br>
`python manage.py makemigrations` </br>
`python manage.py migrate`
5. Run `python manage.py runserver`
6. Go to [localhost:8000](http://127.0.0.1:8000)
#### Have 2 users for testing (if you don't want to register with email confirmation):
- Login: `Maxim`, Password: `qweasdzxc22`
- Login: `Alex`, Password: `qweasdzxc22`
