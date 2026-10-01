# [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/)

## Mô tả bài toán
Viết truy vấn SQL để tìm tất cả các số xuất hiện ít nhất **3 lần liên tiếp**. 

Trả về bảng kết quả theo bất kỳ thứ tự nào.

### Cấu trúc bảng `Logs`
| Cột | Kiểu dữ liệu | Mô tả |
| :--- | :--- | :--- |
| `id` | int | Khóa chính (tự động tăng) |
| `num` | varchar | Giá trị số |

---

## Ví dụ

**Đầu vào:**

Bảng `Logs`:
| id | num |
| :--- | :--- |
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 1 |
| 6 | 2 |
| 7 | 2 |'


**Đầu ra:**

| ConsecutiveNums |
| :--- |
| 1 |

**Giải thích:** Số `1` là số duy nhất xuất hiện ít nhất 3 lần liên tiếp (tại các `id` 1, 2, 3).