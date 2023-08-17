import xml.etree.ElementTree as ET
#匯入xml函式庫，並命名為ET
def xml_to_dict(element):   #把xml轉換為dictionary的函式
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = xml_to_dict(child)
    return result
tree = ET.parse("setting.xml") #讀取設定檔
root = tree.getroot() #獲取裡面的資料
data = xml_to_dict(root) #把資料轉化為dictionary處理
money = int(data["money"]) #輸入
interest = int(data["interest"])
month = int(data["month"])
#輸入的東西一律化為整數
total = 0
for  i in range(month):
    total = total + money
    money = money + money * interest /100
result = open("result.txt","w",encoding="utf-8")    #建立儲存最終數據的檔案
result.write("你最後剩下的錢為:"+str(int(total)))     #寫入數據
result.close()  #關閉檔案
print(int(total))   #輸出總金額