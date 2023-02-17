import boto3


client = boto3.client('eks', region_name='us-east-2')
clusters = client.list_clusters()['clusters']

for cluster in clusters:
    response = client.describe_cluster(
        name=cluster
    )
    cluster_info = response['cluster']
    cluster_status = cluster_info ['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']

    print(f"cluster {cluster} status is {cluster_status}")
    print(f"cluster endpoint: {cluster_endpoint}")
    print(f"cluster version is: {cluster_version}")

