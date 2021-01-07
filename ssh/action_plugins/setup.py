from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        def lookup(obj, path):
            return reduce(dict.get, path.split('.'), obj)

        result = super(ActionModule, self).run(tmp, task_vars)

        myfilter = self._task.args.get('myfilter', None)

        module_args = self._task.args.copy()
        if myfilter:
            module_args.pop('myfilter')

        module_return = self._execute_module(module_name='setup', module_args=module_args, task_vars=task_vars, tmp=tmp)

        if not module_return.get('failed') and myfilter:
            return {"changed":False, myfilter:lookup(module_return['ansible_facts'], myfilter)}
        else:
            return module_return

# https://stackoverflow.com/questions/40181291/ansible-ad-hoc-command-filter-json-output-by-key-or-property
