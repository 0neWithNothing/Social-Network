# MeeDee
MeeDee is a simple social network app where users can follow friends and discover new ones. On MeeDee, users can make posts with text and images, and other users can like and comment on these posts. Also users can send messages to each other in real time.

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
4. Run `python manage.py runserver`
5. Go to [localhost:8000](http://127.0.0.1:8000)
#### Have 2 users for testing:
- Login: `Maxim`, Password: `qweasdzxc22`
- Login: `Alex`, Password: `qweasdzxc22`
#### **On Chat page you will see only your friends!**
