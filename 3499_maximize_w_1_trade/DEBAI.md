# 3499. Maximize Active Section with Trade I

**Độ khó:** Medium  
**Chủ đề:** String, Greedy, Array  

---

## Đề bài

Cho một chuỗi nhị phân $s$ có độ dài $n$:
- Ký tự `'1'` biểu thị một phần tử đang hoạt động (active section).
- Ký tự `'0'` biểu thị một phần tử không hoạt động (inactive section).

Bạn được phép thực hiện **tối đa một lần giao dịch (trade)** để tối đa hóa số lượng `'1'` trong chuỗi $s$. Quy trình giao dịch gồm 2 bước:
1. Đổi một đoạn liên tiếp các ký tự `'1'` nằm giữa hai ký tự `'0'` thành toàn bộ ký tự `'0'`.
2. Sau đó, đổi một đoạn liên tiếp các ký tự `'0'` nằm giữa hai ký tự `'1'` thành toàn bộ ký tự `'1'`.

Trả về *số lượng phần tử hoạt động tối đa* trong chuỗi $s$ sau khi thực hiện giao dịch tối ưu.

> **Lưu ý:** Xem chuỗi $s$ như thể được gắn thêm một ký tự `'1'` vào cả hai đầu ($t = \text{'1'} + s + \text{'1'}$). Hai ký tự này không được tính vào kết quả cuối cùng.

---

## Ví dụ

- **Đầu vào:** `s = "0100"`
- **Đầu ra:** `4`
- **Giải thích:**  
  1. Thêm `'1'` vào hai đầu: `"0100"` $\rightarrow$ `"101001"`.
  2. Chọn đoạn `"1"` ở giữa hai số `'0'` để biến thành `'0'`: `"101001"` $\rightarrow$ `"100001"`.
  3. Chọn toàn bộ đoạn `'0'` ở giữa hai số `'1'` để biến thành `'1'`: `"100001"` $\rightarrow$ `"111111"`.
  4. Bỏ 2 ký tự `'1'` ở đầu và cuối ta được `"1111"`, có tối đa **4** phần tử hoạt động.

---

## Ràng buộc

- $1 \le s.\text{length} \le 10^5$
- $s[i]$ chỉ gồm ký tự `'0'` hoặc `'1'`.