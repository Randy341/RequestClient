##  Request Client 
An easy-to-use and convenient Python3 library for HTTP REST API request and GraphQL request.
This library is a wrapper around Python request library and the original GQL library.   

Currently supports Rest API method:
- Get
- Post
- Delete

NOTE: KeepAlive and Connection Pool is ON by default for Rest Client.  As the wrapper uses request session object to initiate request.

Future improvements:
- Support Rest Put and Patch
- Add documentations


## Python3 (Install)  
Requirements:
- Python3 (version 3.7 or above)
- Pip3
```bash
pip3 install RequestClient
````

## Usage (Python3)
```python
from RequestClient.RestRequestClient import RestRequestClient
from unittest import TestCase    

baseURL = "https://www.fictional-company.com/apis/v2"    #change this to your own for testing

client = RestRequestClient(baseUrl=baseURL,sslverify=False,defaultHeaders={"x-admin":"true"})

store98 = client.get("/store/list", params={"id":"98"}).content
TestCase.assertTrue(store98["stores"]["store"][0]["id"] == 98 , "GET Test Failed")

category2 = client.post("/category/2", payload={"category": {"name":"Testing123", "modifiedBy":"Randy"}})
print(category2.type)
TestCase.assertEqual(category2.content["category"][0]["name"], "Testing123", "Post Raw Python Dictionary Failed")

store45 = client.get("/store/45")
store45 = store45.object()
TestCase.assertTrue(store45.store[0].id == 45, "Object Conversion test failed")

category5 = client.get("/category/5")
category5 = category5.object()
TestCase.assertTrue(category5.category[0].status == "Published", "Object Conversion test failed")

print("Yah! All tests pass!")
```

    
    

