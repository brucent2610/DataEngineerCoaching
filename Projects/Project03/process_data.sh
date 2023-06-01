#!/bin/bash
#1. Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới
# sort -t't' -k19 -s tmdb-movies.csv > sorted-tmdb-movies.csv

#2. Lọc ra các bộ phim có đánh giá trung bình trên 7.5 rồi lưu ra một file mới
awk -f awk_02 tmdb-movies.tsv | sort | uniq > tmdb-movies-average-75.csv

#3. Tìm ra phim nào có doanh thu cao nhất và doanh thu thấp nhất
awk -f awk_03 tmdb-movies.tsv > tmdb-movies-min-max-revenue.csv

#4. Tính tổng doanh thu tất cả các bộ phim
awk -f awk_04 tmdb-movies.tsv > tmdb-movies-total-revenue.csv

#5. Top 10 bộ phim đem về lợi nhuận cao nhất
awk -f awk_05 tmdb-movies.tsv | sort -r -t $'\t' -g -k2,2 | head -n 10 > tmdb-movies-top-10-profit.csv

#6. Đạo diễn nào có nhiều bộ phim nhất và diễn viên nào đóng nhiều phim nhất
awk -f awk_06.1 tmdb-movies.tsv | sort | uniq -c | sort -nr | head -n 100 > tmdb-movies-top-director.csv
awk -f awk_06.2 tmdb-movies.tsv | sort | uniq -c | sort -nr | head -n 100 > tmdb-movies-top-cast.csv

#7. Thống kê số lượng phim theo các thể loại. Ví dụ có bao nhiêu phim thuộc thể loại Action, bao nhiêu thuộc thể loại Family, ….
awk -f awk_07 tmdb-movies.tsv | sort | uniq -c | sort -nr | head -n 100 > tmdb-movies-top-genres.csv