import boto3
import base64
import docker

session = boto3.Session()
ecr = session.client('ecr')
login = ecr.get_authorization_token()
b64token = login['authorizationData'][0]['authorizationToken'].encode('utf-8')
username, password = base64.b64decode(b64token).decode('utf-8').split(':')
registry = login['authorizationData'][0]['proxyEndpoint']

client = docker.from_env()
client.login(username, password, registry=registry)


img_id ='credsite/testdjangoproject'
img, logs = client.images.build(path='.', tag=img_id)
registry_with_name = registry.replace('https://', '') + '/' + img_id
img.tag(registry_with_name, tag='latest2')
client.images.push(registry_with_name, tag='latest2')
