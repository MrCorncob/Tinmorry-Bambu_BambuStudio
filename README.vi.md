# Cấu hình sợi in TINMORRY cho Bambu Studio

*[English](README.md) | [中文](README.zh.md)*

Được fork từ [TINMORRY/Tinmorry-Bambu_BambuStudio](https://github.com/TINMORRY/Tinmorry-Bambu_BambuStudio).

Bộ cấu hình sợi in (filament) tùy chỉnh cho sợi in **TINMORRY**, dùng với Bambu Studio, đóng gói dưới dạng bundle `.bbsflmt` và sắp xếp theo từng dòng máy in Bambu Lab.

## ⚠️ Lưu ý — đọc trước khi tải về và sử dụng

- Các cấu hình có nhãn **Được tạo** trong bảng bên dưới **không phải là file xuất gốc từ TINMORRY**. Chúng được tạo ra bằng cách kết hợp dữ liệu cấu hình cũ (theo từng máy in) của TINMORRY với thông số máy in lấy từ một bundle khác (xem `CLAUDE.md` / `REFERENCES.md`), và **chưa được TINMORRY in thử kiểm chứng**.
- Trước khi in với bất kỳ cấu hình **Được tạo** nào, hãy đối chiếu lại nhiệt độ đầu phun (nozzle), bàn in (bed/plate) và buồng in (chamber) với thông tin thực tế trên nhãn cuộn sợi hoặc datasheet của nhà sản xuất — **đặc biệt là PA-CF và PAHT-CF trên X2D**, vì hai cấu hình này đang dùng tạm khoảng nhiệt độ của PETG CF thay vì khoảng nhiệt độ riêng của chúng (thường thấp hơn đáng kể so với mức PA-CF/PAHT-CF thực sự cần).
- Dùng đầu phun (nozzle) chống mài mòn (hardened) cho bất kỳ loại sợi có pha sợi carbon (CF) hoặc sợi thủy tinh (GF) nào (PETG-CF, PLA-CF, PET-CF, PC GF, TPU GF, PA-CF, PAHT-CF, PP-CF).
- Nên in thử một mẫu nhỏ và theo dõi các lớp in đầu tiên trước khi in một sản phẩm hoàn chỉnh, đặc biệt với các máy in không có buồng bao kín (A1, A1 mini, A2L).
- **Cấu hình PC GF của A1 là một trường hợp đặc biệt cần lưu ý**: bản thân Bambu Studio có cung cấp sẵn cấu hình hệ thống cho PC-GF trên máy A1 (loại máy khung hở, không có buồng bao kín), nên cấu hình này được đưa vào đây dựa trên bằng chứng trực tiếp đó — nhưng điều này không có nghĩa là ABS/ASA cũng an toàn trên A1, và repo này cố tình không tạo cấu hình ABS/ASA cho A1. Nếu in PC GF trên A1 (khung hở), hãy đảm bảo thông gió tốt và lường trước khả năng cong vênh nhiều hơn so với máy có buồng bao kín.
- Các cấu hình này được cung cấp "nguyên trạng" (as-is), không có bảo hành. Bạn tự chịu trách nhiệm kiểm tra xem một cấu hình có an toàn cho máy in và loại sợi của mình trước khi sử dụng hay không.

## Cấu trúc thư mục

Mỗi thư mục cấp cao nhất tương ứng với một dòng máy in (theo đúng giá trị trong trường `compatible_printers` của từng cấu hình). Riêng `X2D` có thêm thư mục con `0.4mm` cho đầu phun 0.4mm.

```
A1/       Bambu Lab A1, đầu phun 0.4mm
A1mini/   Bambu Lab A1 mini, đầu phun 0.4mm
A2L/      Bambu Lab A2L, đầu phun 0.4mm
H2C/      Bambu Lab H2C, đầu phun 0.4mm
H2D/      Bambu Lab H2D, đầu phun 0.4mm
H2S/      Bambu Lab H2S, đầu phun 0.4mm
P1S/      Bambu Lab P1S, đầu phun 0.4mm
P2S/      Bambu Lab P2S, đầu phun 0.4mm
X2D/0.4mm/  Bambu Lab X2D, đầu phun 0.4mm
```

## Danh sách cấu hình hiện có

Bấm vào tên máy in bên dưới để xem danh sách sợi in tương ứng. Mỗi dòng có link **Tải xuống** dẫn thẳng đến file `.bbsflmt` — chuột phải vào link rồi chọn "Save Link As" để tải về (không cần clone repo hay vào GitHub duyệt file).

- **Nguyên bản** = file xuất thật từ TINMORRY.
- **Được tạo** = không phải từ TINMORRY trực tiếp; được tạo ra từ dữ liệu cũ của TINMORRY bằng các script trong repo này (xem `CLAUDE.md`). Hãy đọc mục **⚠️ Lưu ý** ở trên trước khi dùng cấu hình loại "Được tạo", đặc biệt là PA-CF/PAHT-CF trên X2D.

Một số loại sợi (PETG GF, PETG Marble, PETG Metallic, TPU 95A) dùng chung một bundle duy nhất trong `X2D/0.4mm/`, chứa cấu hình cho cả máy P2S lẫn X2D.

<!-- BEGIN GENERATED PROFILE TABLES -->

<details>
<summary><strong>Bambu Lab A1 (22)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A1 mini (20)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A1mini/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A2L (20)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/A2L/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2C (25)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2C/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2D (23)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS pro | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20ABS%20pro.bbsflmt) |
| TINMORRY ASA CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte， | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PLA%20Matte%EF%BC%8C.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2D/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2S (22)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ABS Pro | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/H2S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P1S (26)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ABS Pro | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P1S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P2S (24)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS Pro | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY PP-CF ` | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20PP-CF%20%60.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/P2S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab X2D (22)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS Pro | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY ASA basic | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20ASA%20basic.bbsflmt) |
| TINMORRY PA-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PA-CF.bbsflmt) |
| TINMORRY PAHT-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PAHT-CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PETG CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG ECO | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY PLA matte | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20PLA%20matte.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/Tinmorry-Bambu_BambuStudio/all-printers/X2D/0.4mm/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<!-- END GENERATED PROFILE TABLES -->

Xem [REFERENCES.md](REFERENCES.md) để biết đầy đủ thông tin kỹ thuật (bundle id, phiên bản Studio, chuỗi compatible-printer chính xác).

## Cách cài đặt một cấu hình

1. Trong Bambu Studio, vào **File → Import → Import Configs**.
2. Chọn file `.bbsflmt` tương ứng với loại sợi/máy in bạn cần.
3. Cấu hình sợi sẽ xuất hiện trong danh sách filament của đúng máy in đó, dưới mục vendor `TINMORRY`.

## Định dạng file

Mỗi file `.bbsflmt` là một file nén zip (định dạng bundle cấu hình filament của Bambu Studio) chứa:

- `bundle_structure.json` — thông tin metadata của bundle: bundle id, phiên bản Bambu Studio khi xuất file, tên filament, và bảng ánh xạ vendor/đường dẫn cấu hình.
- `TINMORRY/<tên filament> @<máy in> 0.4 nozzle.json` — một file cấu hình filament cho mỗi máy in tương thích, gồm đầy đủ các thông số của Bambu Studio (nhiệt độ, làm mát, lưu lượng, rút sợi, v.v.).

Xem [REFERENCES.md](REFERENCES.md) để biết danh sách đầy đủ các bundle và metadata của chúng.

## Một số điểm cần lưu ý

- Một vài tên file có ký tự lạ còn sót lại từ lần xuất gốc (ví dụ dấu phẩy toàn chiều rộng trong `H2D/TINMORRY PLA Matte，.bbsflmt`, hoặc dấu backtick trong `` P2S/TINMORRY PP-CF `.bbsflmt ``). Đây chỉ là vấn đề thẩm mỹ, không ảnh hưởng đến việc import.
