# [877. Stone Game (Trò chơi bốc đá)](https://leetcode.com/problems/stone-game/)

Alice và Bob chơi một trò chơi với các đống đá. Có một số lượng chẵn các đống đá được xếp thành một hàng, và mỗi đống có một số lượng đá nguyên dương là `piles[i]`.

Mục tiêu của trò chơi là kết thúc với nhiều viên đá nhất. Tổng số lượng đá trong tất cả các đống là một số lẻ, vì vậy không thể có kết quả hòa.

Alice và Bob thay phiên nhau thực hiện lượt chơi, trong đó Alice đi trước. Ở mỗi lượt, một người chơi có thể lấy toàn bộ số đá của đống nằm ở **đầu hàng** hoặc **cuối hàng**. Trò chơi tiếp tục cho đến khi không còn đống đá nào nữa, lúc này ai có nhiều đá nhất sẽ là người chiến thắng.

Giả sử Alice và Bob đều chơi một cách tối ưu, hãy trả về `true` nếu Alice thắng trò chơi, hoặc `false` nếu Bob thắng.

---

### Ví dụ 1:

**Đầu vào:** `piles = [5,3,4,5]`  
**Đầu ra:** `true`  
**Giải thích:**  
- Alice bắt đầu trước và chỉ có thể chọn giữa đống đá đầu tiên `5` hoặc đống cuối cùng `5`.
- Giả sử Alice chọn đống `5` đầu tiên, hàng đá còn lại là `[3, 4, 5]`.
- Nếu Bob chọn `3`, hàng còn lại `[4, 5]`, Alice có thể chọn `5` để có tổng cộng `5 + 5 = 10` điểm (nhiều hơn so với Bob).
- Nếu Bob chọn `5`, hàng còn lại `[3, 4]`, Alice có thể chọn `4` để có `5 + 4 = 9` điểm (vẫn nhiều hơn `5 + 3 = 8` của Bob).
- Như vậy, Alice luôn có chiến lược để giành chiến thắng, nên ta trả về `true`.

### Ví dụ 2:

**Đầu vào:** `piles = [3,7,2,3]`  
**Đầu ra:** `true`  

---

### Ràng buộc:

- `2 <= piles.length <= 500`
- `piles.length` là một số chẵn.
- `1 <= piles[i] <= 500`
- `sum(piles[i])` là một số lẻ.