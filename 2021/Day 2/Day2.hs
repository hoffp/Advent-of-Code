import System.Console.Haskeline (Interrupt(Interrupt))
type Position  = (Int, Int)
type Direction = (Int, Int)
type State     = (Int, Int, Int)
type Command   = String

main :: IO()
main = do
    input <- readFile "input.txt"
    print $ uncurry (*) $ partOne (lines input)

partOne :: [Command] -> Position
partOne = foldr (newPos . direction) (0,0)

partTwo :: [Command] -> State
partTwo = foldr (newState . aim) (0,0,0)

newPos :: Position -> Direction -> Position
newPos (h,v) (dh,dv) = (nh,nv)
    where nh = h + dh
          nv = v + dv

direction :: Command -> Direction
direction cmd = case words cmd of
    ["forward", x] -> (d,0) where d = read x        :: Int
    ["up", x]      -> (0,d) where d = read x * (-1) :: Int
    ["down", x]    -> (0,d) where d = read x        :: Int
    _              -> (0,0)

newState :: State -> State -> State
newState (h,v,a) (dh,dv,da) = (nh,nv,na)
    where nh = h + dh

aim :: Command -> State -> State
aim cmd (h,d,a) = case words cmd of
    ["forward", x] -> (nh,nd,a) where nh = h + read x     :: Int
                                      nd = d + read x * a :: Int
    ["up", x]      -> (h,d,na)  where na = a - read x     :: Int
    ["down", x]    -> (h,d,na)  where na = a + read x     :: Int
    _              -> (0,0,0)