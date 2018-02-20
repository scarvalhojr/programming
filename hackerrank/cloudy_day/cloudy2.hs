
import Data.List (sort)


data Town = Town { townPos :: Int, population :: Int }
  deriving (Show, Eq, Ord)

data Cloud = Cloud { startPos :: Int, cloudLength :: Int }
  deriving (Show, Eq, Ord)

type OrderedTowns = [Town]
type OrderedClouds = [Cloud]


main :: IO ()
main = do
    -- ignore first line of input (number of towns)
    _ <- getLine

    p <- getLine
    let populations = map read (words p) :: [Int]
    x <- getLine
    let townPositions = map read (words x) :: [Int]
    let towns = buildOrderedTownList townPositions populations

    -- ignore next line of input (number of clouds)
    _ <- getLine

    y <- getLine
    let cloudPositions = map read (words y) :: [Int]
    r <- getLine
    let ranges = map read (words r) :: [Int]
    let clouds = buildOrderedCloudList cloudPositions ranges

    putStrLn $ show (maxSunnyPopulation clouds towns)


buildOrderedTownList :: [Int] -> [Int] -> OrderedTowns
buildOrderedTownList pos = map (uncurry Town) . sort . zip pos

buildOrderedCloudList :: [Int] -> [Int] -> OrderedClouds
buildOrderedCloudList pos = map (uncurry Cloud) . sort . zipWith convert pos
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
