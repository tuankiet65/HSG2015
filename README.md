#Bảng điểm Học sinh giỏi thành phố Đà Nẵng năm 2015

##Nguồn:
 * [Các trường thuộc Phòng Giáo dục](http://danang.edu.vn/danang/UserFiles/file/Thi2015/THCS%20thuoc%20cac%20PGD.rar)
 * [THCS Nguyễn Khuyến](http://danang.edu.vn/danang/UserFiles/file/Thi2015/THCS%20NGUYEN%20KHUYEN.pdf)

Các dữ liệu trong PDF được extract sang CSV bằng [Tabula](http://tabula.technology)

##Cấu trúc:
```
├── <Thư mục của các quận, tên không dấu, dấu cách thay bằng gạch dưới>
│   ├── <File điểm của các trường thuộc quận, tên không dấu, dấu cách thay bằng gạch dưới, định dạng CSV>
│   └── <File PDF nguyên gốc>
├── merge.py (Chương trình Python để tập hợp dữ liệu)
├── std.py (Chương tình Python để "làm đẹp" dữ liệu gốc sau khi đổi từ PDF sang CSV)
├── merged.csv (Dữ liệu đã tập hợp)
└── README.md (File này)
```

## Giấy phép: Public Domain
