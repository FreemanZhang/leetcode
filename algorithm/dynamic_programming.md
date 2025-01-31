- [Dynamic Programming](#dynamic-programming)
    - [1937.Maximum-Number-of-Points-with-Cost \(H-\)](#1937maximum-number-of-points-with-cost-h-)
  - [基本型 I](#基本型-i)
  - [基本型 II](#基本型-ii)
  - [走迷宫型](#走迷宫型)
  - [背包型](#背包型)
  - [键盘型](#键盘型)
  - [To Do or Not To Do](#to-do-or-not-to-do)
  - [区间型 I](#区间型-i)
  - [区间型 II](#区间型-ii)
  - [双序列型](#双序列型)
  - [状态压缩DP](#状态压缩dp)
    - [枚举集合的子集](#枚举集合的子集)
    - [二分图](#二分图)
  - [Catalan](#catalan)
  - [Permutation](#permutation)

# [Dynamic Programming](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming)

[264.Ugly-Number-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/264.Ugly-Number-II) \(H-\)  
[313.Super-Ugly-Number](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/313.Super-Ugly-Number) \(H-\)  
[091.Decode-Ways](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/091.Decode-Ways) \(M\)  
[639.Decode-Ways-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/639.Decode-Ways-II) \(H\)  
[634.Find-the-Derangement-of-An-Array](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/634.Find-the-Derangement-of-An-Array) \(H\)  
823.Binary-Trees-With-Factors \(M+\)  
[221.Maximal-Square](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/221.Maximal-Square) \(H-\)  
[1277.Count-Square-Submatrices-with-All-Ones](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1277.Count-Square-Submatrices-with-All-Ones) \(M+\)  
[600.Non-negative-Integers-without-Consecutive-Ones](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/600.Non-negative-Integers-without-Consecutive-Ones) \(H\)  
[656.Coin-Path](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/656.Coin-Path) \(H-\)  
[053.Maximum-Subarray](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/053.Maximum-Subarray) \(E+\)  
[152.Maximum-Product-Subarray](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/152.Maximum-Product-Subarray) \(M+\)  
[818.Race-Car](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/818.Race-Car) \(H\)  
[377.Combination-Sum-IV](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/377.Combination-Sum-IV) \(M\)  
[837.New-21-Game](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/837.New-21-Game) \(H-\)  
[887.Super-Egg-Drop](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/887.Super-Egg-Drop) \(H\)  
[1884.Egg-Drop-With-2-Eggs-and-N-Floors](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1884.Egg-Drop-With-2-Eggs-and-N-Floors) \(H-\)  
[920.Number-of-Music-Playlists](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/920.Number-of-Music-Playlists) \(H\)  
[940.Distinct-Subsequences-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/940.Distinct-Subsequences-II) \(H\)  
[1987.Number-of-Unique-Good-Subsequences](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1987.Number-of-Unique-Good-Subsequences) \(H\)  
[446.Arithmetic-Slices-II-Subsequence](https://github.com/wisdompeak/LeetCode/tree/master/Hash/446.Arithmetic-Slices-II-Subsequence) \(H-\)  
[1027.Longest-Arithmetic-Sequence](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1027.Longest-Arithmetic-Sequence) \(M+\)  
[1269.Number-of-Ways-to-Stay-in-the-Same-Place-After-Some-Steps](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1269.Number-of-Ways-to-Stay-in-the-Same-Place-After-Some-Steps) \(M+\)  
[1316.Distinct-Echo-Substrings](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1316.Distinct-Echo-Substrings) \(M+\)  
[1420.Build-Array-Where-You-Can-Find-The-Maximum-Exactly-K-Comparisons](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1420.Build-Array-Where-You-Can-Find-The-Maximum-Exactly-K-Comparisons) \(H-\)  
1444. Number of Ways of Cutting a Pizza \(TBD\)  
[1531.String-Compression-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1531.String-Compression-II) \(H+\)  
[1575.Count-All-Possible-Routes](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1575.Count-All-Possible-Routes) \(M+\)  
[1621.Number-of-Sets-of-K-Non-Overlapping-Line-Segments](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1621.Number-of-Sets-of-K-Non-Overlapping-Line-Segments) \(H\)  
[1639.Number-of-Ways-to-Form-a-Target-String-Given-a-Dictionary](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1639.Number-of-Ways-to-Form-a-Target-String-Given-a-Dictionary) \(H-\)  
[1692.Count-Ways-to-Distribute-Candies](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1692.Count-Ways-to-Distribute-Candies) \(H-\)  
[1787.Make-the-XOR-of-All-Segments-Equal-to-Zero](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1787.Make-the-XOR-of-All-Segments-Equal-to-Zero) \(H\)  
[1872.Stone-Game-VIII](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1872.Stone-Game-VIII) \(H-\)  
[1900.The-Earliest-and-Latest-Rounds-Where-Players-Compete](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1900.The-Earliest-and-Latest-Rounds-Where-Players-Compete) \(H\)  

### [1937.Maximum-Number-of-Points-with-Cost](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1937.Maximum-Number-of-Points-with-Cost) \(H-\)  
* Google DP: https://expl.ai/USLKFRP

[1955.Count-Number-of-Special-Subsequences](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1955.Count-Number-of-Special-Subsequences) \(H-\)

## 基本型 I

[198.House-Robber](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/198.House-Robber) \(E\)  
[213.House-Robber-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/213.House-Robber-II) \(M+\)  
[1388.Pizza-With-3n-Slices](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1388.Pizza-With-3n-Slices) \(H-\)  
[276.Paint-Fence](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/276.Paint-Fence) \(H-\)  
[265.Paint-House-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/265.Paint-House-II) \(H\)  
[1473.Paint-House-III](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1473.Paint-House-III) \(H-\)  
[376.Wiggle-Subsequence](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/376.Wiggle-Subsequence) \(H-\)  
[123.Best-Time-to-Buy-and-Sell-Stock-III](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/123.Best-Time-to-Buy-and-Sell-Stock-III) \(M+\)  
[188.Best-Time-to-Buy-and-Sell-Stock-IV](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/188.Best-Time-to-Buy-and-Sell-Stock-IV) \(H\)  
[309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown) \(H-\)  
[714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee](https://github.com/wisdompeak/LeetCode/blob/master/Dynamic_Programming/714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee) \(M+\)  
[514.Freedom-Trail](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/514.Freedom-Trail) \(H-\)  
[740.Delete-and-Earn](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/740.Delete-and-Earn) \(H-\)  
[552.Student-Attendance-Record-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/552.Student-Attendance-Record-II) \(H\)  
[801.Minimum-Swaps-To-Make-Sequences-Increasing](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/801.Minimum-Swaps-To-Make-Sequences-Increasing) \(M\)  
[1223.Dice-Roll-Simulation](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1223.Dice-Roll-Simulation) \(H-\)  
[1262.Greatest-Sum-Divisible-by-Three](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1262.Greatest-Sum-Divisible-by-Three) \(M+\)  
[1363.Largest-Multiple-of-Three](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1363.Largest-Multiple-of-Three) \(H\)  
[1419.Minimum-Number-of-Frogs-Croaking](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1419.Minimum-Number-of-Frogs-Croaking) \(M\)  
[1548.The-Most-Similar-Path-in-a-Graph](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1548.The-Most-Similar-Path-in-a-Graph) \(M+\)  
[1746.Maximum-Subarray-Sum-After-One-Operation](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1746.Maximum-Subarray-Sum-After-One-Operation) \(M+\)  
[1824.Minimum-Sideway-Jumps](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1824.Minimum-Sideway-Jumps) \(M\)  
[1839.Longest-Substring-Of-All-Vowels-in-Order](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1839.Longest-Substring-Of-All-Vowels-in-Order) \(M\)  
[1883.Minimum-Skips-to-Arrive-at-Meeting-On-Time](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1883.Minimum-Skips-to-Arrive-at-Meeting-On-Time) \(H\)

## 基本型 II

[368.Largest-Divisible-Subset](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/368.Largest-Divisible-Subset) \(M+\)  
[300.Longest-Increasing-Subsequence](https://github.com/wisdompeak/LeetCode/tree/master/Greedy/300.Longest-Increasing-Subsequence) \(M+\)  
[673.Number-of-Longest-Increasing-Subsequence](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/673.Number-of-Longest-Increasing-Subsequence) \(M+\)  
[960.Delete-Columns-to-Make-Sorted-III](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/960.Delete-Columns-to-Make-Sorted-III) \(H-\)  
[983.Minimum-Cost-For-Tickets](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/983.Minimum-Cost-For-Tickets) \(H-\)  
[1043.Partition-Array-for-Maximum-Sum](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1043.Partition-Array-for-Maximum-Sum)\(M+\)  
[1105.Filling-Bookcase-Shelves](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1105.Filling-Bookcase-Shelves) \(H-\)  
[1959.minimum-total-space-wasted-with-k-resizing-operations](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1959.minimum-total-space-wasted-with-k-resizing-operations) \(H-\)  
[1416.Restore-The-Array](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1416.Restore-The-Array) \(M+\)  
[1546.Maximum-Number-of-Non-Overlapping-Subarrays-With-Sum-Equals-Target](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1546.Maximum-Number-of-Non-Overlapping-Subarrays-With-Sum-Equals-Target) \(M+\)  
[1626.Best-Team-With-No-Conflicts](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1626.Best-Team-With-No-Conflicts) \(M\)  
[1691.Maximum-Height-by-Stacking-Cuboids](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1691.Maximum-Height-by-Stacking-Cuboids) \(H\)

## 走迷宫型

[120.Triangle](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/120.Triangle) \(E\)  
[174.Dungeon-Game](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/174.Dungeon-Game) \(H-\)  
[741.Cherry-Pickup](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/741.Cherry-Pickup) \(H-\)  
[1463.Cherry-Pickup-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1463.Cherry-Pickup-II) \(M\)  
[576.Out-of-Boundary-Paths](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/576.Out-of-Boundary-Paths) \(H\)  
[931.Minimum-Falling-Path-Sum](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/931.Minimum-Falling-Path-Sum) \(M\)  
[1289.Minimum-Falling-Path-Sum-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1289.Minimum-Falling-Path-Sum-II) \(M+\)  
[1301.Number-of-Paths-with-Max-Score](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1301.Number-of-Paths-with-Max-Score) \(M+\)  
[1594.Maximum-Non-Negative-Product-in-a-Matrix](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1594.Maximum-Non-Negative-Product-in-a-Matrix) \(M\)

## 背包型

[322.Coin-Change](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/322.Coin-Change) \(M\)  
[416.Partition-Equal-Subset-Sum](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/416.Partition-Equal-Subset-Sum) \(M+\)  
[518.Coin-Change-2](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/518.Coin-Change-2) \(H-\)  
[474.Ones-and-Zeroes](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/474.Ones-and-Zeroes) \(H-\)  
[494.Target-Sum](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/494.Target-Sum) \(M+\)  
[805.Split-Array-With-Same-Average](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/805.Split-Array-With-Same-Average) \(H\)  
[879.Profitable-Schemes](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/879.Profitable-Schemes) \(M+\)  
[956.Tallest-Billboard](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/956.Tallest-Billboard) \(H\)  
[1049.Last-Stone-Weight-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1049.Last-Stone-Weight-II) \(H-\)  
[1449.Form-Largest-Integer-With-Digits-That-Add-up-to-Target](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1449.Form-Largest-Integer-With-Digits-That-Add-up-to-Target) \(H-\)  
[1981.Minimize-the-Difference-Between-Target-and-Chosen-Elements](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1981.Minimize-the-Difference-Between-Target-and-Chosen-Elements) \(M+\)

## 键盘型

[650.2-Keys-Keyboard](https://github.com/wisdompeak/LeetCode/blob/master/Dynamic_Programming/650.2-Keys-Keyboard) \(M+\)  
[651.4-Keys-Keyboard](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/651.4-Keys-Keyboard) \(M+\)  
[935.Knight-Dialer](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/935.Knight-Dialer) \(M\)  
[1320.Minimum-Distance-to-Type-a-Word-Using-Two-Fingers](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1320.Minimum-Distance-to-Type-a-Word-Using-Two-Fingers) \(H\)

## To Do or Not To Do

[487.Max-Consecutive-Ones-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/487.Max-Consecutive-Ones-II) \(H-\)  
[1186.Maximum-Subarray-Sum-with-One-Deletion](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1186.Maximum-Subarray-Sum-with-One-Deletion) \(H-\)  
[1187.Make-Array-Strictly-Increasing](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1187.Make-Array-Strictly-Increasing) \(H-\)  
[1909.Remove-One-Element-to-Make-the-Array-Strictly-Increasing](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1909.Remove-One-Element-to-Make-the-Array-Strictly-Increasing) \(H-\)

## 区间型 I

[132.Palindrome-Partitioning-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/132.Palindrome-Partitioning-II) \(H-\)  
[410.Split-Array-Largest-Sum](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/410.Split-Array-Largest-Sum) \(H\)  
[813.Largest-Sum-of-Averages](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/813.Largest-Sum-of-Averages) \(H-\)  
[1278.Palindrome-Partitioning-III](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1278.Palindrome-Partitioning-III) \(H\)  
[1335.Minimum-Difficulty-of-a-Job-Schedule](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1335.Minimum-Difficulty-of-a-Job-Schedule) \(M+\)  
[1478.Allocate-Mailboxes](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1478.Allocate-Mailboxes) \(H\)  
[1977.Number-of-Ways-to-Separate-Numbers](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1977.Number-of-Ways-to-Separate-Numbers) \(H\)

## 区间型 II

[131.Palindrome-Partitioning](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/131.Palindrome-Partitioning) \(M+\)  
[312.Burst-Balloons](https://github.com/wisdompeak/LeetCode/tree/master/DFS/312.Burst-Balloons) \(H-\)  
[375.Guess-Number-Higher-or-Lower-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/375.Guess-Number-Higher-or-Lower-II) \(H\)  
[471.Encode-String-with-Shortest-Length](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/471.Encode-String-with-Shortest-Length) \(H\)  
[516.Longest-Palindromic-Subsequence](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/516.Longest-Palindromic-Subsequence) \(H-\)  
[546.Remove-Boxes](https://github.com/wisdompeak/LeetCode/tree/master/DFS/546.Remove-Boxes) \(H+\)  
[664.Strange-Printer](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/664.Strange-Printer) \(H\)  
[730.Count-Different-Palindromic-Subsequences](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/730.Count-Different-Palindromic-Subsequences) \(H\)  
[1000.Minimum-Cost-to-Merge-Stones](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1000.Minimum-Cost-to-Merge-Stones) \(H\)  
[1130.Minimum-Cost-Tree-From-Leaf-Values](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1130.Minimum-Cost-Tree-From-Leaf-Values) \(M+\)  
[1246.Palindrome-Removal](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1246.Palindrome-Removal) \(H\)  
[1039.Minimum-Score-Triangulation-of-Polygon](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1039.Minimum-Score-Triangulation-of-Polygon) \(H\)  
[1547.Minimum-Cost-to-Cut-a-Stick](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1547.Minimum-Cost-to-Cut-a-Stick) \(M\)  
[1682.Longest-Palindromic-Subsequence-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1682.Longest-Palindromic-Subsequence-II) \(H\)  
[1690.Stone-Game-VII](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1690.Stone-Game-VII) \(H-\)  
[1745.Palindrome-Partitioning-IV](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1745.Palindrome-Partitioning-IV) \(M\)  
[1770.Maximum-Score-from-Performing-Multiplication-Operations](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1770.Maximum-Score-from-Performing-Multiplication-Operations) \(H-\)

## 双序列型

[010.Regular-Expression-Matching](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/010.Regular-Expression-Matching) \(H\)  
[044.Wildcard-Matching](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/044.Wildcard-Matching) \(H-\)  
[097.Interleaving-String](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/097.Interleaving-String) \(H-\)  
[072.Edit-Distance](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/072.Edit-Distance) \(H-\)  
[115.Distinct-Subsequences](https://github.com/wisdompeak/LeetCode/blob/master/Dynamic_Programming/115.Distinct-Subsequences/) \(H-\)  
[583.Delete-Operation-for-Two-Strings](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/583.Delete-Operation-for-Two-Strings) \(M+\)  
[712.Minimum-ASCII-Delete-Sum-for-Two-Strings](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/712.Minimum-ASCII-Delete-Sum-for-Two-Strings) \(M+\)  
[718.Maximum-Length-of-Repeated-Subarray](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/718.Maximum-Length-of-Repeated-Subarray) \(M\)  
[727.Minimum-Window-Subsequence](https://github.com/wisdompeak/LeetCode/tree/master/Greedy/727.Minimum-Window-Subsequence) \(H-\)  
[1035.Uncrossed-Lines](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1035.Uncrossed-Lines) \(M\)  
[1092.Shortest-Common-Supersequence](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1092.Shortest-Common-Supersequence) \(H-\)  
[1143.Longest-Common-Subsequence](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1143.Longest-Common-Subsequence) \(M\)  
[1216.Valid-Palindrome-III](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1216.Valid-Palindrome-III) \(M+\)  
[1312.Minimum-Insertion-Steps-to-Make-a-String-Palindrome](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1312.Minimum-Insertion-Steps-to-Make-a-String-Palindrome) \(M+\)  
[1458.Max-Dot-Product-of-Two-Subsequences](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1458.Max-Dot-Product-of-Two-Subsequences) \(M\)  
[1771.Maximize-Palindrome-Length-From-Subsequences](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1771.Maximize-Palindrome-Length-From-Subsequences) \(H\)

## 状态压缩DP

[465.Optimal-Account-Balancing](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/465.Optimal-Account-Balancing) \(H\)  
[691.Stickers-to-Spell-Word](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/691.Stickers-to-Spell-Word) \(H\)  
[943.Find-the-Shortest-Superstring](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/943.Find-the-Shortest-Superstring) \(H+\)  
[1125.Smallest-Sufficient-Team](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1125.Smallest-Sufficient-Team) \(H\)  
[1349.Maximum-Students-Taking-Exam](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1349.Maximum-Students-Taking-Exam) \(H\)  
[1411.Number-of-Ways-to-Paint-N×3-Grid](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1411.Number-of-Ways-to-Paint-N%C3%973-Grid) \(M\)  
[1434.Number-of-Ways-to-Wear-Different-Hats-to-Each-Other](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1434.Number-of-Ways-to-Wear-Different-Hats-to-Each-Other) \(H-\)  
[1595.Minimum-Cost-to-Connect-Two-Groups-of-Points](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1595.Minimum-Cost-to-Connect-Two-Groups-of-Points) \(H\)  
[1659.Maximize-Grid-Happiness](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1659.Maximize-Grid-Happiness) \(H\)  
[1681.Minimum-Incompatibility](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1681.Minimum-Incompatibility) \(H\)  
[1723.Find-Minimum-Time-to-Finish-All-Jobs](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1723.Find-Minimum-Time-to-Finish-All-Jobs) \(H-\)  
[1799.Maximize-Score-After-N-Operations](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1799.Maximize-Score-After-N-Operations) \(H-\)  
[1931.Painting-a-Grid-With-Three-Different-Colors](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1931.Painting-a-Grid-With-Three-Different-Colors) \(M+\)  
[1994.The-Number-of-Good-Subsets](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1994.The-Number-of-Good-Subsets) \(H\)

### 枚举集合的子集

[1494.Parallel-Courses-II](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1494.Parallel-Courses-II) \(H\)  
[1655.Distribute-Repeating-Integers](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1655.Distribute-Repeating-Integers) \(H\)  
[1986.Minimum-Number-of-Work-Sessions-to-Finish-the-Tasks](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1986.Minimum-Number-of-Work-Sessions-to-Finish-the-Tasks) \(M+\)

### 二分图

[1066.Campus-Bikes-II](https://github.com/wisdompeak/LeetCode/tree/master/BFS/1066.Campus-Bikes-II) \(H+\)  
[1879.Minimum-XOR-Sum-of-Two-Arrays](https://github.com/wisdompeak/LeetCode/tree/master/BFS/1879.Minimum-XOR-Sum-of-Two-Arrays) \(H\)  
[1947.Maximum-Compatibility-Score-Sum](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1947.Maximum-Compatibility-Score-Sum) \(H\)

## Catalan

[096.Unique-Binary-Search-Trees](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/096.Unique-Binary-Search-Trees) \(M+\)  
\[1259.Handshakes-That-Don't-Cross\]\([https://github.com/wisdompeak/LeetCode/tree/master/Dynamic\_Programming/1259.Handshakes-That-Don't-Cross](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1259.Handshakes-That-Don't-Cross)\) \(M+\)

## Permutation

[629.K-Inverse-Pairs-Array](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/629.K-Inverse-Pairs-Array) \(H\)  
[903.Valid-Permutations-for-DI-Sequence](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/903.Valid-Permutations-for-DI-Sequence) \(H\)  
[1866.Number-of-Ways-to-Rearrange-Sticks-With-K-Sticks-Visible](https://github.com/wisdompeak/LeetCode/tree/master/Math/1866.Number-of-Ways-to-Rearrange-Sticks-With-K-Sticks-Visible) \(H\)
