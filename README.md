RabbitMQ
========

[![Build Status](https://travis-ci.org/joshbenner/ansible-role-rabbitmq.svg?branch=master)](https://travis-ci.org/joshbenner/ansible-role-rabbitmq)

Install and configure RabbitMQ, including clustering.

See defaults file for configuration options.

Simple RabbitMQ Node
--------------------

```yaml
- hosts: rabbit-server
  become: yes
  roles:
    - role: joshbenner.rabbitmq
      rabbitmq_users:
        joe:
          password: changeme
          read_priv: .*
```

RabbitMQ Cluster
----------------

```yaml
- hosts: rabbit-servers
  become: yes
  roles:
    - role: joshbenner.rabbitmq
      rabbitmq_cluster_nodes:
        - host: rabbit1.example.com
        - host: rabbit2.example.com
        - host: rabbit3.example.com
          ip: 1.2.3.4
```

Or, if you are adventurous (requires Python jmespath package):

```yaml
- hosts: rabbit-servers
  become: yes
  roles:
    - role: joshbenner.rabbitmq
      rabbitmq_cluster_nodes: |
        {{
          groups['rabbit-servers'] | map('extract', hostvars) | list
          | json_query('[].{host: ansible_fqdn}')
        }}
```

License
-------

BSD
