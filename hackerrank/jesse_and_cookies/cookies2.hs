
import Data.Maybe (fromJust)

-- Min-heap

data MinHeap a = Leaf | MinHeap (MinHeap a) a (MinHeap a)
  deriving (Eq, Show)

instance Ord a => Ord (MinHeap a) where
  compare (MinHeap _ x _) (MinHeap _ y _) = compare x y
  compare  Leaf            Leaf           = EQ
  compare  Leaf            _              = LT
  compare  _               Leaf           = GT

singleton :: a -> MinHeap a
singleton x = MinHeap Leaf x Leaf

merge :: Ord a => MinHeap a -> MinHeap a -> MinHeap a
merge Leaf h = h
merge h Leaf = h
merge h1@(MinHeap l1 m1 r1) h2@(MinHeap l2 m2 r2)
  | m1 <= m2 && l1 == Leaf  = MinHeap h2 m1 r1
  | m1 <= m2 && r1 == Leaf  = MinHeap l1 m1 h2
  | m1 <= m2 && l1 <= r1    = MinHeap (merge h2 l1) m1 r1
  | m1 <= m2                = MinHeap l1 m1 (merge h2 r1)
  | l2 == Leaf              = MinHeap h1 m2 r2
  | r2 == Leaf              = MinHeap l2 m2 h1
  | l2 <= r2                = MinHeap (merge h1 l2) m2 r2
  | otherwise               = MinHeap l2 m2 (merge h1 r2)

insert :: Ord a => a -> MinHeap a -> MinHeap a
insert x h = merge (singleton x) h

pop :: Ord a => MinHeap a -> Maybe (a, MinHeap a)
pop Leaf = Nothing
pop (MinHeap l m r) = Just (m, merge l r)

empty :: MinHeap a -> Bool
empty Leaf = True
empty _    = False

fromList :: Ord a => [a] -> MinHeap a
fromList [] = Leaf
fromList (x:xs) = insert x (fromList xs)

-- Problem functions

type Sweetness = Int
type CookieList = [Sweetness]
type CookieHeap = MinHeap Sweetness

minOperations :: Sweetness -> CookieList -> Maybe Int
minOperations minSweet cookies = countOps minSweet hasSweet bitter
  where bitter   = fromList (filter (< minSweet) cookies)
        hasSweet = not (null (filter (>= minSweet) cookies))

countOps :: Sweetness -> Bool -> CookieHeap -> Maybe Int
countOps minSweet hasSweet cookies
  | empty cookies               = Just 0
  | empty cookies1 && hasSweet  = Just 1
  | empty cookies1              = Nothing
  | combined >= minSweet        = (+1) <$> countOps minSweet True cookies2
  | otherwise                   = (+1) <$> countOps minSweet hasSweet cookies3
  where (c1, cookies1) = fromJust (pop cookies)
        (c2, cookies2) = fromJust (pop cookies1)
        combined       = c1 + 2 * c2
        cookies3       = insert combined cookies2

-- Main function: read input from stdin

main :: IO ()
main = do
  line <- getLine
  let minSweet = read (last (words line)) :: Sweetness
  line <- getLine
  let cookies = map read (words line) :: [Sweetness]
  let minOps = case minOperations minSweet cookies of
                   Nothing -> -1
                   Just m  -> m
  putStrLn $ show minOps
