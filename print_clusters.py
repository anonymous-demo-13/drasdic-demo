import os
import json

def get_cluster_data(base_dir):
    cluster_data = {}
    # Iterate over each item in the base directory.
    for cluster in os.listdir(base_dir):
        cluster_path = os.path.join(base_dir, cluster)
        if os.path.isdir(cluster_path):
            # List only files in this cluster directory.
            files = [f for f in os.listdir(cluster_path) if os.path.isfile(os.path.join(cluster_path, f))]
            files.sort()  # sort alphabetically if desired
            cluster_data[cluster] = files
    return cluster_data

if __name__ == '__main__':
    base_dir = "audio/clusters"
    data = get_cluster_data(base_dir)
    # Format as a JS constant
    js_constant = "const clusterData = " + json.dumps(data, indent=2) + ";"
    print(js_constant)
