
import qualified Data.List as L (unfoldr)
import qualified Data.Heap as H (MinHeap, size, splitAt, insert, fromList)
import qualified Data.ByteString.Lazy.Char8 as B (ByteString, getContents,
                                                  readInt, drop)

type Sweetness = Int
type CookieList = [Sweetness]
type CookieHeap = H.MinHeap Sweetness

minOperations :: Sweetness -> CookieList -> Maybe Int
minOperations minSweet cookies = countOps minSweet hasSweet bitter
  where bitter   = H.fromList (filter (< minSweet) cookies)
        hasSweet = not (null (filter (>= minSweet) cookies))

countOps :: Sweetness -> Bool -> CookieHeap -> Maybe Int
countOps minSweet hasSweet heap
  | H.size heap == 0              = Just 0
  | H.size heap == 1 && hasSweet  = Just 1
  | H.size heap == 1              = Nothing
  | combined >= minSweet          = (+1) <$> countOps minSweet True heap'
  | otherwise                     = (+1) <$> countOps minSweet hasSweet heap''
  where (cs, heap') = H.splitAt 2 heap
        combined    = (head cs) + 2 * (last cs)
        heap''      = H.insert combined heap'

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
