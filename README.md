# Scores distributor version 1.0

**Scores distributor** là một chương trình thống kê số liệu.

- [Yêu cầu](#Yêu-cầu)
- [Cách sử dụng](#Cách-sử-dụng)
- [Kết quả thống kê](#Kết-quả-thống-kê)
- [Ví dụ](#Ví-dụ)
- [Điều chỉnh các thành phần thống kê](#Điều-chỉnh-các-thành-phần-thống-kê)

## Yêu cầu

* Để chạy được code thì cần phải có bộ dịch python, có thể tải ở https://www.python.org.

## Cách sử dụng

* Ở thư mục chứa code chạy lệnh trong terminal.
```
python app.py
```
hoặc 
```
python3 app.py
````
* Cửa sổ chương trình sẽ mở và có dạng như sau:

<img src="resource\README\interface.svg" width = 450>
</br></br>

* Chương trình có thể thống kê cho nhiều phần dữ liệu cùng một lúc.

* Ở vùng nhập dữ liệu gồm 4 loại dòng:
    1. **Loại có kí tự đầu là `#`**: đây là dòng heading, chương trình sẽ in ra dòng này ở trên đầu của từng phần dữ liệu.
    2. **Loại có 2 kí tự đầu là `//`**: đây là dòng comment, chương trình sẽ bỏ qua dòng này.
    3. **Loại chỉ có DUY NHẤT một số thực**: đây là dòng chứa số liệu cần thống kê, chương trình sẽ đọc số liệu này để xử lí (số thực này có thể có dạng `1e10`; `-1E34`; ...).
    4. **Loại chỉ có DUY NHẤT 3 kí tự `...`**: đây là dòng kết thúc của một phần dữ liệu gồm 3 loại dòng trên, chương trình sẽ in ra kết quả thống kê tương ứng cho phần này, nếu vẫn còn dòng tiếp theo thì chương trình sẽ khởi tạo lại và bắt đầu thống kê số liệu của phần dữ liệu mới.
* ***CHÚ Ý: Mỗi phần dữ liệu đều phải kết thúc bằng dòng loại 4 (dòng "`...`"), tất cả các dòng trong đầu vào phải thuộc một trong 4 loại dòng trên, nếu không thì chương trình có thể bị lỗi khi xử lí.***
* Khi nhập xong thì bấm **nút xử lí dữ liệu** (get statistics) ở dưới cùng để lấy kết quả thống kê.

## Kết quả thống kê

* Kết quả thống kê gồm các phần thống kê của các phần dữ liệu khác nhau, ngăn cách nhau bởi dòng `---------------------`
    * Các dòng có kí tự đầu là `#` sẽ được đặt ở đầu của từng  phần kết quả thống kê tương ứng.
    * Tiếp theo là các dòng là thành phần cần thống kê có dạng `<Tên thống kê> : <số lượng số thuộc thành phần thống kê>`.
    * Dòng cuối của thành phần là tổng số lượng số liệu thống kê.

## Ví dụ

* Đây là một đầu vào gồm số liệu điểm của học sinh trong một bài kiểm tra:

<img src="resource\README\example.png" width=400>

* Về chi tiết đầu vào có thể xem tại [đây](resource/README/data-example).

## Điều chỉnh các thành phần thống kê

* Hiện tại thành phần thống kê là dành cho điểm số (0->10).
* Để điều chỉnh thì có thể chỉnh ở file [ranges.json](ranges.json).
* Đây là một kiểu dictionary, mỗi phần tử có 2 giá `key` và `value`:
    * Giá trị `key` có dạng "`*|*`", dấu `*` có thể có giá trị nằm trong tập `{"<=","<","==","!=",">",">="}`.
    * Giá trị `value` là một danh sách, một phần tử trong danh sách có dạng `[x, y, s]` gồm ba giá trị `x`, `y` và `s`, `x` và `y` là hai số thực dùng cho giá trị `key` ở trên, khi xét đến một số liệu `a` thì chương trình sẽ kiểm tra mệnh đề "`x "*" a "*" y`", ở đây 2 dấu `"*"` lần lượt là 2 dấu trong "`*|*`", nếu đúng thì sẽ đếm vào thành phần tương ứng, nếu sai thì ngược lại, `s` là một xâu là tên của thành phần, `s` sẽ được in ra và tiếp theo là số lượng số thuộc thành phần.
        * **Ví dụ**: giá trị `key` là "`<=|<`" thì chương trình sẽ kiểm tra xem "`x <= a < y`" có đúng hay không, nếu đúng thì sẽ đếm vào thành phần tương ứng (là thành phần `>= x` và `< y`), nếu sai thì ngược lại, giả sử `s = "x --> <y"` và số lượng số thuộc thành phần là `23` thì sau khi xử lí xong thì chương trình sẽ in ra ở dòng mới là "`x --> <y : 23`".