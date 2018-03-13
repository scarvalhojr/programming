
import qualified Data.Sequence as S (Seq, fromList, sort, length, index, drop,
                                     spanl)
import           Data.Sequence      ((<|), (><))


type Sweetness = Int
type CookieList = [Sweetness]
type CookieSeq = S.Seq Sweetness

minOperations :: Sweetness -> CookieList -> Maybe Int
minOperations minSweet cookies = countOps minSweet hasSweet bitter
  where bitter   = S.sort $ S.fromList (filter (< minSweet) cookies)
        hasSweet = not (null (filter (>= minSweet) cookies))

countOps :: Sweetness -> Bool -> CookieSeq -> Maybe Int
countOps minSweet hasSweet cookies
  | len == 0              = Just 0
  | len == 1 && hasSweet  = Just 1
  | len == 1              = Nothing
  | combined > minSweet   = (+1) <$> countOps minSweet True cookies2
  | otherwise             = (+1) <$> countOps minSweet hasSweet cookies3
  where len      = S.length cookies
        c0       = S.index cookies 0
        c1       = S.index cookies 1
        combined = c0 + 2 * c1
        cookies2 = S.drop 2 cookies
        (le, gt) = S.spanl (< combined) cookies2
        cookies3 = le >< (combined <| gt)

-- Main function: read input from stdin

main :: IO ()
main = do
  line <- getLine
  let minSweet = read (last (words line)) :: Sweetness
  line <- getLine
  let cookies = map read (words line) :: CookieList
  let minOps = case minOperations minSweet cookies of
                   Nothing -> -1
                   Just m  -> m
  putStrLn $ show minOps
