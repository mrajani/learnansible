# Docker on Ubuntu LTS

This playbook will install Docker an Ubuntu machine, with the options specified in the `vars.yml` variable file.

## Settings

- `users`: number of user to create.
- `ssh_key_file`: default ssh key for users.
- `docker_version`: named docker version to install.


## Running this Playbook

Quick Steps:

### 1. Obtain the playbook
```shell
git clone https://github.com/mrajani/learnansible.git
cd learnansible/docker
```

### 2. Customize Options

```shell
vi vars.yml
```

```yml
#vars.yml
---
users:
  - ansible
  - docker
ssh_key_file: ~/.ssh/lnxa_rsa
docker_version: 5:19.03.13~3-0~ubuntu-focal
```

### 3. Run the Playbook

```command
ansible-playbook -l [target] -i [inventory file] -u [remote user] playbook.yml
```

