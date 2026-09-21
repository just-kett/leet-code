# 1306. Jump Game III (Medium)

## Đề bài
Cho một mảng các số nguyên không âm `arr`, ban đầu bạn đang đứng ở vị trí `start` của mảng. 

Khi đang ở chỉ số `i`, bạn có thể nhảy tới vị trí `i + arr[i]` hoặc `i - arr[i]`. Hãy kiểm tra xem bạn có thể nhảy tới bất kỳ chỉ số nào có giá trị bằng `0` hay không.

Lưu ý: Bạn không được phép nhảy ra ngoài phạm vi của mảng ở bất kỳ thời điểm nào.

---

### Ví dụ 1:
- **Đầu vào:** `arr = [4, 2, 3, 0, 3, 1, 2]`, `start = 5`
- **Đầu ra:** `true`
- **Giải thích:**  
  Tất cả các cách có thể để đến vị trí có giá trị bằng `0` (chỉ số 3) là:
  - Chỉ số $5 \to 4 \to 1 \to 3$
  - Chỉ số $5 \to 6 \to 4 \to 1 \to 3$
