#!/bin/bash

#Transfer the csv file to correct format to continue process
#Remove the \n character between ," and ", to prevent new line csv
sed -e ':a;N;$!ba;s/,"\([^"]*\)\n\([^"]*\)",/,"\1\2",/g' tmdb-movies.csv > tmdb-movies-transformed-1.csv
#Remove the , between "" to prevent new column csv
sed -e ':a;s/^\(\([^"]*,\?\|"[^",]*",\?\)*"[^",]*\),/\1 /;ta;s/  */ /g' tmdb-movies-transformed-1.csv > tmdb-movies-transformed.csv

echo "Hoan thanh xoa nhung ky tu khong can thiet trong cot"

#1. Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới
awk -f awk_01 tmdb-movies-transformed.csv | sort -r -t $',' -g -k2,2 > tmdb-movies-latest-released-date.csv

echo "Hoan thanh Cau 1"

#2. Lọc ra các bộ phim có đánh giá trung bình trên 7.5 rồi lưu ra một file mới
awk -f awk_02 tmdb-movies-transformed.csv | sort | uniq > tmdb-movies-average-75.csv

echo "Hoan thanh Cau 2"

#3. Tìm ra phim nào có doanh thu cao nhất và doanh thu thấp nhất
awk -f awk_03 tmdb-movies-transformed.csv > tmdb-movies-min-max-revenue.csv

echo "Hoan thanh Cau 3"

#4. Tính tổng doanh thu tất cả các bộ phim
awk -f awk_04 tmdb-movies-transformed.csv > tmdb-movies-total-revenue.csv

echo "Hoan thanh Cau 4"

#5. Top 10 bộ phim đem về lợi nhuận cao nhất
awk -f awk_05 tmdb-movies-transformed.csv | sort -r -t $'\t' -g -k2,2 | head -n 10 > tmdb-movies-top-10-profit.csv

echo "Hoan thanh Cau 5"

#6. Đạo diễn nào có nhiều bộ phim nhất và diễn viên nào đóng nhiều phim nhất
awk -f awk_06.1 tmdb-movies-transformed.csv | sort | uniq -c | sort -nr | head -n 100 > tmdb-movies-top-director.csv
awk -f awk_06.2 tmdb-movies-transformed.csv | sort | uniq -c | sort -nr | head -n 100 > tmdb-movies-top-cast.csv

echo "Hoan thanh Cau 6"

#7. Thống kê số lượng phim theo các thể loại. Ví dụ có bao nhiêu phim thuộc thể loại Action, bao nhiêu thuộc thể loại Family, ….
awk -f awk_07 tmdb-movies-transformed.csv | sort | uniq -c | sort -nr | head -n 100 > tmdb-movies-top-genres.csv

echo "Hoan thanh Cau 7"