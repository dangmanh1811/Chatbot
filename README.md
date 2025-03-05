# 🤖 Chatbot Demo - Gemini API & MongoDB Atlas Integration
## Giới thiệu
Dự án chatbot demo được xây dựng nhằm mục đích thử nghiệm và trình diễn các tính năng sau:

* Kết nối và lấy dữ liệu từ Gemini API để trả lời câu hỏi tự động.
* Tích hợp MongoDB Atlas để lưu trữ thông tin người dùng.
* Triển khai giao diện bằng Streamlit để tương tác trực tiếp trên trình duyệt.
* Dự án phù hợp để làm mẫu tích hợp chatbot AI cơ bản với khả năng mở rộng vào các hệ thống thực tế như hỗ trợ khách hàng, tư vấn sức khỏe tâm lý, hay các hệ thống hỏi đáp.

## Công nghệ sử dụng
* Python	Ngôn ngữ lập trình chính
* Streamlit	Xây dựng giao diện web
* Gemini API Nguồn cung cấp dữ liệu AI trả lời
* MongoDB Atlas	Lưu trữ thông tin người dùng, lịch sử chat
* Pymongo	Kết nối MongoDB với Python

## ⚙️ Cài đặt

1️. Clone project
```bash
    git clone https://github.com/dangmanh1811/Chatbot.git 
```

```bash
    cd chatbot-gemini-mongodb 
```


2️. Cài đặt thư viện
 ```bash
    pip install -r requirements.txt
 ```

3️. Thêm file cấu hình .env
Tạo file .env ở thư mục gốc với nội dung:
```bash
    GEMINI_API_KEY=[your_gemini_api_key]
    MONGODB_URI=[your_mongodb_uri]
```


## Chạy dự án
```bash
    streamlit run app.py
```
