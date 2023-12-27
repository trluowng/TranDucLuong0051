import xml.dom.minidom
# Tải và phân tích file XML
dom = xml.dom.minidom.parse("sample.xml")
# Lấy nút gốc
company = dom.documentElement #trả về company 
# Lấy thông tin về nhân viên
staffs = company.getElementsByTagName("staff")
for staff in staffs:
    id = staff.getAttribute("id")    
    name = staff.getElementsByTagName("name")[0].childNodes[0].data
    #sử dụng childnodes[0] để lấy nút con của pahanf tử Name, sử dụng [0] để lấy phần thử đầu tiên

    salary = staff.getElementsByTagName("salary")[0].childNodes[0].data

    print("Nhân viên (ID:{}) - Tên: {}, Lương: {}".format(id, name, salary))