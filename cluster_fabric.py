from fabric.api import *
prod_host =["172.31.18.63","172.31.24.154"]

def prepare_env():
    env.hosts = prod_host
    env.username = "opencfp"

def composer_install():
    run("php composer.phar install")

def db_migration():
    run("vendor/bin/phinx migrate --environment=production")

def run_phpunit():
    run("./vendor/bin/phpunit")

def update_app():
    with cd('/var/www/html/opencfp'):
        composer_install()
        db_migration()
        run_phpunit()
