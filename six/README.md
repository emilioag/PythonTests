# Six

## Build the container

```bash
docker build -t six .
```

## Running the api
```bash
docker run --rm --name six -p 8000:8000 -it six
```

```bash
No changes detected
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
Username (leave blank to use 'root'): admin
Email address:  
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 02, 2019 - 09:55:33
Django version 2.2, using settings 'jwtauthexample.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

Set the user and password for root and then the server will be run at http://0.0.0.0:8000.