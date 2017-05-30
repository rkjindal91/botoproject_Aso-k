import boto3
client = boto3.client(
		'iam',)
client_list = client.list_users()
users = client_list['Users']
policy names = []
def get_auth(marker=None):
	if marker is None:
			get_auth = client.get_account_authorization_details(Filter=['User'])
	else:
			get_auth = client.get_account_authorization_details(Filter=['User'], Marker=marker)
	return get_auth

ga = get_auth()
list_of_ga = []
marker = []

list_of_ga.append(ga)

if ga['IsTruncated'] is True:
	marker.append(ga['Marker'])

while len(marker) > 0:
	g_auth = get_auth(marker[0])
	list_of_ga.append(g_auth)
	marker.pop()
	if g_auth['Istruncated'] is True:
		marker.append(ga['Marker'])

user_detail_list = []
with open('names.csv', 'w') as csvfile:
	fieldnames = ['UserName', 'Inline Policies', 'Managed Policies', 'Group List']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for a in list_of_ga:
		for item in a['UserDetailList']:
			if 'UserPolicyList' in item:
				plist = item['UserPolicyList']
			else: 
				plist = 'Blank'
			writer.writerow({
				'UserName' : item['UserName'],
				'Inline Policies' : plist, 
				'Managed Policies': item['AttachedManagedPolicies'],
				'Group List' : item['GroupList']
})