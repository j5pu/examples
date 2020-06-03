# ansible_vars_consul
Ansible vars plugin, to get inventory configuration variables from Hashicorp Consul KV store.


## Usage

Consul KV store should contain tree structure, starting in 'inventory-json' folder, for example:
```
/inventory-json/common/foo:bar - configuration level common to all inventories and projects.
/inventory-json/pgsql/bar:baz- configuration level for all hosts in 'pgsql' group.
/inventory-json/dev/common/foo:xyz - configuration level common for all hosts in 'dev' project.
/inventory-json/dev/redis/param:redis-dev - configuration level common for all hosts in group 'redis' of 'dev' project.
```

The script will merge all parameters in abovementioned order, so mode specific config will take precedence over common config.


Only configration parameter needed - Consul URL, set in CONSUL_KV_URL parameter inside of VarsModule class.


Inventory example:
```
[all:vars]
# this is project name for importing project-level variables
project=cool_project

[backend]
192.168.1.215 hostname=back-05
192.168.1.216 hostname=back-06

[service]
192.168.1.217 hostname=service-06
192.168.1.218 hostname=service-07

[cron]
192.168.1.39 hostname=cron-01
192.168.1.40 hostname=cron-02
```
Group names backend/service/cron is used to import group-level variables.


PR's are welcome.



