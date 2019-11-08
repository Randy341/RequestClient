from unittest import TestCase
from RequestClient.RestRequestClient import RestRequestClient

if __name__ == "__main__":

    baseURL = ""    #change this to your own for testing

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