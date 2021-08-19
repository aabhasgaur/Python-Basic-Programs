priceOfCameras={"Sony":500,"Nikon":700,"Cannon":1100}
print(priceOfCameras)
#print(priceOfCameras["Sony"])
#print(priceOfCameras["Cannon"])
priceOfCameras["Nikon"]=800
print(priceOfCameras.keys())

copyOfPriceOfCameras=priceOfCameras.copy()
print(copyOfPriceOfCameras)

del copyOfPriceOfCameras["Sony"]
print(copyOfPriceOfCameras)

copyOfPriceOfCameras.clear()
print(copyOfPriceOfCameras)
