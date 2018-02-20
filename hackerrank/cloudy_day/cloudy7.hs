
import qualified Data.List                  as L (sort, unfoldr)
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

    let numTowns = head numbers
    let (townInput, numbers') = splitAt (2 * numTowns) (tail numbers)
    let (populations, townPositions) = splitAt numTowns townInput
    let towns = buildOrderedTownList townPositions populations

    let numClouds = head numbers'
    let (cloudPositions, ranges) = splitAt numClouds (tail numbers')
    let clouds = buildOrderedCloudList cloudPositions ranges

    putStrLn $ show (maxSunnyPopulation clouds towns)


parseInts :: B.ByteString -> [Int]
parseInts = L.unfoldr step
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
