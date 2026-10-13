# LeetCode 3727: Maximum Alternating Sum of Squares (Tổng bình phương đan dấu lớn nhất)

* **Link bài gốc:** [https://leetcode.com/problems/maximum-alternating-sum-of-squares/](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)
* **Độ khó:** Medium
* **Chủ đề:** Array, Greedy, Sorting

---

## 1. Đề bài (Description)

Cho một mảng số nguyên `nums`. Bạn có thể sắp xếp lại các phần tử của mảng theo bất kỳ thứ tự nào.

**Điểm đan dấu (Alternating score)** của một mảng $arr$ được định nghĩa như sau:

$$score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + \dots$$

**Yêu cầu:** Trả về một số nguyên biểu diễn giá trị lớn nhất có thể của điểm đan dấu sau khi sắp xếp lại các phần tử trong `nums`.

---

## 2. Ví dụ (Examples)

### Ví dụ 1:

* **Đầu vào:** `nums = [1, 2, 3]`
* **Đầu ra:** `12`
* **Giải thích:**  
  Một cách sắp xếp hợp lệ cho `nums` là `[2, 1, 3]`, cách này cho điểm đan dấu lớn nhất trong tất cả các cách sắp xếp có thể:  
  $$score = 2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12$$

### Ví dụ 2:

* **Đầu vào:** `nums = [1, -1, 2, -2, 3, -3]`
* **Đầu ra:** `16`
* **Giải thích:**  
  Một cách sắp xếp hợp lệ cho `nums` là `[-3, -1, -2, 1, 3, 2]`, cách này cho điểm đan dấu lớn nhất trong tất cả các cách sắp xếp có thể:  
  $$score = (-3)^2 - (-1)^2 + (-2)^2 - (1)^2 + 3^2 - 2^2 = 9 - 1 + 4 - 1 + 9 - 4 = 16$$

---

## 3. Ràng buộc (Constraints)

* $1 \le nums.length \le 10^5$
* $-4 \times 10^4 \le nums[i] \le 4 \times 10^4$