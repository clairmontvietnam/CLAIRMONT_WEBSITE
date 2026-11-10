# Quy tắc viết bài Góc nhìn — Clairmont Group

## FORMAT BẮT BUỘC (Nhà sáng lập chốt 10/11/2026 — thay cả quy tắc 29/10 lẫn "Editorial Bible V2.0")
Bài KHÔNG được toàn chữ: giữ các khối hình ảnh, nhân vật khu phố và MỘT học thuyết vẽ thành sơ đồ, nhưng nội dung viết theo lối **phân tích tư vấn chiến lược**, không theo lối bút ký.
- Bài mẫu chuẩn (cấu trúc, giọng, độ sâu): `content/posts/thuong-hieu-du-an-bat-dong-san.md` (bản biên tập 10/11/2026). Đọc kỹ trước khi viết.
- Cú pháp khối hình ảnh: docstring đầu tệp `tools/blocks.py` (hook, takeaways, story, model, compare, example, steps, principle, exercise, quote).
- Thứ tự: hook (1–2 câu) → 2–3 đoạn mở bài nêu vấn đề quản trị → takeaways (3 ý, mỗi ý một câu đầy đủ) → story (tình huống kinh doanh 150–250 từ) → câu bắc cầu → `##` + model (tác giả/năm chính xác) + phân tích ứng dụng, có nêu giới hạn của mô hình → `##` compare và/hoặc example (ví dụ giả định, kết bằng điều kiện kiểm chứng) → `## Áp dụng cho …` + steps (4 bước, mỗi bước 2 câu: làm gì + lưu ý) → principle (+ 1 đoạn diễn giải) → exercise (có thể hai chiều) → quote (+ 1–2 câu liên hệ) → câu dẫn trang dịch vụ → `## Câu hỏi thường gặp` (3–4 câu).
- 1.500–2.000 chữ; đoạn văn ≤ 3 câu.
- Không lặp học thuyết đã dùng ở bài khác (xem dòng `:::model` trong content/posts/*.md); ưu tiên học thuyết marketing & quản trị kinh điển (Maslow, AIDA, STP, 4P, Porter, Ansoff, BCG, SWOT/TOWS, Blue Ocean, 7S, PDCA, Balanced Scorecard, Business Model Canvas, Golden Circle, Kapferer, Keller CBBE, Moments of Truth, PLC, Kraljic, Greiner, Eisenhower, VRIO, Kotter 8 bước, Jobs-to-be-done, Hedgehog…).
- Nhân vật khu phố (mã cho `:::story`): co-hoa (Cô Hoa, quán cà phê đầu phố) · ong-thuong (Ông Thương, Tiệm Bánh Thương biển đỏ logo trái tim) · ong-tu (Ông Tư, sạp dưa hấu, 20 năm giữ lời "không đỏ không lấy tiền") · di-linh (Dì Linh, quán cơm gà kiểu Đà Lạt) · ong-9-co (Ông 9 Cò, siêu thị đầu ngõ) · cau-hieu (Cậu Hiếu, Khách sạn Hiếu Thảo) · cau-trong (Cậu Trống, xưởng đồ thủ công) · chi-thao (Chị Thảo, văn phòng tư vấn Clairmont — chỉ đặt câu hỏi, không kể thành tích) · chu-dau-tu (Anh Minh, chủ đầu tư giả định). Không nói nhân vật nào là FLEUR/KỂ.
- Câu cổ nhân (`:::quote`, 4 dòng: chữ Hán · Hán Việt · nghĩa · nguồn): CHỈ dùng câu trong danh sách đã kiểm chứng dưới đây hoặc câu đã xuất hiện trong khối `:::quote` của các bài hiện có. Được dùng lại, nhưng không trùng với 7 bài đăng gần nhất; chọn câu thật sự liên quan đến luận điểm. Sau khối quote có 1–2 câu liên hệ với quản trị.
  - 上兵伐謀 · Thượng binh phạt mưu · Dùng binh giỏi nhất là thắng bằng mưu lược · Tôn Tử binh pháp · Mưu công
  - 己所不欲，勿施於人 · Kỷ sở bất dục, vật thi ư nhân · Điều mình không muốn, đừng làm cho người · Luận Ngữ · Vệ Linh Công
  - 學而不思則罔 · Học nhi bất tư tắc võng · Học mà không suy nghĩ thì mờ mịt · Luận Ngữ · Vi chính
  - 見小利則大事不成 · Kiến tiểu lợi tắc đại sự bất thành · Ham lợi nhỏ thì việc lớn không thành · Luận Ngữ · Tử Lộ
  - 苟日新，日日新，又日新 · Cẩu nhật tân, nhật nhật tân, hựu nhật tân · Nếu một ngày đổi mới, thì ngày ngày đổi mới, lại ngày càng mới · Đại Học
  - 道生一，一生二，二生三，三生萬物 · Đạo sinh nhất, nhất sinh nhị, nhị sinh tam, tam sinh vạn vật · Từ một mà sinh ra muôn vật · Đạo Đức Kinh · chương 42
  - 知者不惑，仁者不憂，勇者不懼 · Trí giả bất hoặc, nhân giả bất ưu, dũng giả bất cụ · Người trí không ngờ vực, người nhân không lo, người dũng không sợ · Luận Ngữ · Tử Hãn
  - 其身正，不令而行 · Kỳ thân chính, bất lệnh nhi hành · Bản thân ngay thẳng thì không ra lệnh người cũng làm theo · Luận Ngữ · Tử Lộ
  - 水滴石穿 · Thuỷ tích thạch xuyên · Nước nhỏ giọt lâu ngày làm mòn đá · Thành ngữ
  - 授人以魚，不如授人以漁 · Thụ nhân dĩ ngư, bất như thụ nhân dĩ ngư · Cho người con cá không bằng dạy người cách câu · Thành ngữ
  (danh sách mở rộng: xem `grep -h -A1 "^:::quote" content/posts/*.md`)

## Định dạng tệp: `content/posts/<slug>.md`
```
---
slug: <slug-khong-dau-gach-noi>
title: <≤ 60 ký tự, có từ khóa chính, kết thúc " | Clairmont Group" nếu vừa>
h1: <tiêu đề hiển thị>
description: <130–155 ký tự, có từ khóa chính, lý do để bấm vào>
keywords: <từ khóa chính>, <phụ>, <phụ>
summary: <1 câu ≤ 120 ký tự cho thẻ danh sách>
date: <YYYY-MM-DD — đúng ngày đăng theo giờ Việt Nam>
category: <Chiến lược doanh nghiệp | Bất động sản | Quản trị tổ chức | Thương hiệu | Chuỗi giá trị | Góc nhìn Nhà sáng lập | Hỏi đáp>
author: Clairmont Group
---
```
Thân bài theo FORMAT BẮT BUỘC ở trên. Không có H1 trong thân bài. `## Câu hỏi thường gặp` + 3 mục `### câu hỏi?` + đoạn trả lời (tự thành FAQ schema) luôn là phần CUỐI.

## Từ khóa & liên kết
- Một từ khóa chính mỗi bài; có trong title, slug, đoạn đầu, 1–2 tiêu đề `##`. Viết tự nhiên, không nhồi.
- Không viết bài mới trùng từ khóa chính với bài đã có (kiểm tra `keywords:` của các tệp trong `content/posts/` và các trang `content/services/`).
- Mỗi bài: ít nhất 1 liên kết tới trang dịch vụ của cụm (xem `content/calendar.md`) và 1 liên kết tới một bài cũ cùng chủ đề (`/goc-nhin/<slug>/`).

## Sự thật được dùng (KHÔNG bịa thêm khách hàng, số liệu, giải thưởng, giá, kết quả, trích dẫn)
- Công ty TNHH Clairmont Group, MST 0111450942, thành lập 17/04/2021, Hà Nội. Slogan "Bản sắc dẫn lối chiến lược" / "Identity Inspires Strategy".
- Ba lĩnh vực: 01 Tư vấn và đồng hành chiến lược (gồm bất động sản, phát triển dự án) · 02 Đầu tư và phát triển thương hiệu (FLEUR — cà phê & quà tặng cao cấp mang bản sắc Việt; KỂ — quà tặng văn hoá Việt từ thiết kế và nghề thủ công; MỜI — omakase cà phê và rượu cho lãnh đạo doanh nghiệp; KỂ, MỜI ra mắt theo kế hoạch 2027) · 03 Phát triển đối tác và chuỗi giá trị (đối tác là doanh nghiệp độc lập; 5 cấp: Kết nối, Chuẩn hoá, Tích hợp, Mở thị trường, Bền vững).
- Phương pháp 4 bước: Nghiên cứu → Chiến lược → Triển khai → Đánh giá. Triết lý Porter: "chiến lược là chọn điều không làm" — "Không làm mọi thứ. Chỉ làm điều đúng. Làm đúng cách. Đúng lúc."
- Sáu trụ cột năng lực: Chiến lược & Quản trị; Tài chính & Đầu tư; Nhân sự & Tổ chức; Cung ứng & Đấu thầu; Thị trường & Phân phối; Đổi mới & Chuyển đổi số. ESG là tham chiếu, chưa phải chứng nhận.
- Nhà sáng lập & Giám đốc Tô Thị Thu Thảo, 10+ năm kinh nghiệm; 2019 Đại Quang Minh (Lâm viên sinh thái Thủ Thiêm, Quảng trường Đà Lạt); kinh nghiệm tư vấn của Nhà sáng lập với Tân Á Đại Thành, Vạn Phúc Group, Đất Vàng, Gia Khang, CTS Group; dự án: Thăng Long Legend, Meyhomes Capital Phú Quốc, Vạn Phúc City, Galia Hà Nội, Làng Mộc Miên — luôn ghi là "kinh nghiệm tư vấn của Nhà sáng lập". Chứng chỉ: Pháp lý (FIIVN), Marketing tổng thể, Tài chính – Kế toán (PACE), Quản trị nhân sự.
- FLEUR ra mắt tại Hà Nội ngày 29/11/2026.
- Clairmont là đơn vị tư vấn chiến lược và kinh doanh, KHÔNG phải tư vấn tài chính, pháp lý, môi giới. Không hứa kết quả, không nêu giá, không nêu thời hạn phản hồi.
- Kiến thức chung (định nghĩa, khung phân tích) được dùng nếu chính xác; ví dụ phải ghi "Ví dụ giả định", không dùng tên doanh nghiệp thật.

## Giọng văn (bắt buộc — Nhà sáng lập chốt 10/11/2026, thay giọng "bút ký" cũ)
Văn phong **báo cáo tư vấn chiến lược**: phân tích, chặt chẽ, trung tính, nói với chủ doanh nghiệp, ban lãnh đạo, chủ đầu tư. Bài mẫu chuẩn giọng: `content/posts/thuong-hieu-du-an-bat-dong-san.md`.
- Lập luận có điều kiện và giới hạn: "nếu doanh nghiệp đã thực sự chứng minh…", "đây không phải sự phân chia tuyệt đối", "không có một mô hình phù hợp cho mọi doanh nghiệp", "cần được kiểm chứng bằng nghiên cứu khách hàng". Không khẳng định tuyệt đối, không quy luật hoá một mô hình.
- Phân biệt rõ các khái niệm dễ nhầm (ví dụ: rủi ro danh tiếng và trách nhiệm pháp lý; nhận thức nội bộ và nhận thức thị trường). Thuật ngữ chuyên môn chính xác, kèm tên tiếng Anh trong ngoặc ở lần đầu khi cần.
- Câu chuyện khu phố viết như một tình huống kinh doanh: bối cảnh → quyết định phải đưa ra → các phương án và đánh đổi → câu hỏi cần trả lời. KHÔNG tả cảnh, không chi tiết giác quan (gió heo may, mùi bánh, sương sớm…), không ví von, không kết bằng câu cảm xúc.
- Câu mở (`:::hook`) là một nhận định quản trị rõ ràng, không ẩn dụ, không giọng TikTok.
- Tiêu đề `##` mô tả nội dung, rõ nghĩa; ít nhất một tiêu đề chứa từ khóa chính hoặc tên mô hình.
- Tránh: văn hoa mỹ, ẩn dụ, câu ngắn gây hiệu ứng, "bí quyết", "đột phá", "hàng đầu", "số 1", "trong bối cảnh hiện nay", "hãy cùng…", lạm dụng "không chỉ… mà còn…", câu cảm thán, emoji, câu kết sáo, giọng quảng cáo, khẩu ngữ, hạ thấp doanh nghiệp khác. Bài "Góc nhìn Nhà sáng lập" viết ở ngôi "Clairmont"/"chúng tôi", không đặt lời trích dẫn vào miệng Nhà sáng lập.

## Bản cắt mạng xã hội (lưu `social/<date>-<slug>.md`, không đăng lên web)
1. LinkedIn: 150–250 chữ, một luận điểm, giọng chuyên gia, link bài.
2. Facebook: 150–250 chữ + gợi ý 4–6 slide carousel (tiêu đề từng slide), link bài.
3. Google Business Profile: 80–150 chữ, nút "Tìm hiểu thêm" → link bài.
4. TikTok/Reels: kịch bản 45–60 giây — câu mở 3 giây, 4–6 khung một ý, chữ to, kết bằng clairmontgroup.vn và hotline 0947 120 258.

## Đăng
Bài mới viết dạng NHÁP trên nhánh `nhap-goc-nhin`, chỉ đăng lên `main` khi Nhà sáng lập duyệt. `python3 tools/build.py` phải chạy không lỗi.
