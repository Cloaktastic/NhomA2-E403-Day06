# Toolkit — Từ Evidence Đến Build Slice

Dùng sau khi nhóm đã có evidence. Mục tiêu là chốt một build slice đủ nhỏ cho Day 06.

## 1. Gom evidence thành cụm

Gom theo **workflow/pain**, không gom theo tên feature.

Ví dụ cụm tốt:

- "Không biết chọn chuyên khoa"
- "Không hiểu vì sao bị tính phí"
- "Muốn sửa output nhưng không có chỗ sửa"
- "Bot trả lời tự tin nhưng không dẫn nguồn"

## 2. Viết insight

Form:

```text
User [segment] không chỉ cần [surface need].
Họ thật ra cần [deeper need],
vì [evidence pattern].
```

Ví dụ:

```text
Người lần đầu đi khám không chỉ cần danh sách chuyên khoa.
Họ cần hỗ trợ ra quyết định an toàn,
vì nhiều review/observation cho thấy họ không biết triệu chứng của mình nên đi khoa nào.
```

## 3. Viết opportunity

Form:

```text
Cơ hội là dùng AI để [augment/automate hành động hẹp],
giúp user [kết quả],
trong khi vẫn kiểm soát [failure/risk].
```

## 4. Chọn build slice

Build slice tốt phải qua 5 câu hỏi:

| Câu hỏi | Đạt khi |
|---|---|
| User cụ thể chưa? | Nói được ai dùng, trong bối cảnh nào. |
| Task đủ hẹp chưa? | Demo được trong 3-5 phút. |
| AI decision rõ chưa? | AI gợi ý/tự làm một việc cụ thể. |
| Failure path rõ chưa? | Có một case AI không chắc hoặc sai để test. |
| Có evidence không? | Có bằng chứng từ self-use/review/user/competitor. |

## 5. Quyết định: giữ, giảm scope, hay đổi hướng?

| Tình huống | Quyết định |
|---|---|
| Evidence yếu, user mơ hồ | Dừng build sâu; quay lại research 20 phút. |
| Ý tưởng quá rộng | Giữ domain, cắt xuống một flow. |
| AI không cần thiết | Dùng rule/manual prototype; ghi rõ vì sao không dùng AI sâu. |
| Rủi ro cao | Chọn augmentation hoặc conditional automation. |
| Không demo được trong 1 ngày | Đưa phần lớn vào backlog, giữ một path nhỏ. |

## 6. Câu chốt cuối

Điền câu này trước khi rời lớp:

```text
Dựa trên phản hồi về việc khó tìm món ăn cân đối và thiếu thông tin dinh dưỡng (Image2.jpg, Image3.jpg),
nhóm sẽ build mẫu thử Trợ lý AI gợi ý thực đơn (AI Balanced Diet Agent),
cho nhân viên văn phòng bận rộn đặt cơm trưa trên GrabFood,
để giải quyết khó khăn trong việc tính toán calo và duy trì chế độ dinh dưỡng khi ăn ngoài tiệm,
bằng cách AI tự động ước lượng calo/macros và gợi ý combo kết hợp món ăn phụ (rau, súp) phù hợp mục tiêu sức khỏe,
và sẽ test failure path khi AI nhận diện sai thành phần ẩn nhiều đường/calo trong nước sốt.
```

## 7. Backlog

Những thứ **không build trong Day 06**:

- Tính năng kết nối tài khoản thanh toán và đặt hàng thực tế qua API của Grab.
- Đồng bộ hóa lịch sử dinh dưỡng hàng ngày/hàng tuần với các ứng dụng sức khỏe (Apple Health, Google Fit).
- Gợi ý món ăn thông minh theo định vị GPS thời gian thực.
- Cơ sở dữ liệu dinh dưỡng chi tiết được kiểm chứng lâm sàng cho toàn bộ các quán ăn (chỉ demo dữ liệu do AI phân tích trên menu của một nhóm quán tiêu biểu).
