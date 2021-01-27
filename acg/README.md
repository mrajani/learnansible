export VAULT_DEV_ROOT_TOKEN_ID=mytoken
export VAULT_ADDR='http://127.0.0.1:8200'


vault policy list
vault policy read default
vault policy write dev-policy dev-policy.hcl
vault auth enable userpass
vault write auth/userpass/users/appuser password=password policies=dev-policy

