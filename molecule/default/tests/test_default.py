import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rabbit_service(host):
    service = host.service('rabbitmq-server')
    assert service.is_running
    assert service.is_enabled


def test_rabbit_listening(host):
    assert host.socket('tcp://0.0.0.0:5672').is_listening
    assert host.socket('tcp://0.0.0.0:5671').is_listening


def test_rabit_management_listening(host):
    assert host.socket('tcp://0.0.0.0:15672').is_listening


def test_config_file(host):
    f = host.file('/etc/rabbitmq/rabbitmq.config')
    assert f.is_file
    assert f.user == 'rabbitmq'
    assert f.group == 'rabbitmq'
    assert f.mode == 0o644
    assert f.contains('connection, info')


def test_env_file(host):
    f = host.file('/etc/rabbitmq/rabbitmq-env.conf')
    assert f.is_file
    assert f.user == 'rabbitmq'
    assert f.group == 'rabbitmq'
    assert f.mode == 0o644
    assert f.contains('RABBITMQ_NODENAME="rabbit"')


def test_users(host):
    out = host.check_output('rabbitmqctl list_users')
    assert 'joe' in out
    assert 'guest' not in out
