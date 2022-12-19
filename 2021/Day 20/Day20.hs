main :: IO ()
main = do
    input <- readFile "input.txt"
    let imageAlgo = head   $ lines input
    let image     = drop 2 $ lines input
    print image