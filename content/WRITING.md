# Quy tắc viết bài Góc nhìn — Clairmont Group

## FORMAT BẮT BUỘC (từ 29/10/2026) — theo phong cách series TikTok Clairmont
Nhà sáng lập yêu cầu: bài KHÔNG được toàn chữ. Mỗi bài = một câu chuyện khu phố + MỘT học thuyết vẽ thành sơ đồ + áp dụng cho doanh nghiệp.
- Bài mẫu chuẩn: `content/posts/concept-du-an-bat-dong-san.md` — chép đúng cấu trúc, nhịp, độ dài.
- Cú pháp khối hình ảnh: docstring đầu tệp `tools/blocks.py` (hook, takeaways, story, model, compare, example, steps, principle, exercise, quote).
- Thứ tự: hook → takeaways (3 ý) → story (120–200 từ, nhân vật khu phố) → câu bắc cầu → `##` + model (sơ đồ học thuyết, tác giả/năm chính xác) + giải thích ngắn → `##` compare và/hoặc example → `## Áp dụng cho doanh nghiệp` + steps (3–5) → principle → exercise → quote → câu dẫn trang dịch vụ → `## Câu hỏi thường gặp` (3 câu).
- 750–1.100 từ; đoạn văn ≤ 3 câu; không đoạn chữ liền nào dài quá 120 từ ngoài khối.
- Không lặp học thuyết đã dùng ở bài khác (xem dòng `:::model` trong content/posts/*.md); ưu tiên học thuyết marketing & quản trị kinh điển (Maslow, AIDA, STP, 4P, Porter, Ansoff, BCG, SWOT/TOWS, Blue Ocean, 7S, PDCA, Balanced Scorecard, Business Model Canvas, Golden Circle, Kapferer, Keller CBBE, Moments of Truth, PLC, Kraljic, Greiner, Eisenhower, VRIO, Kotter 8 bước, Jobs-to-be-done, Hedgehog…).
- Nhân vật khu phố (mã cho `:::story`): co-hoa (Cô Hoa, quán cà phê đầu phố) · ong-thuong (Ông Thương, Tiệm Bánh Thương biển đỏ logo trái tim) · ong-tu (Ông Tư, sạp dưa hấu, 20 năm giữ lời "không đỏ không lấy tiền") · di-linh (Dì Linh, quán cơm gà kiểu Đà Lạt) · ong-9-co (Ông 9 Cò, siêu thị đầu ngõ) · cau-hieu (Cậu Hiếu, Khách sạn Hiếu Thảo) · cau-trong (Cậu Trống, xưởng đồ thủ công) · chi-thao (Chị Thảo, văn phòng tư vấn Clairmont — chỉ đặt câu hỏi, không kể thành tích) · chu-dau-tu (Anh Minh, chủ đầu tư giả định). Không nói nhân vật nào là FLEUR/KỂ.
- Câu cổ nhân (`:::quote`, 4 dòng: chữ Hán · Hán Việt · nghĩa · nguồn): CHỈ dùng câu trong danh sách đã kiểm chứng dưới đây, ưu tiên câu chưa dùng:
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
  (đã dùng trong 33 bài 29/10: xem các khối `:::quote` hiện có — không dùng lại)

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

## Giọng văn
Tiếng Việt tự nhiên, chuyên nghiệp, rõ ràng, có chiều sâu; không "văn AI", không sáo rỗng (đột phá, hàng đầu, số 1, toàn diện), không emoji, không hạ thấp doanh nghiệp khác. Thuật ngữ tiếng Anh chỉ khi là thuật ngữ chuyên môn. Bài "Góc nhìn Nhà sáng lập" viết ở ngôi "Clairmont" hoặc "chúng tôi", không đặt lời trích dẫn vào miệng Nhà sáng lập.

## Bản cắt mạng xã hội (lưu `social/<date>-<slug>.md`, không đăng lên web)
1. LinkedIn: 150–250 chữ, một luận điểm, giọng chuyên gia, link bài.
2. Facebook: 150–250 chữ + gợi ý 4–6 slide carousel (tiêu đề từng slide), link bài.
3. Google Business Profile: 80–150 chữ, nút "Tìm hiểu thêm" → link bài.
4. TikTok/Reels: kịch bản 45–60 giây — câu mở 3 giây, 4–6 khung một ý, chữ to, kết bằng clairmontgroup.vn và hotline 0947 120 258.

## Đăng
`python3 tools/build.py` → kiểm tra không lỗi → commit → push lên `main` (Vercel tự đăng).
