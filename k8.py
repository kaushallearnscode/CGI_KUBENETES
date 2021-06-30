#!/usr/bin/python3
    

import cgi
import subprocess
                
print("content-type: text/html")
print()
                            

mydata = cgi.FieldStorage()
mys = mydata.getvalue("s")
myx = mydata.getvalue("x")
myy = mydata.getvalue("y")
myz = mydata.getvalue("z")


cmd1 = "sudo kubectl get {} --kubeconfig admin.conf".format(myx)
cmd2 = "sudo kubectl run {} --image={} --kubeconfig admin.conf ".format(myx,myy)
cmd3 = "sudo kubectl create deployment {} --image={} --kubeconfig admin.conf".format(myx,myy)
cmd4 = "sudo kubectl expose {} {} --port={} --type=NodePort --kubeconfig admin.conf".format(myx,myy,myz)
cmd5 = "sudo kubectl scale deployment {} --replicas={} --kubeconfig admin.conf ".format(myx,myy)
cmd6 = "sudo kubectl delete all --all --kubeconfig admin.conf"
cmd7 = "sudo kubectl delete {} {} --kubeconfig admin.conf".format(myx,myy)

if('launch'in mys ) and ('pod' in mys):
    output = subprocess.getoutput(cmd2)
elif('run' in mys) and ('deployment'in mys):
    output = subprocess.getoutput(cmd3)
elif('scale' in mys) and ('deployment' in mys):
    output = subprocess.getoutput(cmd5)
elif('expose' in mys):
    output = subprocess.getoutput(cmd4)
elif('all' in mys) and ('delete' in mys):
    output = subprocess.getoutput(cmd6)
elif('delete' in mys):
    output = subprocess.getoutput(cmd7)
elif('show' in mys):
    output = subprocess.getoutput(cmd1)
print(output)
