
import qualified Data.List                  as L (sort)
import qualified Data.Vector                as V (Vector, unfoldr, toList, head,
                                                  tail, splitAt)
import qualified Data.ByteString.Lazy.Char8 as B (ByteString, getContents,
                                                  readInt, drop)


data Town = Town { townPos :: Int, population :: Int }
  deriving (Show, Eq, Ord)

data Cloud = Cloud { startPos :: Int, cloudLength :: Int }
  deriving (Show, Eq, Ord)

type OrderedTowns = [Town]
type OrderedClouds = [Cloud]


main :: IO ()
main = do
    input <- B.getContents
    let numbers = parseInts input

    let numTowns = V.head numbers
    let (townInput, numbers') = V.splitAt (2 * numTowns) (V.tail numbers)
    let (populations, townPositions) = V.splitAt numTowns townInput
    let towns = buildOrderedTownList (V.toList townPositions) (V.toList populations)

    let numClouds = V.head numbers'
    let (cloudPositions, ranges) = V.splitAt numClouds (V.tail numbers')
    let clouds = buildOrderedCloudList (V.toList cloudPositions) (V.toList ranges)

    putStrLn $ show (maxSunnyPopulation clouds towns)


parseInts :: B.ByteString -> V.Vector Int
parseInts = V.unfoldr step
  where step bs = case B.readInt bs of
                    Nothing     -> Nothing
                    Just (k, t) -> Just (k, B.drop 1 t)

buildOrderedTownList :: [Int] -> [Int] -> OrderedTowns
buildOrderedTownList pos = L.sort . map (uncurry Town) . zip pos

buildOrderedCloudList :: [Int] -> [Int] -> OrderedClouds
buildOrderedCloudList pos = L.sort . map (uncurry Cloud) . zipWith convert pos
  where convert p r = (p - r, 2 * r)

maxSunnyPopulation :: OrderedClouds -> OrderedTowns -> Int
maxSunnyPopulation clouds towns = sunnyPopulation + maxUncoverablePopulation
  where (sunnyTowns, singleCloudTowns) = selectTowns towns clouds
        sunnyPopulation                = sumPopulation sunnyTowns
        maxUncoverablePopulation       = maxUncover clouds singleCloudTowns

selectTowns :: OrderedTowns -> OrderedClouds -> (OrderedTowns, OrderedTowns)
selectTowns [] _  = ([], [])
selectTowns ts [] = (ts, [])
selectTowns towns@(t:ts) clouds@(c:cs)
  | comparePosition t c == GT   = selectTowns towns cs
  | comparePosition t c == LT   = ([t], []) `mappend` selectTowns ts clouds
  | isSunny t cs                = ([], [t]) `mappend` selectTowns ts clouds
  | otherwise                   = selectTowns ts clouds

isSunny :: Town -> OrderedClouds -> Bool
isSunny town = all (not . covers town) . takeWhile lessOrEqual
  where lessOrEqual = ((> LT) . comparePosition town)

maxUncover :: OrderedClouds -> OrderedTowns -> Int
maxUncover = findMax 0
  where findMax m [] _ = m
        findMax m _ [] = m
        findMax m clouds@(c:cs) towns@(t:ts) =
          case comparePosition t c of
            LT -> findMax m clouds ts
            GT -> findMax m cs towns
            EQ -> findMax (max m (coveredPopulation c towns)) cs ts

coveredPopulation :: Cloud -> OrderedTowns -> Int
coveredPopulation cloud = sumPopulation . takeWhile (flip covers cloud)

comparePosition :: Town -> Cloud -> Ordering
comparePosition (Town tp _) (Cloud cp l)
  | tp < cp       = LT
  | tp > cp + l   = GT
  | otherwise     = EQ

covers :: Town -> Cloud -> Bool
covers town = (== EQ) . comparePosition town

sumPopulation :: [Town] -> Int
sumPopulation = sum . map population
