def test_homePageView(client):
	response=client.get('/')
	assert response.status_code==200
	assert response.content == b'Hello World'


