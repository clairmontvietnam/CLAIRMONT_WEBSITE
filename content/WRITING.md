# Editorial Bible V2.0 — bài Góc nhìn Clairmont Group

Nhà sáng lập duyệt ngày 10/11/2026. Thay thế toàn bộ quy tắc cũ (khuôn 10 khối, truyện khu phố, câu cổ nhân, giọng bút ký). Báo cáo đầy đủ: CLM-MKT-ED-01.
Bài mẫu chuẩn (đọc kỹ trước khi viết): `content/posts/chien-luoc-doanh-nghiep-la-gi.md` (strategic insight), `content/posts/co-cau-san-pham-bat-dong-san.md` (technical deep dive), `content/posts/tai-dinh-vi-du-an-bat-dong-san-ban-cham.md` (case analysis) — bản ở nhánh `nhap-bien-tap-v2` cho đến khi được đăng.

## 1. Định vị
Góc nhìn là thư viện tri thức của một đơn vị tư vấn chiến lược, phát triển dự án và kiến trúc thương hiệu. Độc giả: chủ đầu tư, HĐQT, CEO, giám đốc phát triển dự án, giám đốc chiến lược. Mỗi bài giúp người đọc ra một quyết định tốt hơn hoặc hiểu đúng hơn vấn đề họ phải quyết định. Không viết blog truyền cảm hứng, sách đạo lý, quảng cáo hay SEO hàng loạt.
Mỗi bài trả lời (tuỳ dạng, không bắt buộc đủ): vấn đề kinh doanh là gì · vì sao quan trọng · các lựa chọn · điều kiện chọn · đánh đổi · rủi ro · cách triển khai. Mỗi đoạn phải đóng góp kiến thức, lập luận, bằng chứng hoặc công cụ ra quyết định.

## 2. Sáu dạng bài (không dùng một khuôn chung; xoay vòng để không hai bài liên tiếp cùng dạng)
| Dạng | Cấu trúc gợi ý | Độ dài |
|---|---|---|
| Strategic insight (trụ cột) | định nghĩa làm việc có nguồn → phân biệt khái niệm gần → các cấp/thành phần → phép thử/tiêu chí → giới hạn → dẫn sang bài chuyên sâu | 1.800–2.500 |
| Research analysis | câu hỏi nghiên cứu → nguồn và phương pháp → phát hiện có số liệu và nguồn → giới hạn dữ liệu → hàm ý quyết định | 1.500–2.500 |
| Decision framework | quyết định cần đưa ra → phương án → tiêu chí, điều kiện (ma trận) → đánh đổi → rủi ro → quy trình quyết định | 1.500–2.200 |
| Case analysis | bối cảnh (thật có nguồn, hoặc giả định ghi rõ) → dữ liệu → chẩn đoán từng giả thuyết → phương án và lý do → điều kiện để kết luận còn đúng | 1.500–2.500 |
| Technical deep dive | vì sao quan trọng → ràng buộc cứng (văn bản có số hiệu, hiệu lực) → biến số → công cụ → ví dụ giả định có số liệu và quy ước tính → sai lầm thường gặp | 2.000–3.000 |
| Executive perspective | lập trường nêu ngay → lý do, bằng chứng → phản biện mạnh nhất → vì sao vẫn giữ → điều kiện khiến lập trường sai | 900–1.500 |
Độ dài theo độ phức tạp, không theo chỉ tiêu.

## 3. Định dạng tệp `content/posts/<slug>.md`
```
---
slug: <không đổi slug đã xuất bản>
title: <≤ 60 ký tự, chứa từ khoá chính>
h1: <tiêu đề hiển thị, chứa từ khoá chính>
description: <130–160 ký tự>
keywords: <từ khoá chính>, <phụ>, ...
summary: <1 câu ≤ 160 ký tự>
date: <YYYY-MM-DD>
category: <Chiến lược doanh nghiệp | Bất động sản | Quản trị tổ chức | Thương hiệu | Chuỗi giá trị | Góc nhìn Nhà sáng lập | Hỏi đáp>
author: Clairmont Group
---
```
Thân bài: đoạn mở thường (không dùng `:::hook`), nêu vấn đề và luận điểm; hai câu đầu trả lời ý định tìm kiếm.
Khối được dùng: `:::takeaways` (tóm tắt cho lãnh đạo, số ý tuỳ bài) · `:::example <tiêu đề ghi rõ giả định>` · `:::model` (chỉ khi mô hình trả lời câu hỏi của bài, nguồn đúng) · `:::steps` (quy trình có thứ tự thật) · bảng markdown (so sánh phương án, ma trận quyết định).
KHÔNG dùng: `:::story`, `:::quote`, `:::principle`, `:::exercise`, `:::hook`. `:::compare` chỉ cho "cách sai / cách đúng" (hiển thị ✕/✓); so sánh phương án có đánh đổi dùng bảng.
Cuối bài: `## Nguồn tham khảo` (tác giả, năm, tác phẩm/tạp chí; văn bản pháp luật có số hiệu và hiệu lực) + một câu nêu rõ phần nào là đề xuất/giả định của Clairmont; sau đó `## Câu hỏi thường gặp` với 3–5 mục `###` từ truy vấn thật (câu trả lời 40–80 từ, tự đứng được) — luôn là phần CUỐI.

## 4. Giọng văn
Làm: chuyên gia tư vấn trình bày với HĐQT; điềm tĩnh, rõ, chính xác; thuật ngữ giải thích một lần; nói điều kiện và giới hạn ("phù hợp khi…", "không phù hợp khi…"); gọi người đọc bằng vai trò (chủ đầu tư, Ban điều hành), không gọi "bạn".
Không làm: nhân vật hư cấu, chuyện khu phố, tiệm bánh, tả cảnh mùi vị thời tiết; câu cổ nhân, danh ngôn, triết lý phương Đông; câu đối xứng công thức ("không chỉ X mà còn Y", "không phải A mà là B") khi không tạo hiểu biết mới; châm ngôn kết đoạn; câu cảm thán; emoji; từ sáo ("đột phá", "hàng đầu", "bí quyết", "trong bối cảnh hiện nay", "hành trình", "đẳng cấp"); khẳng định tuyệt đối không bằng chứng. Không dùng tên người thật (kể cả Nhà sáng lập) trong tình huống.

## 5. Chuẩn nguồn — năm loại khẳng định
1. Sự kiện đã kiểm chứng: có nguồn công khai đáng tin, ghi trong mục Nguồn.
2. Quan điểm học thuật: tác giả, năm, tác phẩm; đúng phạm vi. Ghi tác giả gốc của mô hình; nói giới hạn và cách điều chỉnh cho bối cảnh dự án/doanh nghiệp Việt Nam. Không vẽ lại mô hình theo trục mới rồi ghi nguồn tác giả gốc. Không áp máy móc framework quản trị chung vào bất động sản.
3. Nhận định chuyên gia: nguồn (CBRE, Savills, JLL, ULI, RICS, McKinsey, BCG, Bain, HBR…) và kỳ báo cáo.
4. Giả định phân tích: gắn nhãn "giả định"; ví dụ số phải ghi quy ước tính; không trình bày như dữ liệu thị trường.
5. Đề xuất của Clairmont: ghi rõ là đề xuất/khung/nhận định của Clairmont.
Pháp lý, quy hoạch, tài chính, tiêu chuẩn kỹ thuật: tra cứu văn bản hiện hành bằng web search trước khi viết; ghi số hiệu, ngày hiệu lực; kiểm tra văn bản sửa đổi, thay thế, dự thảo; luôn khuyến nghị ý kiến pháp lý cho quyết định cụ thể. Điều gì không xác minh được thì BỎ khỏi bài và báo lại.

## Sự thật được dùng (KHÔNG bịa thêm khách hàng, số liệu, giải thưởng, giá, kết quả, trích dẫn)
- Công ty TNHH Clairmont Group, MST 0111450942, thành lập 17/04/2021, Hà Nội. Slogan "Bản sắc dẫn lối chiến lược" / "Identity Inspires Strategy".
- Ba lĩnh vực: 01 Tư vấn và đồng hành chiến lược (gồm bất động sản, phát triển dự án) · 02 Đầu tư và phát triển thương hiệu (FLEUR — cà phê & quà tặng cao cấp mang bản sắc Việt; KỂ — quà tặng văn hoá Việt từ thiết kế và nghề thủ công; MỜI — omakase cà phê và rượu cho lãnh đạo doanh nghiệp; KỂ, MỜI ra mắt theo kế hoạch 2027) · 03 Phát triển đối tác và chuỗi giá trị (đối tác là doanh nghiệp độc lập; 5 cấp: Kết nối, Chuẩn hoá, Tích hợp, Mở thị trường, Bền vững).
- Phương pháp 4 bước: Nghiên cứu → Chiến lược → Triển khai → Đánh giá. Triết lý Porter: "chiến lược là chọn điều không làm" — "Không làm mọi thứ. Chỉ làm điều đúng. Làm đúng cách. Đúng lúc."
- Sáu trụ cột năng lực: Chiến lược & Quản trị; Tài chính & Đầu tư; Nhân sự & Tổ chức; Cung ứng & Đấu thầu; Thị trường & Phân phối; Đổi mới & Chuyển đổi số. ESG là tham chiếu, chưa phải chứng nhận.
- Nhà sáng lập & Giám đốc Tô Thị Thu Thảo, 10+ năm kinh nghiệm; 2019 Đại Quang Minh (Lâm viên sinh thái Thủ Thiêm, Quảng trường Đà Lạt); kinh nghiệm tư vấn của Nhà sáng lập với Tân Á Đại Thành, Vạn Phúc Group, Đất Vàng, Gia Khang, CTS Group; dự án: Thăng Long Legend, Meyhomes Capital Phú Quốc, Vạn Phúc City, Galia Hà Nội, Làng Mộc Miên — luôn ghi là "kinh nghiệm tư vấn của Nhà sáng lập"; chỉ nêu tên dự án khi thật cần cho luận điểm, không mô tả vai trò hay kết quả cụ thể chưa được Nhà sáng lập xác nhận. Chứng chỉ: Pháp lý (FIIVN), Marketing tổng thể, Tài chính – Kế toán (PACE), Quản trị nhân sự.
- FLEUR ra mắt tại Hà Nội ngày 29/11/2026.
- Clairmont là đơn vị tư vấn chiến lược và kinh doanh, KHÔNG phải tư vấn tài chính, pháp lý, môi giới. Không hứa kết quả, không nêu giá, không nêu thời hạn phản hồi.

## 7. SEO và liên kết
- Một từ khoá chính mỗi URL; không trùng `keywords` đầu tiên của bài khác hay trang `content/services/`. Trước khi viết, xác định: người tìm là ai, cần quyết định gì, 10 giây đầu cần đọc gì.
- Từ khoá chính có trong title, h1, đoạn đầu và ít nhất một `##`.
- 2–5 liên kết nội bộ theo cụm (bài hỗ trợ → chuyên sâu → trụ cột → trang dịch vụ); mọi URL phải tồn tại; anchor mô tả trang đích.
- CTA 1–2 câu gắn với vấn đề bài, trỏ đúng dịch vụ, nêu đầu ra của công việc; không hứa kết quả, không nêu giá, không nêu thời hạn phản hồi.

## 8. QA trước khi gửi duyệt
Luận điểm trung tâm viết được thành một câu và khác các bài cùng cụm · hai câu đầu trả lời ý định tìm kiếm · không có thành phần ở mục "Không làm" · mọi mô hình có tác giả, năm, giới hạn · mọi số liệu có nguồn hoặc nằm trong ví dụ có nhãn giả định · văn bản pháp luật có số hiệu và hiệu lực đã kiểm tra · có mục Nguồn tham khảo · title ≤ 60, description 130–160 · liên kết nội bộ tồn tại · `python3 tools/build.py` không lỗi.

## 9. Bản cắt mạng xã hội (lưu `social/<date>-<slug>.md`, không đăng lên web)
1. LinkedIn: 150–250 chữ, một luận điểm, giọng chuyên gia, link bài.
2. Facebook: 150–250 chữ + gợi ý 4–6 slide carousel (tiêu đề từng slide), link bài.
3. Google Business Profile: 80–150 chữ, nút "Tìm hiểu thêm" → link bài.
4. TikTok/Reels: kịch bản 45–60 giây, một luận điểm, 4–6 khung một ý, kết bằng clairmontgroup.vn.

## 10. Quy trình đăng (từ 10/11/2026: viết nháp, Nhà sáng lập duyệt mới đăng)
Bài mới viết vào nhánh `nhap-goc-nhin` (KHÔNG push lên `main`). Chỉ commit tệp bài `.md`, bản cắt mạng xã hội và `content/calendar.md`; không commit tệp HTML do build sinh ra. Sau khi Nhà sáng lập duyệt, bài được chuyển sang `main`, build và đăng.
