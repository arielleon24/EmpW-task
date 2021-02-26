# EmpWorks-task
This project is a task for Empathy Works to test my ability to learn Django

- Run server with the command: **python manage.py runserver**
- Once server is running you can visit it with: http://127.0.0.1:8000/  
    8000 is the default but this can be changed when running it by adding the desired port as a command line arg. EX: **python manage.py runserver 8080**
  
- If you want to change the server’s IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use: **python manage.py runserver 0:8000** 
  (0 is a shortcut for 0.0.0.0. Full docs for the development server can be found in the runserver reference.)
  
Guide to make model (DB) changes:

-change your models (in **models.py**)

-run **python manage.py makemigrations** to create migrations for those changes

-run **python manage.py migrate** to apply those changes to the database

