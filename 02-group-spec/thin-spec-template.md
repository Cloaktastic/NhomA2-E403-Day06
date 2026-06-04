# Template — Thin SPEC Cuối Day 05

Thin SPEC không phải PRD đầy đủ. Đây là bản cam kết đủ rõ để sáng Day 06 nhóm build ngay.

## 1. Track, product/app và user

**Track:** Food Delivery  
**Product/app thật:** GrabFood  
**User cụ thể:** Nhân viên văn phòng bận rộn muốn duy trì cân nặng hoặc tập luyện (gym/fitness), cần đặt đồ ăn trưa ngoài nhưng vẫn kiểm soát được lượng calo và chất dinh dưỡng nạp vào (Calories, Protein, Carb, Fat).  
**Nhóm có phải user thật không? Nếu không, khác ở đâu?** Có, các thành viên trong nhóm đều thường đặt cơm trưa qua GrabFood và có nhu cầu ăn uống lành mạnh, cân đối dinh dưỡng.

## 2. Evidence summary

| Evidence | Nguồn | User/pain nói lên điều gì? | SPEC phải đổi gì? |
|---|---|---|---|
| Phàn nàn không tìm được món ăn đúng ý hoặc ngoài ngân sách ([xem hình](./images/Image3.jpg)) | Phản hồi của user trên social media / App Store | Công cụ tìm kiếm hiện tại chỉ dựa vào từ khóa tĩnh, bỏ qua nhu cầu lọc theo ngân sách và hàm lượng dinh dưỡng. | Thiết kế ô tìm kiếm/lọc thông minh dựa trên mục tiêu dinh dưỡng và khoảng giá. |
| Menu quán ăn chỉ bán món đơn lẻ, không có combo cân đối dinh dưỡng sẵn có ([xem hình](./images/Image2.jpg)) | Menu thực tế các quán cơm văn phòng trên GrabFood | Người dùng mất thời gian tự lựa chọn, chắp vá các món để đủ protein và rau xanh. | AI tự động gợi ý ghép món (ví dụ: món chính + món canh/rau phụ) thành combo cân bằng dinh dưỡng. |
| Thiếu hụt thông tin chỉ số dinh dưỡng (Macros) của món ăn ngoài | Khảo sát nhanh người dùng tập gym | Người dùng không thể theo dõi chính xác lượng calo nạp vào hàng ngày để đạt mục tiêu sức khỏe. | AI tự động phân tích tên món ăn và ước lượng chỉ số dinh dưỡng đi kèm. |

## 3. Pain statement

```text
User muốn ăn uống lành mạnh đang gặp khó ở bước chọn món ăn cân bằng dinh dưỡng trên GrabFood,
vì app thiếu thông tin chỉ số calo/dinh dưỡng và luồng gợi ý mặc định chỉ ưu tiên các combo nhiều dầu mỡ/đồ ngọt quảng cáo,
dẫn tới hậu quả user mất nhiều thời gian tra cứu thủ công hoặc chọn nhầm món ăn phá vỡ chế độ ăn kiêng.
Bằng chứng chính là các phản hồi phàn nàn về việc khó tìm kiếm món ăn lành mạnh (Image3.jpg) và menu quán ăn thiếu combo cân đối chất (Image2.jpg).
```

## 4. Build slice

```text
Cho nhân viên văn phòng đang đặt bữa trưa lành mạnh trên GrabFood,
prototype sẽ dùng AI để phân tích thực đơn và gợi ý một combo bữa ăn cân bằng dinh dưỡng (1 món chính ít béo + 1 món phụ xơ kèm chỉ số calo/protein ước lượng),
tạo ra một thực đơn đề xuất cá nhân hóa kèm nhãn phân tích calo/dinh dưỡng,
và xử lý failure mode (AI ước tính calo sai lệch) bằng cách hiển thị dải calo ước tính kèm nhãn cảnh báo "Chỉ số mang tính chất tham khảo".
```

## 5. Auto/Aug decision

Chọn một:

- [x] **Augmentation:** AI gợi ý/draft/phân loại, user quyết cuối.
- [ ] **Conditional automation:** AI tự làm trong case hẹp; case mơ hồ/rủi ro chuyển người.
- [ ] **Automation:** AI tự quyết và tự hành động.

**Lý do chọn:** AI đóng vai trò làm huấn luyện viên gợi ý combo bữa ăn và ước lượng dinh dưỡng giúp người dùng đưa ra quyết định nhanh hơn. Quyết định mua hàng và thanh toán cuối cùng vẫn do người dùng thực hiện.  
**Human role:** reviewer (người dùng xem xét và phê duyệt combo do AI gợi ý trước khi bấm đặt hàng).

## 6. Four paths

| Path | Prototype phải thể hiện gì? |
|---|---|
| **Happy** | User nhập: "Trưa nay cần 600 Calo, nhiều đạm". AI lập tức lọc menu quán ăn và gợi ý combo: *Cơm gà luộc xé + Canh rau cải thịt bằm* với tổng calo 580 kcal (đạt mục tiêu). User bấm một nút để thêm cả combo vào giỏ hàng. |
| **Low-confidence** | User chọn món có tên mơ hồ (ví dụ: "Cơm thập cẩm đặc biệt"). AI không chắc chắn về lượng calo vì nguyên liệu không rõ ràng. AI sẽ hiển thị dải calo rộng (ví dụ: 600 - 900 Calo) và đưa ra ghi chú khuyên người dùng nên chọn các món có mô tả nguyên liệu rõ ràng hơn. |
| **Failure** | AI hiểu sai mô tả món ăn (ví dụ: nhầm nước sốt mayonnaise béo ngậy là sốt healthy ít béo) và đề xuất món này cho người đang ăn kiêng nghiêm ngặt. User phát hiện ra khi đọc nhãn cảnh báo nguyên liệu của món. |
| **Correction** | User bấm vào combo gợi ý và chọn tùy chỉnh: "Bỏ bớt cơm trắng, thêm rau luộc". AI lập tức cập nhật lại biểu đồ ước tính calo và macros của bữa ăn ngay trên giao diện giỏ hàng. |

## 7. Failure mode nguy hiểm nhất

```text
Nếu user chọn chế độ ăn kiêng nghiêm ngặt (ví dụ: Keto hoặc Low-Carb),
AI có thể phân tích sai thành phần ẩn trong nước sốt (như bột năng hoặc đường tinh luyện),
hậu quả là user nạp thừa tinh bột/đường, phá vỡ quá trình ăn kiêng.
Prototype sẽ xử lý bằng cách hiển thị cảnh báo rõ ràng ("Nước sốt đi kèm món này có thể chứa đường/bột - bạn nên yêu cầu quán để riêng sốt") và hiển thị dải calo ước tính tối đa.
Owner kiểm thử path này là Nguyễn Minh Đức.
```

## 8. Owner plan cho sáng Day 06

| Thành viên | Việc phụ trách | Bằng chứng cần có trong repo |
|---|---|---|
| Nguyễn Đoàn Gia Tuấn | Research / evidence | Tổng hợp tài liệu khảo sát người dùng và ảnh chụp màn hình điểm gãy. |
| Nguyễn Minh Đức | SPEC | Hoàn thiện tài liệu Thin SPEC và các kịch bản test 4 paths. |
| Phạm Văn Sơn | Prototype | Mã nguồn frontend/backend của chatbot gợi ý món ăn dinh dưỡng. |
| Nguyễn Minh Đức | Test / failure path | Kịch bản kiểm thử tự động/thủ công cho Failure Path và Correction Path. |
| Nguyễn Đoàn Gia Tuấn | Demo script / repo | Kịch bản trình bày demo 3 phút và README hướng dẫn chạy prototype. |

