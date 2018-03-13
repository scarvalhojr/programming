
import           Data.Maybe                       (fromJust)
import           Data.Ord                         (comparing, Down(..))
import qualified Data.List                   as L (unfoldr)
import qualified Data.Vector                 as V (Vector, length, fromList,
                                                   modify, unsafeIndex)
import qualified Data.Vector.Algorithms.Heap as H (heapify, pop, heapInsert)
import qualified Data.ByteString.Lazy.Char8  as B (ByteString, getContents,
                                                   readInt, drop)


data MinHeap a = MinHeap { vector :: V.Vector a, heapSize :: Int }

minHeapOrd :: Ord a => a -> a -> Ordering
minHeapOrd = comparing Down

minHeapBuild :: (Ord a) => [a] -> MinHeap a
minHeapBuild xs = MinHeap vec' size
  where vec  = V.fromList xs
        size = V.length vec
        vec' = V.modify (\v -> H.heapify minHeapOrd v 0 size) vec

minHeapInsert :: (Ord a) => MinHeap a -> a -> MinHeap a
minHeapInsert (MinHeap vec size) x
  | size == V.length vec  = error "Exceeded heap capacity"
  | otherwise             = MinHeap vec' (size + 1)
  where vec'  = V.modify (\v -> H.heapInsert minHeapOrd v 0 size x) vec

minHeapPop :: Ord a => MinHeap a -> Maybe (a, MinHeap a)
minHeapPop (MinHeap vec size)
  | size == 0   = Nothing
  | otherwise   = Just (x, MinHeap vec' size')
  where size' = size - 1
        vec'  = V.modify (\v -> H.pop minHeapOrd v 0 size') vec
        x     = V.unsafeIndex vec' size'

heapEmpty :: MinHeap a -> Bool
heapEmpty = (==0) . heapSize

---

type Sweetness = Int
type CookieList = [Sweetness]
type CookieHeap = MinHeap Sweetness

minOperations :: Sweetness -> CookieList -> Maybe Int
minOperations minSweet cookies = countOps minSweet hasSweet bitter
  where bitter   = minHeapBuild (filter (< minSweet) cookies)
        hasSweet = not (null (filter (>= minSweet) cookies))

countOps :: Sweetness -> Bool -> CookieHeap -> Maybe Int
countOps minSweet hasSweet heap
  | heapEmpty heap               = Just 0
  | heapEmpty heap1 && hasSweet  = Just 1
  | heapEmpty heap1              = Nothing
  | combined >= minSweet         = (+1) <$> countOps minSweet True heap2
  | otherwise                    = (+1) <$> countOps minSweet hasSweet heap3
  where (c1, heap1) = fromJust (minHeapPop heap)
        (c2, heap2) = fromJust (minHeapPop heap1)
        combined    = c1 + 2 * c2
        heap3       = minHeapInsert heap2 combined

-- Main function: read input from stdin

main :: IO ()
main = do
  line1 <- getLine
  let minSweet = read (last (words line1)) :: Sweetness
  line2 <- B.getContents
  let cookies = parseInts line2
  let minOps = case minOperations minSweet cookies of
                   Nothing -> -1
                   Just m  -> m
  putStrLn $ show minOps

parseInts :: B.ByteString -> [Int]
parseInts = L.unfoldr step
  where step bs = case B.readInt bs of
                    Nothing     -> Nothing
                    Just (k, t) -> Just (k, B.drop 1 t)
