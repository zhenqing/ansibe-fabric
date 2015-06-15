from fabric.api import *
prod_host ="52.10.23.27"

def prepare_env():
    env.hosts = [prod_host]
    env.username = "ubuntu"

def prepare_deploy():
    run("touch helloworld")
