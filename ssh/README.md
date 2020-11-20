### Create SSH KEY pair for ACG

### Copy ssh pub key to all the hosts

ansible-playbook ssh_keygen.yml
ansible-playbook -k -K ssh_copyid.yml

