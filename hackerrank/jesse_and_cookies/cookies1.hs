
import Data.List (sort, insert)


type Sweetness = Int

minOperations :: Sweetness -> [Sweetness] -> Maybe Int
minOperations minSweet cookies = countOps minSweet hasSweet bitter
  where bitter   = sort (filter (< minSweet) cookies)
        hasSweet = not (null (filter (>= minSweet) cookies))

countOps :: Sweetness -> Bool -> [Sweetness] -> Maybe Int
countOps _ _ [] = Just 0
countOps _ True [_] = Just 1
countOps _ False [_] = Nothing
countOps minSweet hasSweet (c1 : c2 : cookies)
  | combined >= minSweet   = (+1) <$> countOps minSweet True cookies
  | otherwise              = (+1) <$> countOps minSweet hasSweet cookies'
  where combined = c1 + 2 * c2
        cookies' = insert combined cookies

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
