ssh_cmd="ssh ln_app_root"
if [ -z "$1" ]
then
    $ssh_cmd
else
    ssh_cmd=${ssh_cmd/root/$1}
    $ssh_cmd
fi