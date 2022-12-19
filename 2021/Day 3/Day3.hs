{-# LANGUAGE LambdaCase #-}
{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import Data.List
type Binary = [Bool]

main :: IO ()
main = do
    input <- readFile "input.txt"
    let bin = map (map (\case '0' -> False ; '1' -> True)) (lines input)
    print $ decimal (gamma bin) * decimal (epsilon bin)

decimal :: Binary -> Int
decimal = foldr (\x y -> fromEnum x + 2*y) 0

epsilon :: [Binary] -> Binary
epsilon bins = reverse $ foldr ((:) . least) [] (transpose bins)

gamma :: [Binary] -> Binary 
gamma bins = reverse $ foldr ((:) . most) [] (transpose bins)

most :: Binary -> Bool
most bin = head $ snd $ maximum $ [(length xs, xs) | xs <- group $ sort bin]

least :: Binary -> Bool
least bin = head $ snd $ minimum $ [(length xs, xs) | xs <- group $ sort bin]