# [3286. Find a Safe Walk Through a Grid](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/)

**Độ khó:** Medium  
**Link bài gốc:** [https://leetcode.com/problems/find-a-safe-walk-through-a-grid/](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/)

---

## Đề bài

Bạn được cho một ma trận nhị phân `grid` có kích thước $m \times n$ và một số nguyên `health` biểu thị lượng máu ban đầu.

Bạn bắt đầu tại ô góc trên bên trái `(0, 0)` và muốn đi đến ô góc dưới bên phải `(m - 1, n - 1)`.

- Bạn có thể di chuyển lên, xuống, sang trái hoặc sang phải giữa các ô kề nhau, miễn là lượng máu của bạn **luôn lớn hơn $0$** (tức là $\ge 1$).
- Các ô $(i, j)$ có `grid[i][j] = 1` được coi là ô nguy hiểm và sẽ **làm giảm $1$ máu** của bạn ngay khi bạn bước vào (bao gồm cả ô xuất phát nếu ô xuất phát có giá trị $1$).
- Các ô có `grid[i][j] = 0` là ô an toàn và không làm giảm máu.

Hãy trả về `true` nếu bạn có thể đi đến ô đích với lượng máu còn lại từ $1$ trở lên, ngược lại trả về `false`.

---

## Ví dụ

### Ví dụ 1:

**Đầu vào (Input):**
```text
grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1
```

**Đầu ra (Output):**
```text
true
```

**Giải thích:**
Có thể đến ô đích an toàn bằng cách chỉ đi qua các ô an toàn có giá trị bằng $0$ (ví dụ: `(0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (1,2) -> (0,2) -> (0,3) -> (0,4) -> (1,4) -> (2,4)`). Vì chỉ đi qua các ô an toàn, bạn không bị mất máu và đến đích với lượng máu còn nguyên là $1$.

---

### Ví dụ 2:

**Đầu vào (Input):**
```text
grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
```

**Đầu ra (Output):**
```text
false
```

**Giải thích:**
Cần ít nhất $4$ điểm máu để có thể đến được ô đích một cách an toàn. Với `health = 3`, không có đường đi nào giữ được lượng máu lớn hơn $0$ khi tới đích.

---

### Ví dụ 3:

**Đầu vào (Input):**
```text
grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5
```

**Đầu ra (Output):**
```text
true
```

**Giải thích:**
Bạn có thể đi đến ô cuối cùng an toàn nếu đi qua ô an toàn ở tâm `(1, 1)` (ví dụ theo đường: `(0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2)` với số ô nguy hiểm gặp phải là $4$). Với `health = 5`, bạn còn lại $1$ máu khi đến đích. Bất kỳ đường đi nào không đi qua ô `(1, 1)` đều tiêu tốn từ $5$ máu trở lên, khiến máu giảm về $0$ hoặc âm trước/khi đến đích.

---

## Ràng buộc (Constraints)

- $m == \text{grid.length}$
- $n == \text{grid}[i]\text{.length}$
- $1 \le m, n \le 50$
- $2 \le m \times n$
- $1 \le \text{health} \le m + n$
- `grid[i][j]` chỉ nhận giá trị $0$ hoặc $1$.