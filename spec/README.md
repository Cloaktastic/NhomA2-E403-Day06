## Track, product/app và user

**Track:** Food Delivery  
**Product/app thật:** GrabFood  
**User cụ thể:** User không biết nên ăn gì, cần đặt đồ ăn trưa nhưng gợi ý đồ ăn app không đủ variety, dẫn đến cân bằng dinh dưỡng bị kém, thiếu chất, ăn nhiều đồ dầu mỡ.

**Nhóm có phải user thật không? Nếu không, khác ở đâu?** Có, cá nhân và thành viên gia đình nhóm gập nhiều trường hợp mất nhiều thời gian trong việc lựa chọn đồ ăn và điều chỉnh chế độ ăn uống.


## 1. Evidence summary

| Evidence | Nguồn | User/pain nói lên điều gì? | SPEC phải đổi gì? |
|---|---|---|---|
| Phàn nàn không tìm được món ăn đúng ý hoặc ngoài ngân sách (giả định) ([xem hình](./images/Image3.jpg)) | Phản hồi của user trên social media / App Store | Công cụ tìm kiếm hiện tại chỉ dựa vào từ khóa tĩnh, bỏ qua nhu cầu lọc theo ngân sách và hàm lượng dinh dưỡng. | Agent đưa ra gợi ý ăn gì phù hợp nhu cầu từng user, user có thể đưa ra mong muốn cho Agent đáp ứng (ăn gà -> Agent gợi ý ăn kèm gì đảm bào cân bằng dinh dưỡng) |
| Menu quán ăn chỉ bán món đơn lẻ, không có combo cân đối dinh dưỡng sẵn có ([xem hình](./images/Image2.jpg)) | Menu thực tế các quán cơm văn phòng trên GrabFood | Người dùng mất thời gian tự lựa chọn, chắp vá các món để đủ dinh dưỡng. | AI tự động gợi ý ghép món (ví dụ: món chính + món canh/rau phụ) thành combo cân bằng dinh dưỡng. |

## 2. Slice to Build
User không biết nên ăn gì -> User yêu cầu agent đưa ra gợi ý món ăn -> Agent đưa ra gợi ý vài loại món ăn phù hợp -> Người dùng chọn 1 món đã gợi ý -> Agent đi chuyển người dùng đến trang của quán đã chọn và tự thêm món vào giỏ hàng -> User xem lại giỏ hàng và đặt hàng.

## 3. AI Product canvas 

| Ô | Câu hỏi cần trả lời |
|---|---------------------|
| **Value** — Giá trị |Sản phảm dành cho User không biết ăn gì, họ đau vì mất thời gian để đặt đồ ăn, không biết ăn gì, đặt món ăn không cân bằng nhu cầu dinh dưỡng. AI agent có thể gợi ý món ăn dựa trên nhu cầu và khẩu vị của user, hiện tại search engine tập trung đẫy những quán ăn ngon, nhưng không nhất thiết tốt cho sức khỏe|
| **Trust** — Niềm tin |Khi AI trả lời sai (Đưa sai món ăn mà user cần ăn, quán quá xa, đồ ăn không phù hợp với sở thích...) thì người dùng có thể sửa lại, yêu cầu AI gợi ý món ăn khác. Agent có thể bỏ món vào blacklist tạm thời, không gợi ý lại món đó nữa, nhưng User có thể tương tác với blacklist trường họp đổi ý. |
| **Feasibility** —  | Chi phí 1 lượt gọi khoảng 0.002$, độ trễ khoảng 500ms - 1s, rủi ro lớn nhất là AI trả lời sai món ăn, hoặc đưa ra những gợi ý không phù hợp với nhu cầu user, ngưỡng mà nhóm sẵn sàng dừng lại là khi user không có tương tác trong 1 phút, nhóm sẽ dừng lại. |
| **Tín hiệu học** | Khi User chỉnh sửa hoạc chốt kết quả, dữ liệu sẽ được lưu lại với mục đích personalize cho từng user khác nhau (Gợi ý món ăn phù hợp khẩu vị, nhu cầu)

## 4. Tăng năng lực hay tự động hóa

AI gợi ý món ăn User có thể tự do điều chỉnh, chọn món ăn hoạc yêu cầu gợi ý khác. AI tự động hóa việc chốt món ăn (di chuyển đến trang quán, thêm món vào giỏ) và chỉ dừng lại khi user thanh toán hoặc yêu cầu chỉnh lại/ngừng.
Khi câu trả lời bị sai, hậu quả kém nghiêm trọng vì chưa chốt món ăn, user sẽ yêu cầu gợi ý lại.

## 5. Bốn đường đi của trải nghiệm

| Đường đi | Câu hỏi | Ví dụ cách xử lý |
|----------|---------|------------------|
| **Đường thuận** | AI đúng và tự tin — người dùng thấy gì? | Gợi ý món ăn hiện rõ, user đồng ý và tiếp tục quá trình đặt món |
| **Khi AI không chắc** | AI lưỡng lự — có hỏi lại không? | Đưa ra vài lựa chọn hoặc xin thêm thông tin (ví dụ: user thích ăn gà, AI chưa chắc chắn về độ cay -> AI hỏi lại user có thích ăn cay không) |
| **Khi AI sai** | Kết quả sai — người dùng gỡ ra thế nào? | Người dùng có thể blacklist gợi ý, Yêu cầu gợi ý khác. (ví dụ: AI gợi ý món ăn không phù hợp với sở thích của user -> User yêu cầu AI gợi ý món ăn khác) |
| **Khi người dùng sửa** | Người dùng chỉnh lại — dữ liệu đi về đâu? | Lưu lại để cập nhật quy tắc sở thích user, đưa gợi ý mới theo dữ liệu thu được|  

## 6. Những kiểu lỗi đáng lo nhất

- User yêu cầu ăn gà, AI gợi ý món ức gà sốt chua ngọt nhưng user không thích ăn ngọt, người dùng có thể blacklist gợi ý, Yêu cầu gợi ý khác. Prototype sẽ xử lý bằng cách: Lưu lại phản hồi của user để cập nhật quy tắc sở thích user, đưa gợi ý mới theo dữ liệu thu được.

 - Người dùng yêu cầu món ăn không có trong thực đơn của quán, user sẽ yêu cầu gợi ý món ăn khác. Prototype sẽ xử lý bằng cách : Dừng lại request đến LLM, đưa ra lựa chọn thay thế gần nhất với nhu cầu của user.

 
 ## 7. Kế hoạch kiểm thử và bằng chứng demo


#### A. Đầu vào bình thường cho đường thuận

![Demo1](./images/demo1.png)

#### B. Đầu vào gây nhiễu 

![Demo2](./images/demo2.png)

## 8. Phân công

Cuối cùng, ghi rõ ai phụ trách phần nào — người viết và kiểm thử prompt, người dựng giao diện, người giữ repo, người viết kịch bản demo, và người lo phần bằng chứng. Mỗi thành viên cần có một phần đủ rõ để tự mình giải thích được khi demo.

- Nguyễn Đoàn Gia Tuấn: Viết Spec
- Nguyễn Minh Đức: Build agent 
- Phạm Văn Sơn:  Dựng giao diện

- Tuấn + Đức + Sơn: Viết prompt, test + demo, build data.