#(Wipro’s client eBay wants to run a campaign on their website, which will have the following parameters, eBay wants that on certain x products,
#they want to calculate the final price, for each product on eBay there will be a stock unit parameter, this parameter will denote, how many items
#are their in their fulfillment center  Now, while these numbers if are positive means product x is available in the fulfillment center and if not
#than the product is not available and cannot be shipped to the customer Now the price on for each product varies based on the distance of the customer
#from the fulfillment center. Now, each product is in different fulfillment zone. Now, these values are 00’s kms for each centurion km. The price
#available would further increase by factor distance. You’ve to find the maximum discount price for each product if the product can be shipped.)


no_of_products=int(input("Enter the number of products: "))
list_price=list(input().split(" "))
list_distance=list(input().split(" "))
list_sku=list(input().split(" "))
list_final=[]
for item in range(0,no_of_products):
    if int(list_sku[item]) >0 :
        temp = int(list_price[item])*int(list_distance[item])
        list_final.append(temp)

for item in range(0,len(list_final)):
    print(list_final[item], sep=" ",end=" ")
