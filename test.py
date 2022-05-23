import hvac

client = hvac.Client(
    url='http://172.17.0.12:8200',
    token='aiphohTaa0eeHei'
)
client.is_authenticated()

client.secrets.kv.v2.create_or_update_secret(
    path='hvac',
    secret=dict(netology='Big secret!!!'),
)

print(client.secrets.kv.v2.read_secret_version(
    path='hvac',
))
