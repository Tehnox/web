sudo ln -sf "${PWD}/etc/nginx.conf"  "/etc/nginx/sites-enabled/default"
sudo /etc/init.d/nginx restart

pkill gunicorn
gunicorn hello_module:hello_app -c "${PWD}/etc/hello.conf.py"

GUNICORN_DJANGO_CONFIG_PATH="${PWD}/etc/django.conf.py"
cd ask || exit
gunicorn ask.wsgi -c "${GUNICORN_DJANGO_CONFIG_PATH}"
