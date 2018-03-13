
data MinHeap a = Leaf | MinHeap (MinHeap a) a (MinHeap a)
  deriving (Eq, Show)

instance Ord a => Ord (MinHeap a) where
  compare (MinHeap _ x _) (MinHeap _ y _) = compare x y
  compare  Leaf            Leaf           = EQ
  compare  Leaf            _              = LT
  compare  _               Leaf           = GT

singleton :: a -> MinHeap a
singleton x = MinHeap Leaf x Leaf

peek :: MinHeap a -> Maybe a
peek Leaf            = Nothing
peek (MinHeap _ x _) = Just x

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

toAscList :: Ord a => MinHeap a -> [a]
toAscList h = case pop h of
                Nothing      -> []
                Just (v, h') -> v : toAscList h'

height :: MinHeap a -> Int
height Leaf = 1
height (MinHeap l _ r) = 1 + max (height l) (height r)
