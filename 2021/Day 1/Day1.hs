main :: IO()
main = do
    input <- readFile "input.txt"
    let dataList = map read (lines input) :: [Int]
    print $ solve dataList 1 -- Part 1
    print $ solve dataList 3 -- Part 2

solve :: [Int] -> Int -> Int
solve dataList group = length 
                     $ filter (uncurry (<)) 
                     $ zip dataList (drop group dataList)
