#!/usr/bin/python3

import os
import csv

dict_districts = {
    "Hai_Chau": "Hải Châu",
    "Cam_Le": "Cẩm Lệ",
    "Hoa_Vang": "Hòa Vang",
    "Lien_Chieu": "Liên Chiểu",
    "Ngu_Hanh_Son": "Ngũ Hành Sơn",
    "Son_Tra": "Sơn Trà",
    "Thanh_Khe": "Thanh Khê",
    "THCS_Nguyen_Khuyen": ""
}

dict_schools = {
    "Nguyen_Cong_Tru": "THCS Nguyễn Công Trứ",
    "Tran_Quy_Cap": "THCS Trần Quý Cáp",
    "Nguyen_Van_Linh_CLE": "THCS Nguyễn Văn Linh",
    "Nguyen_Thien_Thuat": "THCS Nguyễn Thiện Thuật",
    "Nguyen_Thi_Dinh": "THCS Nguyễn Thị Định",
    "Dang_Thai_Mai": "THCS Đặng Thai Mai",
    "Kim_Dong": "THCS Kim Đồng",
    "Le_Hong_Phong": "THCS Lê Hồng Phong",
    "Ly_Thuong_Kiet": "THCS Lý Thường Kiệt",
    "Le_Thanh_Ton": "THCS Lê Thánh Tôn",
    "Nguyen_Hue": "THCS Nguyễn Huệ",
    "Sao_Nam": "THCS Sào Nam",
    "Tay_Son": "THCS Tây Sơn",
    "Tran_Hung_Dao": "THCS Trần Hưng Đạo",
    "Trung_Vuong": "THCS Trưng Vương",
    "Skyline": "Sky Line",
    "Nguyen_Ba_Phat": "THCS Nguyễn Bá Phát",
    "Tran_Quoc_Tuan": "THCS Trần Quốc Tuấn",
    "Nguyen_Tri_Phuong": "THCS Nguyễn Tri Phương",
    "Do_Thuc_Tinh": "THCS Đỗ Thúc Tịnh",
    "Nguyen_Van_Linh_HVA": "THCS Nguyễn Văn Linh",
    "Nguyen_Hong_Anh": "THCS Nguyễn Hồng Ánh",
    "Nguyen_Phu_Huong": "THCS Nguyễn Phú Hường",
    "Ong_Ich_Duong": "THCS Ông Ích Đường",
    "Nguyen_Viet_Xuan": "THCS Nguyễn Viết Xuân",
    "Pham_Van_Dong": "THCS Phạm Văn Đồng",
    "Tran_Quang_Khai": "THCS Trần Quang Khải",
    "Luong_The_Vinh": "THCS Lương Thế Vinh",
    "Nguyen_Binh_Khiem_LCH": "THCS Nguyễn Bỉnh Khiêm",
    "Nguyen_Thai_Binh": "THCS Nguyễn Thái Bình",
    "Le_Anh_Xuan": "THCS Lê Anh Xuân",
    "Ngo_Thi_Nham": "THCS Ngô Thì Nhậm",
    "Dam_Quang_Trung": "THCS Đàm Quang Trung",
    "Nguyen_Luong_Bang": "THCS Nguyễn Lương Bằng",
    "Nguyen_Binh_Khiem_NHS": "THCS Nguyễn Bỉnh Khiêm",
    "Le_Loi": "THCS Lê Lợi",
    "Huynh_Ba_Chanh": "THCS Huỳnh Bá Chánh",
    "Tran_Dai_Nghia": "THCS Trần Đại Nghĩa",
    "Quoc_Te_Singapore": "Quốc Tế Singapore",
    "Nguyen_Khuyen": "THCS Nguyễn Khuyến",
    "Cao_Thang": "THCS Cao Thắng",
    "Le_Do": "THCS Lê Độ",
    "Ly_Tu_Trong": "THCS Lý Tự Trọng",
    "Nguyen_Chi_Thanh": "THCS Nguyễn Chí Thanh",
    "Nguyen_Van_Cu": "THCS Nguyễn Văn Cừ",
    "Phan_Boi_Chau": "THCS Phan Bội Châu",
    "Pham_Ngoc_Thach": "THCS Phạm Ngọc Thạch",
    "Chu_Van_An": "THCS Chu Văn An",
    "Hoang_Dieu": "THCS Hoàng Diệu",
    "Huynh_Thuc_Khang": "THCS Huỳnh Thúc Kháng",
    "Le_Thi_Hong_Gam": "THCS Lê Thị Hồng Gấm",
    "Nguyen_Dinh_Chieu": "THCS Nguyễn Đình Chiểu",
    "Nguyen_Duy_Hieu": "THCS Nguyễn Duy Hiệu",
    "Nguyen_Thi_Minh_Khai": "THCS Nguyễn Thị Minh Khai",
    "Nguyen_Trai": "THCS Nguyễn Trãi",
    "Phan_Dinh_Phung": "THCS Phan Đình Phùng",
    "Do_Dang_Tuyen": "THCS Đỗ Đăng Tuyển"
}
dict_testsite = {
    "THCS NGUYỄN KHUYẾN": "THCS Nguyễn Khuyến",
    "THPT TRẦN PHÚ": "THPT Trần Phú",
    "THPT CHUYÊN LÊ QUÝ ĐÔN": "THPT chuyên Lê Quý Đôn"
}
dict_subject={
    'Tiếng anh': 'Tiếng Anh',
    'Tiếng nhật': 'Tiếng Nhật',
    'Tiếng pháp': 'Tiếng Pháp'
}
for district in dict_districts.keys():
    for school in os.listdir(district):
        if school[:-4] in dict_schools:
            with open(os.path.join(district, school), "r", newline='') as f:
                raw_data = csv.reader(f, strict=True)
                contestants = []
                for row in raw_data:
                    contestants.append([s.strip() for s in row])
            with open(os.path.join(district, school), "w", newline='') as f:
                for contestant in contestants:
                    if contestant[5] in ['Hồ Chí Minh', 'TP Hồ Chí Minh', 'TP.Hồ Chí Minh', 'TP.HCM']:
                        contestant[5] = "TP. Hồ Chí Minh"
                    if contestant[5] in ['Q Nam', 'Quãng  Nam', 'Quảng  Nam']:
                        contestant[5] = 'Quảng Nam'
                    if contestant[5] in ['TT. Huế', 'TT-Huế', 'Huế', 'Thừa Thiên-Huế', 'Thừa Thiên- Huế', 'Thừa Thiên Huế']:
                        contestant[5] = 'Thừa Thiên - Huế'
                    if contestant[5] in ['Đăk Lăk']:
                        contestant[5] = 'Đắk Lắk'
                    #contestant[6] = dict_testsite[contestant[6]]
                    if contestant[8] in dict_subject:
                        contestant[8]=dict_subject[contestant[8]]
                    contestant[3] = '"' + contestant[3].replace(".", "/") + '"'
                    contestant[4] = contestant[4].replace('.', '/')
                    if contestant[10] == "":
                        contestant[10] = '""'
                    f.write(",".join(contestant) + "\n")
