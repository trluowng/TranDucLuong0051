import xml.dom.minidom
# Tải và phân tích file XML
dom = xml.dom.minidom.parse("sample.xml")
# Lấy nút gốc
company = dom.documentElement #trả về company 
# Lấy tên công ty
name = company.getElementsByTagName("name")[0].childNodes[0].data
print("Tên công ty:", name)

