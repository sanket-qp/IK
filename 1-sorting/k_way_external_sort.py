"""
sort 256 Billion 32 bit integers with 16 GB memory

Table to remember
-----------------
https://www.eagle-web-designs.com/cool_stuff/ByteConversion.html

1 byte (B) = 8 bits (b)
1 Kilobyte (K / KB) = 2^10 bytes = 1,024 bytes
1 Megabyte (M / MB) = 2^20 bytes = 1,048,576 bytes
1 Gigabyte (G / GB) = 2^30 bytes = 1,073,741,824 bytes
1 Terabyte (T / TB) = 2^40 bytes = 1,099,511,627,776 bytes


1 byte (B) = 8 bits (b)
1 Kilobyte (K / KB) = 10^3 bytes = 1,000 bytes = 2^10
1 Megabyte (M / MB) = 10^6 bytes = 1,000,000 bytes
1 Gigabyte (G / GB) = 10^9 bytes = 1,000,000,000 bytes
1 Terabyte (T / TB) = 10^12 bytes = 1,000,000,000,000 bytes


Million = MB = 2^20 = 10^6
Billion = GB = 2^30 = 10^9
Trillion = TB = 2^40 = 10^12
-----------------------------------------------------------------

Storage required for 256 B 32 bit integers
256 = (2 ^ 8 )
Billion = (10 ^ 9 = 2 ^ 30)
32 bit = ( 2 ^ 5 bits)
so total storage required = 2^8 * 2^30 * 2^5 = 2^43 bits OR 2^43/2^3 = 2^40 bytes = 1 TB
------

Memory Given 16 GB
16 = 2^4
G = 2^30
B = 2 ^ 3 bits
total memory = 2 ^4 * 2 ^ 30 * 2 ^ 3 = 2^37 bits or 2^34 bytes = 16 GB

so we have to partition (divide) our data (2^43 bits) by available memory (2^37 bits)
total_partitions = 2^43 / 2^37 = 2 ^ 6 = 64 partitions
single_partition_size = 2^34

just to verify if the math works out, single_partition_size * total_partitions = total_data_size
2^34 * 2^6 =  2^43

--------
sorting

(1) so we divide our original data in to 64 partitions
(2) sort each partition and save it on the disk
(3) now pick 2 partitions and merge them and save the merged (sorted) list back to the disk
    (1) to merge 2 partitions, we required o(n) extra space
    (2) so we can't merge two 16 GB partitions as total memory is 16 G
    (3) so we have to read only 8 GB (4 G from partion 1 and 4 G from 2nd)
    (4) sort 2 partitions by reading 4G chunks and save one sorted partition which is 32 G in total

this is how the process should look like

size per partition (GB)  -  number of partitions
-----------
16   -  64
32   -  32
64   -  16
128  -   8
256  -   4
512  -   2
1024 -   1
"""
