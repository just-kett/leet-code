# [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

**Độ khó:** Medium  
**Liên kết bài tập:** [https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

---

## Đề bài

Một chuỗi dấu ngoặc được coi là **hợp lệ** khi và chỉ khi:
- Nó là một chuỗi rỗng,
- Nó có thể được viết dưới dạng `AB` (`A` nối với `B`), trong đó `A` và `B` đều là các chuỗi hợp lệ, hoặc
- Nó có thể được viết dưới dạng `(A)`, trong đó `A` là một chuỗi hợp lệ.

Cho một chuỗi dấu ngoặc `s`. Trong một thao tác (nước đi), bạn có thể chèn một dấu ngoặc vào bất kỳ vị trí nào trong chuỗi.
- Ví dụ: nếu $s = \text{"()))"}$, bạn có thể chèn một dấu ngoặc mở để trở thành $\text{"(()))"}$ hoặc một dấu ngoặc đóng để trở thành $\text{"())))"}$.

Hãy trả về **số thao tác tối thiểu** cần thực hiện để biến `s` thành một chuỗi hợp lệ.

---

## Ví dụ

### Ví dụ 1:
- **Đầu vào:** `s = "())"`
- **Đầu ra:** `1`

### Ví dụ 2:
- **Đầu vào:** `s = "((("`
- **Đầu ra:** `3`

---

## Ràng buộc

- $1 \le \text{s.length} \le 1000$
- `s[i]` chỉ có thể là `'('` hoặc `')'`.