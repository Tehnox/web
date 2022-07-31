sudo ln -sf "${PWD}/etc/nginx.conf"  "/etc/nginx/sites-enabled/default"
sudo /etc/init.d/nginx restart

pkill gunicorn
gunicorn hello_module:hello_app -c "${PWD}/etc/hello.conf.py"

cd ask || exit
gunicorn ask.wsgi -c "${PWD}/etc/django.conf.py"
