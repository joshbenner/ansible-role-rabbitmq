import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cluster(host):
    out = host.check_output('rabbitmqctl cluster_status')
    assert 'rabbit1' in out
    assert 'rabbit2' in out
