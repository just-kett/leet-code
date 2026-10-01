# [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

**Độ khó:** Medium  
**Chủ đề:** Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect  
---

Cho một mảng các điểm `points` trong đó `points[i] = [xi, yi]` đại diện cho một điểm trên mặt phẳng tọa độ $X-Y$ và một số nguyên $k$, hãy trả về $k$ điểm gần gốc tọa độ $(0, 0)$ nhất.

Khoảng cách giữa hai điểm trên mặt phẳng $X-Y$ được tính bằng khoảng cách Euclidean:

$$\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

Khoảng cách từ một điểm $(x, y)$ tới gốc tọa độ $(0, 0)$ được rút gọn thành:

$$\sqrt{x^2 + y^2}$$

Bạn có thể trả về kết quả theo **bất kỳ thứ tự nào**. Đáp án được đảm bảo là duy nhất (ngoại trừ thứ tự xuất hiện của các điểm).

---

### Ví dụ 1:
- **Input:** `points = [[1,3],[-2,2]]`, `k = 1`
- **Output:** `[[-2,2]]`
- **Giải thích:**
  - Khoảng cách từ $(1, 3)$ đến gốc tọa độ là $\sqrt{1^2 + 3^2} = \sqrt{10}$.
  - Khoảng cách từ $(-2, 2)$ đến gốc tọa độ là $\sqrt{(-2)^2 + 2^2} = \sqrt{8}$.
  - Vì $\sqrt{8} < \sqrt{10}$, nên điểm $(-2, 2)$ gần gốc tọa độ hơn.
  - Ta cần lấy $k = 1$ điểm gần nhất, nên kết quả là `[[-2,2]]`.
