import sys
import subprocess
import os

localImages = os.environ['DOCKER_LOCAL_IMAGES'].strip().split(',')
remoteImages = os.environ['DOCKER_REGISTRY_REMOTE_IMAGES'].strip().split(',')

for i, localImage in enumerate(localImages):
    tag = 'docker tag {}:latest {}:{}'.format(localImage, remoteImages[i], os.environ['BUILD_NUMBER'])
    print(tag)
    process1 = subprocess.Popen(tag.split(), stdout=subprocess.PIPE)
    output1, error1 = process1.communicate()
    print (output1)

    push = 'docker push {}:{}'.format(remoteImages[i], os.environ['BUILD_NUMBER'])
    print(push)
    process2 = subprocess.Popen(push.split(), stdout=subprocess.PIPE)
    output2, error2 = process2.communicate()
    print (output2)
