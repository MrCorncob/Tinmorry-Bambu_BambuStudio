# Cấu hình sợi in TINMORRY cho Bambu Studio

*[English version](README.md)*

Bộ cấu hình sợi in (filament) tùy chỉnh cho sợi in **TINMORRY**, dùng với Bambu Studio, đóng gói dưới dạng bundle `.bbsflmt` và sắp xếp theo từng dòng máy in Bambu Lab.

## ⚠️ Lưu ý — đọc trước khi tải về và sử dụng

- Các cấu hình có đánh dấu `*` trong bảng bên dưới **không phải là file xuất gốc từ TINMORRY**. Chúng được tạo ra bằng cách kết hợp dữ liệu cấu hình cũ (theo từng máy in) của TINMORRY với thông số máy in lấy từ một bundle khác (xem `CLAUDE.md` / `REFERENCES.md`), và **chưa được TINMORRY in thử kiểm chứng**.
- Trước khi in với bất kỳ cấu hình có dấu `*` nào, hãy đối chiếu lại nhiệt độ đầu phun (nozzle), bàn in (bed/plate) và buồng in (chamber) với thông tin thực tế trên nhãn cuộn sợi hoặc datasheet của nhà sản xuất — **đặc biệt là PA-CF và PAHT-CF trên X2D**, vì hai cấu hình này đang dùng tạm khoảng nhiệt độ của PETG CF thay vì khoảng nhiệt độ riêng của chúng (thường thấp hơn đáng kể so với mức PA-CF/PAHT-CF thực sự cần).
- Dùng đầu phun (nozzle) chống mài mòn (hardened) cho bất kỳ loại sợi có pha sợi carbon (CF) hoặc sợi thủy tinh (GF) nào (PETG-CF, PLA-CF, PET-CF, PC GF, TPU GF, PA-CF, PAHT-CF, PP-CF).
- Nên in thử một mẫu nhỏ và theo dõi các lớp in đầu tiên trước khi in một sản phẩm hoàn chỉnh, đặc biệt với các máy in không có buồng in gia nhiệt (A1 mini, A2L).
- Các cấu hình này được cung cấp "nguyên trạng" (as-is), không có bảo hành. Bạn tự chịu trách nhiệm kiểm tra xem một cấu hình có an toàn cho máy in và loại sợi của mình trước khi sử dụng hay không.

## Cấu trúc thư mục

Mỗi thư mục cấp cao nhất tương ứng với một dòng máy in (theo đúng giá trị trong trường `compatible_printers` của từng cấu hình). Riêng `X2D` có thêm thư mục con `0.4mm` cho đầu phun 0.4mm.

```
A1mini/   Bambu Lab A1 mini, đầu phun 0.4mm
A2L/      Bambu Lab A2L, đầu phun 0.4mm
H2C/      Bambu Lab H2C, đầu phun 0.4mm
H2D/      Bambu Lab H2D, đầu phun 0.4mm
H2S/      Bambu Lab H2S, đầu phun 0.4mm
P2S/      Bambu Lab P2S, đầu phun 0.4mm
X2D/0.4mm/  Bambu Lab X2D, đầu phun 0.4mm
```

## Danh sách cấu hình hiện có

| Máy in | Sợi in |
|---|---|
| A1 mini | PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG CF PP*, PETG ECO*, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Matte, PETG Metallic*, PETG Sparkly*, PLA*, PLA CF*, PLA Galaxy*, PLA Matte*, PLA Silk*, TPU 95A, TPU GF* |
| A2L | PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG CF PP*, PETG ECO, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Metallic, PETG Sparkly*, PLA CF*, PLA Galaxy*, PLA Matte*, PLA Rapid, PLA Silk, TPU 95A, TPU GF* |
| H2C | ABS*, ASA*, ASA CF*, PC GF*, PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG CF PP*, PETG ECO*, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Metallic*, PETG Sparkly*, PLA CF, PLA Galaxy*, PLA Matte*, PLA Rapid, PLA Silk*, TPU*, TPU 95A*, TPU GF* |
| H2D | ABS pro, ASA CF, PC GF*, PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG CF PP*, PETG ECO*, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Metallic*, PETG Sparkly*, PLA CF*, PLA Galaxy*, PLA Matte, PLA Silk*, TPU*, TPU 95A*, TPU GF* |
| H2S | ABS*, ABS Pro*, ASA CF, PC GF*, PET CF*, PET CF GF*, PETG CF, PETG ECO*, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Metallic*, PETG Sparkly*, PLA CF*, PLA Galaxy*, PLA Matte*, PLA Rapid, PLA Silk*, TPU 95A, TPU GF* |
| P2S | ABS Pro, ASA*, ASA CF*, PC GF*, PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG ECO*, PETG GF, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Matte, PETG Metallic, PETG Sparkly*, PLA*, PLA CF*, PLA Galaxy*, PLA Matte*, PLA Silk*, PP-CF, TPU 95A, TPU GF* |
| X2D | ABS Pro, ASA basic, ASA CF*, PA-CF*, PAHT-CF*, PC GF*, PET CF*, PETG CF, PETG ECO, PETG GF, PETG Galaxy, PETG HS*, PETG Marble, PETG Metallic, PETG Sparkly, PLA CF*, PLA Galaxy*, PLA Silk*, PLA matte, TPU 95A, TPU GF* |

Một số loại sợi (PETG GF, PETG Marble, PETG Metallic, TPU 95A) dùng chung một bundle duy nhất trong `X2D/0.4mm/`, chứa cấu hình cho cả máy P2S lẫn X2D.

\* Không phải file xuất gốc từ TINMORRY — được tạo ra từ dữ liệu cấu hình cũ theo từng máy in của TINMORRY thông qua `scripts/convert_old_repo_to_printer.py`, có áp dụng chính sách kiểm tra khả năng tương thích máy in (xem CLAUDE.md). PA-CF/PAHT-CF chỉ có trên X2D và cố tình không có ở các máy còn lại; ABS/ASA/PC hoàn toàn không có trên A1 mini/A2L — vì không có bằng chứng cho thấy các máy này tương thích với những loại sợi đó, nên đã bỏ qua thay vì đoán bừa. Xem [REFERENCES.md](REFERENCES.md) để biết danh sách đầy đủ và lưu ý về nhiệt độ của cấu hình PA-CF/PAHT-CF trên X2D.

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
