# 595. Big Countries

**Độ khó:** Easy  
**Chủ đề:** Database (SQL / Pandas)

---

## 1. Cấu trúc bảng

### Bảng: `World`

| Column Name | Type    |
| :---        | :---    |
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |

- `name` là khóa chính (cột chứa các giá trị duy nhất) cho bảng này.
- Mỗi hàng cung cấp thông tin về tên quốc gia, châu lục, diện tích, dân số và tổng sản phẩm quốc nội (GDP).

---

## 2. Yêu cầu

Một quốc gia được coi là **lớn (big)** nếu thỏa mãn **ít nhất một** trong hai điều kiện sau:
1. Có diện tích tối thiểu **3.000.000** $\text{km}^2$ (`area >= 3000000`).
2. Có dân số tối thiểu **25.000.000** người (`population >= 25000000`).

Hãy viết truy vấn/hàm để tìm `name`, `population`, và `area` của các quốc gia lớn.  
Kết quả trả về có thể theo bất kỳ thứ tự nào.

---

## 3. Ví dụ

### Đầu vào (`World` table):

| name        | continent | area    | population | gdp          |
| :---        | :---      | :---    | :---       | :---         |
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |

### Đầu ra:

| name        | population | area    |
| :---        | :---       | :---    |
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |

