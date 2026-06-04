# Template — Evidence Pack

Nộp kèm thin SPEC cuối Day 05.

## 1. Nhóm và track

**Tên nhóm: Nhóm trái ngoài cùng**  
**Track:** Food Delivery  
**Product/app đã chọn: GrabFood**  
**Build slice đang nghĩ:** AI Balanced Diet Agent - Trợ lý AI gợi ý thực đơn cân bằng dinh dưỡng (ước lượng Calories, Carb, Protein, Fat)

## 2. Self-use evidence

Nhóm tự dùng app/workflow và ghi lại điểm gãy.

| Observation | Screenshot/link | Path liên quan | Điều học được |
|---|---|---|---|
| Nhiều comments về app phàn nàn về việc không tim được món ăn, do app không gợi ý đúng hay cho gợi ý sai ý muốn, ngoài budget | [xem hình](./images/Image3.jpg) | Failure | Thuật toán tìm kiếm thông thường không đủ để đáp ứng nhu cầu của User |
| Người dùng muốn kết hợp một bữa ăn đầy đủ chất (ví dụ: cần thêm xơ từ rau và protein từ thịt) nhưng menu quán chỉ hiển thị món đơn lẻ. App không gợi ý combo cân đối (ví dụ: Cơm ức gà + Canh rau cải) để đạt mục tiêu dinh dưỡng. | [xem hình](./images/Image2.jpg) | Low-confidence | Các combo có sẵn chủ yếu do quán tự tạo để tăng doanh thu (ví dụ: cơm + nước ngọt), không hướng đến tiêu chí cân bằng sức khỏe. |

## 3. User / review / social evidence

Nguồn có thể là review App Store/Play, group, comment, phỏng vấn nhanh, hoặc nguồn public khác.

| Quote / review / observation | Nguồn | User là ai? | Pain/failure mode |
|---|---|---|---|
| "Mình tập gym và cần ăn đủ 120g protein/ngày. Gọi đồ ăn ngoài tiệm cực kỳ đau đầu vì không biết lượng protein thực tế là bao nhiêu, đành toàn phải tự nấu hoặc nhắm mắt chọn đại ức gà." | Group "Cộng đồng Gym & Fitness Việt Nam" | Người tập thể hình, có mục tiêu tăng cơ/giảm mỡ | **Failure path:** Thiếu hụt trầm trọng thông tin chỉ số dinh dưỡng (Macros) khiến việc đặt đồ ăn ngoài trở nên rủi ro cho chế độ tập luyện. |
| "Muốn ăn uống lành mạnh hơn nhưng mỗi lần mở GrabFood là bị ngập trong các banner gà rán, trà sữa giảm giá. Tìm được món mất cả buổi." | Phỏng vấn nhanh 3 nhân viên văn phòng | Nhân viên văn phòng bận rộn muốn duy trì cân nặng | **Failure path:** Luồng gợi ý mặc định của app ưu tiên đồ ăn nhanh nhiều dầu mỡ; thiếu bộ lọc thông minh cho chế độ dinh dưỡng cân bằng. |
| "App nên có tính năng tự động tính tổng lượng calo của giỏ hàng và gợi ý thêm đĩa rau hoặc bớt bát cơm nếu thấy quá nhiều tinh bột." | Comment trên bài đăng của Grab Vietnam | Người dùng phổ thông muốn ăn uống khoa học | **Correction path:** Không có cơ chế phản hồi hay gợi ý điều chỉnh giỏ hàng khi phát hiện mất cân đối dinh dưỡng. |

## 4. Competitor / analog evidence

| App / mô hình tham khảo | Họ xử lý task này thế nào? | Pattern học được | Có áp dụng trong 1 ngày không? |
|---|---|---|---|
| **MyFitnessPal / Lifesum** | Cho phép người dùng quét hoặc nhập món ăn để phân tích lượng calo và 3 chỉ số chính (Carb, Protein, Fat). | Sử dụng cơ sở dữ liệu dinh dưỡng để quy đổi tên món ăn thành chỉ số cụ thể. | Có, dùng LLM để ước lượng dinh dưỡng sơ bộ của món dựa trên tên và mô tả món. |
| **HealthyOut** | App chuyên gợi ý món ăn nhà hàng dựa trên mục tiêu ăn kiêng (Low Carb, Heart Healthy, High Protein). | Gợi ý món ăn đi kèm lý do chi tiết (ví dụ: "Món này giàu xơ và dưới 500 Calo"). | Có, thiết kế thẻ gợi ý (recommender card) hiển thị lý do dinh dưỡng và lượng calo ước tính. |

## 5. Evidence -> Insight

```text
Evidence nổi bật nhất:
Nhóm user quan tâm đến sức khỏe (gym, giảm cân, ăn uống sạch) gặp khó khăn lớn khi đặt đồ ăn ngoài vì GrabFood hoàn toàn thiếu thông tin dinh dưỡng (Calories, Protein, Fat, Carb) và các đề xuất mặc định của app đều thiên về đồ ăn nhanh nhiều dầu mỡ.

Insight:
User không chỉ cần những gợi ý món ăn ngẫu nhiên.
Họ cần sự minh bạch về dinh dưỡng (nutrition transparency) và hỗ trợ kết hợp thực đơn (meal pairing) để dễ dàng kiểm soát lượng calo và chất dinh dưỡng nạp vào cơ thể mà không cần tự tính toán thủ công.

Opportunity:
AI có thể giúp bằng cách phân tích tên và mô tả các món ăn trên menu, ước lượng chỉ số dinh dưỡng sơ bộ (Macros), và đóng vai trò như một huấn luyện viên dinh dưỡng gợi ý cách kết hợp món ăn (ví dụ: 1 món chính ít béo + 1 món canh/rau) để đạt được một bữa ăn cân bằng.
```

## 6. Evidence đổi SPEC như thế nào?

- [ ] Đổi user chính.
- [ ] Đổi pain statement.
- [x] Đổi build slice.
- [x] Đổi Auto/Aug decision.
- [x] Đổi 4 paths.
- [ ] Đổi failure mode.
- [ ] Đổi owner/test plan.

Ghi rõ 1-2 thay đổi quan trọng:

```text
Trước evidence, nhóm định: Làm một chatbot gợi ý món ăn chung chung theo tâm trạng của người dùng (vui, buồn, thèm ngọt).

Sau evidence, nhóm đổi thành: Build một Trợ lý AI gợi ý bữa ăn cân bằng dinh dưỡng (AI Balanced Diet Agent) dựa trên việc phân tích chỉ số dinh dưỡng (Macros) và đề xuất các combo món kết hợp lành mạnh.

Lý do:
Dữ liệu nghiên cứu người dùng chỉ ra rằng nhu cầu kiểm soát calo và các chất dinh dưỡng khi ăn ngoài tiệm là cực kỳ lớn và chưa được giải quyết tốt trên thị trường hiện nay. AI có thế mạnh vượt trội trong việc phân tích ngữ nghĩa để ước lượng dinh dưỡng từ mô tả món ăn thô.
```
